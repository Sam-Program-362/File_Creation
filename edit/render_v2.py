#!/usr/bin/env python3
"""
Dying Of Death Pt. II — v2 renderer.
Cinematic code-rendered nature scenes (rain window, storm, lightning, ocean,
snow, fog valley, burning sunset sky, fireflies) + grid-locked beat cuts +
vocal-phrase-aligned captions. Every scene is a pure function of time, so
camera cuts inside a scene are seamless. 1080x1920 @30fps.
"""
import numpy as np, json, os, time, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import imageio_ffmpeg

W, H, FPS = 1080, 1920, 30
BUFW, BUFH = 1350, 2400
LOWW, LOWH = 270, 480          # low-res base for soft fields, upscaled 5x
LR_SCALE = 5
WORK = 'work'
plan = json.load(open(f'{WORK}/plan.json'))
dips = json.load(open(f'{WORK}/dips.json'))['dips']
DUR = plan['duration']
GRID = np.array(plan['grid'])
HITS = np.array(plan['hits'])
VE = np.load(f'{WORK}/ve.npy')
VE_T = np.arange(len(VE)) * 512 / 22050.0
TOTAL_FRAMES = int(os.environ.get("TEST_FRAMES", 0)) or int(DUR * FPS)
rng0 = np.random.default_rng(11)

def snap_grid(t):
    i = int(np.argmin(np.abs(GRID - t)))
    return float(GRID[i])

# ================================================================ sections
SECTIONS = [  # (name, start, end, scene key, cut-grid-steps pattern, intensity)
    ('verse',  0.0,   snap_grid(24.85), 'rain',    [8],            0),
    ('build',  None,  snap_grid(36.76), 'storm',   [4],            1),
    ('drop1a', None,  snap_grid(49.06), 'storm',   [4, 4, 2, 2],   2),
    ('drop1b', None,  snap_grid(61.35), 'ocean',   [4, 2, 4, 2],   2),
    ('drop1c', None,  snap_grid(73.65), 'lightning',[2, 4, 2, 4],  2),
    ('bridge', None,  snap_grid(80.5),  'snow',    [4],            0),
    ('bridge2',None,  snap_grid(87.89), 'fog',     [4, 4, 2, 2],   1),
    ('drop2',  None,  snap_grid(97.06), 'sunset',  [2],            3),
    ('outro',  None,  DUR,              'fireflies',[8, 8],        0),
]
for i, s in enumerate(SECTIONS):
    if s[1] is None:
        SECTIONS[i] = (s[0], SECTIONS[i-1][2], s[2], s[3], s[4], s[5])
SEC_STARTS = [round(s[1] * FPS) for s in SECTIONS if s[1] > 0.1]
SEC_INFO = {s[0]: s for s in SECTIONS}

# ================================================================ timeline (grid-locked)
CAMERAS = [  # (zoom0, zoom1, panx, pany) — crop windows into the 1350x2400 scene buffer
    (1.00, 1.10,  50, -30), (1.12, 1.02, -60,  40), (1.02, 1.14, -40, -50),
    (1.15, 1.03,  60,  30), (1.05, 1.18,  30,  50), (1.18, 1.06, -50, -20),
    (1.03, 1.11,  70,   0), (1.11, 1.01,   0, -60), (1.06, 1.16, -30,  40),
]
clips = []
for name, start, end, scene, pattern, inten in SECTIONS:
    b = GRID[(GRID >= start - 1e-6) & (GRID < end - 1e-6)]
    cuts = list(b)
    if cuts[0] > start + 0.01: cuts.insert(0, start)
    cuts.append(end)
    i = k = 0
    seg = []
    while i < len(cuts) - 1:
        j = min(i + pattern[k % len(pattern)], len(cuts) - 1)
        if cuts[j] - cuts[i] < 0.5 and j < len(cuts) - 1: j = j + 1
        seg.append((cuts[i], cuts[min(j, len(cuts)-1)])); i = j; k += 1
    if seg[-1][1] < end: seg[-1] = (seg[-1][0], end)
    for j, (a, bnd) in enumerate(seg):
        z0, z1, px, py = CAMERAS[(j + len(name)) % len(CAMERAS)]
        if inten == 3: z0, z1 = z0 + 0.03, z1 + 0.12
        clips.append(dict(t0=a, t1=bnd, scene=scene, cam=(z0, z1, px, py),
                          sec=name, inten=inten, seed=int(rng0.integers(1e6))))
print(f'{len(clips)} clips, all grid-locked')
maxdev = max(min(abs(np.array(GRID) - c['t0']).min(), abs(np.array(GRID) - c['t1']).min()) for c in clips if c['t0'] > 0.2)
print(f'max cut deviation from tempo grid: {maxdev*1000:.1f} ms')

# ================================================================ scenes (pure functions of t)
def vfield(resx, resy, cell, rng, octaves=5, persistence=0.55):
    """fractal value noise field in [0,1], low-res"""
    out = np.zeros((resy, resx), np.float32)
    amp, total = 1.0, 0.0
    for o in range(octaves):
        c = max(2, int(cell / (2 ** o)))
        gx = rng.random((resy // c + 2, resx // c + 2)).astype(np.float32)
        im = Image.fromarray(gx, mode='F').resize((resx, resy), Image.BILINEAR)
        out += np.asarray(im) * amp
        total += amp; amp *= persistence
    return out / total

def grad_sky(top, bottom):
    t = np.linspace(0, 1, LOWH, dtype=np.float32)[:, None, None]
    top = np.array(top, np.float32)[None, None, :]
    bot = np.array(bottom, np.float32)[None, None, :]
    return (top * (1 - t) + bot * t).repeat(LOWW, axis=1)

def soft_blob_overlay(draw_list, blur=8):
    """draw gaussian glow dots on half-res then upscale-blur"""
    im = Image.new('RGBA', (LOWW * 2, LOWH * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for (x, y, r, col) in draw_list:
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    im = im.filter(ImageFilter.GaussianBlur(blur)).resize((LOWW * LR_SCALE, LOWH * LR_SCALE), Image.BILINEAR)
    return im

_RIDGE_CACHE = {}
def ridgeline(seed, base_frac, amp_frac, resx=270):
    key = (seed, round(base_frac, 3), round(amp_frac, 3))
    if key in _RIDGE_CACHE:
        return _RIDGE_CACHE[key]
    r = np.random.default_rng(seed)
    n = vfield(resx, 1, 60, r, octaves=4).ravel()
    y = base_frac - (n - n.min()) / (np.ptp(n) + 1e-6) * amp_frac
    _RIDGE_CACHE[key] = y
    return y  # per-x height fraction

def draw_ridgeline(d, ys, color, low2full=LR_SCALE):
    pts = [(x * 4 * low2full, float(y) * LOWH * low2full) for x, y in enumerate(ys)]
    pts += [BUFW, BUFH, 0, BUFH]
    d.polygon(pts, fill=color)

def scene_rain(t, seed, inten=1.0):
    r = np.random.default_rng(seed)
    base = grad_sky((16, 22, 34), (34, 44, 62))
    # distant city glow
    city = np.zeros((LOWH, LOWW, 3), np.float32)
    for _ in range(9):
        cx, cy = r.uniform(0, LOWW), r.uniform(0.45, 0.75) * LOWH
        col = r.choice([[255, 190, 120], [150, 200, 255], [255, 150, 110], [190, 170, 255]])
        w, h = r.uniform(30, 90), r.uniform(20, 60)
        xx, yy = np.meshgrid(np.arange(LOWW), np.arange(LOWH))
        g = np.exp(-(((xx - cx) / w) ** 2 + ((yy - cy) / h) ** 2))[..., None]
        city += np.array(col, np.float32)[None, None, :] * g
    base = np.clip(base + city * 0.16 * inten, 0, 255)
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    # bokeh blobs
    blobs = [(r.uniform(0, BUFW), r.uniform(0.5, 0.85) * BUFH, r.uniform(18, 55),
              tuple(int(c) for c in r.choice([[255,200,140],[160,210,255],[255,160,120]]) ) + (int(r.uniform(40, 90)),))
             for _ in range(12)]
    img.alpha_composite(soft_blob_overlay(blobs, blur=10))
    # rain streaks
    ov = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    n = int(200 * inten)
    for i in range(n):
        rs = np.random.default_rng(seed * 7919 + i)
        speed = rs.uniform(1100, 1900); L = rs.uniform(45, 110)
        x = (rs.uniform(0, BUFW) + rs.uniform(-160, -60) * t) % (BUFW + 200) - 100
        y = (rs.uniform(0, BUFH) + speed * t) % (BUFH + 150) - 75
        a = int(rs.uniform(28, 80))
        d.line([x, y, x - L * 0.22, y + L], fill=(185, 205, 235, a), width=rs.choice([1, 1, 2]))
    img.alpha_composite(ov)
    # glass droplets with trails
    ov2 = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); d2 = ImageDraw.Draw(ov2)
    for i in range(46):
        rs = np.random.default_rng(seed * 104729 + i)
        x = rs.uniform(0, BUFW); v = rs.uniform(28, 95)
        y = (rs.uniform(0, BUFH) + v * t) % (BUFH + 60) - 30
        rad = rs.uniform(3, 9)
        for k in range(4):
            ya = y - k * rad * 2.4
            al = max(10, 110 - k * 28)
            d2.ellipse([x - rad * (1 - k * 0.16), ya - rad * (1 - k * 0.16),
                        x + rad * (1 - k * 0.16), ya + rad * (1 - k * 0.16)],
                       fill=(205, 225, 250, al))
    img.alpha_composite(ov2)
    return np.asarray(img.convert('RGB')).copy()

def storm_base(t, seed, dark, warm=False):
    """churning cloud field shared by storm scenes (windowed noise: no seams)"""
    W2 = LOWW * 2
    f1 = vfield(W2, LOWH, 90, np.random.default_rng(seed + 1), octaves=5)
    f2 = vfield(W2, LOWH, 40, np.random.default_rng(seed + 2), octaves=4)
    o1 = int((t * 6) % LOWW); o2 = int((t * 14) % LOWW)
    f1 = f1[:, o1:o1 + LOWW]; f2 = f2[:, o2:o2 + LOWW]
    f = 0.62 * f1 + 0.38 * f2
    if not warm:
        top = (10 + dark * 6, 11 + dark * 6, 16 + dark * 8)
        bot = (46 - dark * 10, 48 - dark * 10, 60 - dark * 12)
        sky = grad_sky(top, bot)
        col = np.stack([f * (70 - dark * 12) + 18, f * (70 - dark * 12) + 20, f * (80 - dark * 12) + 28], -1)
    else:
        sky = grad_sky((26, 12, 16), (60, 24, 20))
        col = np.stack([f * 150 + 30, f * 58 + 12, f * 44 + 10], -1)
    out = np.clip(sky * 0.35 + col * 0.85, 0, 255)
    return out

def scene_storm(t, seed, inten=1.0, warm=False, bolts=False):
    dark = np.clip(t / 40.0, 0, 1)
    base = storm_base(t, seed, dark, warm)
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    # rain (heavier with inten)
    ov = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    gust = 1.0 + 0.5 * np.sin(t * 0.9 + seed % 7)
    n = int(330 * inten)
    for i in range(n):
        rs = np.random.default_rng(seed * 31 + i)
        speed = rs.uniform(1500, 2500); L = rs.uniform(70, 150)
        wind = 240 * gust
        x = (rs.uniform(0, BUFW) - wind * t) % (BUFW + 260) - 130
        y = (rs.uniform(0, BUFH) + speed * t) % (BUFH + 180) - 90
        d.line([x, y, x - L * (wind / 1800), y + L], fill=(190, 208, 235, int(rs.uniform(26, 66))), width=1)
    img.alpha_composite(ov)
    # lightning flashes at hit times mod clip-local
    flash = 0.0; boltpts = None
    if bolts:
        rb = np.random.default_rng(seed)
        bt0 = rb.uniform(2, 4)
        for k in range(3):
            ft = bt0 + k * rb.uniform(3.2, 5.2)
            dt = t - ft
            if 0 <= dt < 0.55:
                flash = max(flash, float(np.exp(-dt * 9)))
                if dt < 0.22 and boltpts is None:
                    # recursive midpoint bolt
                    pts = []
                    x, y = rb.uniform(0.25, 0.75) * BUFW, -30
                    while y < BUFH * rb.uniform(0.55, 0.9):
                        pts.append((x, y)); x += rb.uniform(-90, 90); y += rb.uniform(70, 150)
                    boltpts = pts
    if flash > 0:
        flash_img = Image.new("RGBA", (BUFW, BUFH), (225, 232, 248, int(min(0.30, flash * 0.30) * 255)))
        img.alpha_composite(flash_img)
        if boltpts:
            bo = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); bd = ImageDraw.Draw(bo)
            for wd, al in [(16, 60), (8, 130), (3, 255)]:
                bd.line(boltpts, fill=(235, 240, 255, al), width=wd, joint='curve')
            bo = bo.filter(ImageFilter.GaussianBlur(4))
            img.alpha_composite(bo)
    return np.asarray(img.convert('RGB')).copy()

def scene_ocean(t, seed):
    r = np.random.default_rng(seed)
    base = storm_base(t, seed, dark=0.3)
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    d = ImageDraw.Draw(img, 'RGBA')
    horizon = 0.44 * BUFH
    d.rectangle([0, horizon, BUFW, BUFH], fill=(10, 18, 30, 255))
    # water body gradient
    wat = Image.new('RGBA', (BUFW, BUFH - int(horizon)), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wat)
    for gy in range(wat.height):
        fz = gy / wat.height
        wd.line([0, gy, BUFW, gy], fill=(int(12 + 14 * fz), int(22 + 16 * fz), int(34 + 18 * fz), 255))
    img.alpha_composite(wat, (0, int(horizon)))
    d = ImageDraw.Draw(img, 'RGBA')
    # moon glare path: scattered shimmering glints
    gx = BUFW * 0.62
    for gi in range(90):
        rs = np.random.default_rng(int(seed * 3 + gi))
        fz = rs.random() ** 0.8
        gy = horizon + (BUFH - horizon) * fz
        gw = 14 + 110 * fz
        wob = 34 * np.sin(t * 1.1 + fz * 9) * fz
        x = gx + wob + rs.normal(0, gw * 0.5)
        w = rs.uniform(0.3, 1.0) * gw * 0.45
        ga = int((38 - 22 * fz) * rs.uniform(0.5, 1.0))
        d.ellipse([x - w, gy - 2, x + w, gy + 2], fill=(215, 225, 242, ga))
    # wave bands
    for layer in range(14):
        lz = layer / 13.0
        yb = horizon + (BUFH - horizon) * (lz ** 1.5)
        amp = 5 + 30 * lz; speed = 60 + 240 * lz
        ph = t * speed * 0.02 + layer * 1.7
        pts = [(x, yb + amp * np.sin(x / (90 - 60 * lz) + ph) + amp * 0.5 * np.sin(x / (37 - 20 * lz) - ph * 1.3))
               for x in range(0, BUFW + 16, 16)]
        shade = int(26 + 34 * lz)
        d.line(pts, fill=(shade, shade + 10, shade + 22, 255), width=int(3 + 8 * lz), joint='curve')
        # crest highlights
        hx = [p[0] for p in pts]; hy = [p[1] for p in pts]
        for k in range(0, len(pts) - 1, 3):
            if hy[k] < yb - amp * 0.55:
                d.ellipse([hx[k] - 5 * lz - 1, hy[k] - 1.5, hx[k] + 5 * lz + 1, hy[k] + 1.5],
                          fill=(185, 205, 230, int(30 + 60 * lz)))
    # rain overlay light
    ov = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); dd = ImageDraw.Draw(ov)
    for i in range(150):
        rs = np.random.default_rng(seed * 17 + i)
        x = (rs.uniform(0, BUFW) - 200 * t) % (BUFW + 200) - 100
        y = (rs.uniform(0, BUFH) + rs.uniform(1600, 2300) * t) % (BUFH + 160) - 80
        dd.line([x, y, x - 12, y + 90], fill=(190, 205, 230, 30), width=1)
    img.alpha_composite(ov)
    return np.asarray(img.convert('RGB')).copy()

def scene_snow(t, seed):
    r = np.random.default_rng(seed)
    base = grad_sky((10, 16, 30), (30, 40, 58))
    xx = np.meshgrid(np.arange(LOWW), np.arange(LOWH))[1]
    base[..., 0] += 60 * np.exp(-((xx - LOWH * 0.30) ** 2) / (2 * 40 ** 2))[:, 0][:, None].repeat(LOWW, 1)[:, :] if False else 0
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    # moon
    d = ImageDraw.Draw(img, 'RGBA')
    mx, my = BUFW * 0.68, BUFH * 0.24
    d.ellipse([mx - 130, my - 130, mx + 130, my + 130], fill=(190, 200, 230, 26))
    d.ellipse([mx - 90, my - 90, mx + 90, my + 90], fill=(200, 210, 235, 40))
    d.ellipse([mx - 52, my - 52, mx + 52, my + 52], fill=(235, 240, 250, 235))
    # tree layers
    for li, (bf, af, col) in enumerate([(0.86, 0.16, (14, 20, 32)), (0.94, 0.22, (8, 12, 22))]):
        ys = ridgeline(seed + 40 + li, bf, af)
        pts = [(x * 5, float(y) * LOWH * 5) for x, y in enumerate(ys)] + [BUFW, BUFH, 0, BUFH]
        # jagged pines
        d.polygon(pts, fill=col)
    # snow
    ov = Image.new('RGBA', (BUFW, BUFH), (0, 0, 0, 0)); dd = ImageDraw.Draw(ov)
    for i in range(240):
        rs = np.random.default_rng(seed * 61 + i)
        spd = rs.uniform(50, 160); sz = rs.uniform(1.6, 6.5); sw = rs.uniform(20, 90); sf = rs.uniform(0.4, 1.4)
        x = (rs.uniform(0, BUFW) + sw * np.sin(t * sf + rs.uniform(0, 6.28))) % BUFW
        y = (rs.uniform(0, BUFH) + spd * t) % (BUFH + 40) - 20
        al = int(rs.uniform(70, 190))
        dd.ellipse([x - sz, y - sz, x + sz, y + sz], fill=(230, 238, 250, al))
        if sz > 4.5:
            dd.ellipse([x - sz * 2.2, y - sz * 2.2, x + sz * 2.2, y + sz * 2.2], fill=(230, 238, 250, 28))
    img.alpha_composite(ov)
    return np.asarray(img.convert('RGB')).copy()

def scene_fog(t, seed):
    r = np.random.default_rng(seed)
    base = grad_sky((22, 30, 40), (56, 68, 82))
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    d = ImageDraw.Draw(img, 'RGBA')
    layers = [(0.50, 0.22, (92, 104, 118, 255), 14), (0.62, 0.20, (66, 78, 92, 255), 10),
              (0.74, 0.16, (44, 54, 66, 255), 6), (0.88, 0.12, (26, 33, 42, 255), 0)]
    for i, (bf, af, col, fog_a) in enumerate(layers):
        ys = ridgeline(seed + i * 13, bf, af)
        pts = [(x * 5, float(y) * LOWH * 5) for x, y in enumerate(ys)] + [BUFW, BUFH, 0, BUFH]
        d.polygon(pts, fill=col)
        # fog band drifting
        fa = fog_a * (0.75 + 0.25 * np.sin(t * 0.5 + i))
        yf = bf * BUFH + 40 * np.sin(t * 0.3 + i * 2)
        grad = Image.new('RGBA', (BUFW, 340), (0, 0, 0, 0))
        gd = ImageDraw.Draw(grad)
        for gy in range(340):
            a = int(fa * 24 * np.exp(-((gy - 170) / 130) ** 2))
            gd.line([0, gy, BUFW, gy], fill=(175, 190, 205, a))
        grad = grad.filter(ImageFilter.GaussianBlur(26))
        off = int((t * (8 + i * 5)) % BUFW)
        band = Image.new('RGBA', (BUFW * 2, 340))
        band.paste(grad, (0, 0)); band.paste(grad, (BUFW, 0))
        img.alpha_composite(band.crop((off % BUFW, 0, off % BUFW + BUFW, 340)), (0, int(yf - 170)))
    return np.asarray(img.convert('RGB')).copy()

def scene_sunset(t, seed):
    """burning red sky — 'beautiful sky' irony"""
    r = np.random.default_rng(seed)
    W2 = LOWW * 2
    f1 = vfield(W2, LOWH, 70, np.random.default_rng(seed + 5), octaves=5)
    f2 = vfield(W2, LOWH, 30, np.random.default_rng(seed + 6), octaves=4)
    f1 = f1[:, int((t * 26) % LOWW):int((t * 26) % LOWW) + LOWW]
    f2 = f2[:, int((t * 44) % LOWW):int((t * 44) % LOWW) + LOWW]
    f = np.clip(0.60 * f1 + 0.40 * f2, 0, 1)
    yy = np.linspace(0, 1, LOWH)[:, None]
    # palette: deep crimson top -> fire orange bottom, darker with time
    dk = np.clip(0.25 + t * 0.02, 0, 0.6)
    r_ch = (150 + 105 * f) * (1 - 0.5 * yy) * (1 - dk * 0.4)
    g_ch = (26 + 60 * f ** 1.6) * (1 - 0.3 * yy) * (1 - dk * 0.5)
    b_ch = (18 + 30 * f ** 2.2) * (1 - dk * 0.5)
    base = np.clip(np.stack([r_ch, g_ch, b_ch], -1), 0, 255)
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    # low sun glow
    blobs = [(BUFW * 0.5, BUFH * 0.72, 260, (255, 120, 40, 60)), (BUFW * 0.5, BUFH * 0.72, 120, (255, 170, 70, 70))]
    img.alpha_composite(soft_blob_overlay(blobs, blur=16))
    # dark cloud depth: soft blobs, drifting
    blobs = []
    for bi in range(7):
        rs = np.random.default_rng(seed + 300 + bi)
        bx = (rs.uniform(0, BUFW) + t * rs.uniform(4, 14)) % (BUFW + 400) - 200
        by = rs.uniform(0.04, 0.42) * BUFH
        br = rs.uniform(90, 220)
        al = int(rs.uniform(26, 60))
        blobs.append((bx, by, br, (26, 8, 10, al)))
    img.alpha_composite(soft_blob_overlay(blobs, blur=22))
    return np.asarray(img.convert('RGB')).copy()

def scene_fireflies(t, seed):
    base = grad_sky((6, 14, 18), (14, 34, 30))
    img = Image.fromarray(base.astype(np.uint8)).resize((BUFW, BUFH), Image.BILINEAR).convert('RGBA')
    d = ImageDraw.Draw(img, 'RGBA')
    # stars
    for i in range(60):
        rs = np.random.default_rng(seed + i)
        x, y = rs.uniform(0, BUFW), rs.uniform(0, BUFH * 0.5)
        al = int(60 + 60 * np.sin(t * 2 + i)) if rs.random() > 0.5 else 90
        d.ellipse([x - 1.5, y - 1.5, x + 1.5, y + 1.5], fill=(220, 230, 240, al))
    # tree line
    ys = ridgeline(seed + 9, 0.88, 0.18)
    pts = [(x * 5, float(y) * LOWH * 5) for x, y in enumerate(ys)] + [BUFW, BUFH, 0, BUFH]
    d.polygon(pts, fill=(4, 10, 9, 255))
    # fireflies
    fl = Image.new('RGBA', (BUFW // 2, BUFH // 2), (0, 0, 0, 0)); fd = ImageDraw.Draw(fl)
    for i in range(42):
        rs = np.random.default_rng(seed * 89 + i)
        ph = rs.uniform(0, 6.28); sp = rs.uniform(0.8, 2.2)
        pulse = 0.5 + 0.5 * np.sin(t * sp + ph)
        x = (rs.uniform(0, BUFW) + rs.uniform(-30, 30) * np.sin(t * 0.5 + ph)) / 2
        y = (rs.uniform(BUFH * 0.45, BUFH * 0.92) + rs.uniform(-24, 24) * np.cos(t * 0.4 + ph)) / 2
        rad = rs.uniform(2.5, 5.5)
        al = int(30 + 215 * pulse ** 2)
        fd.ellipse([x - rad, y - rad, x + rad, y + rad], fill=(200, 255, 140, al))
        fd.ellipse([x - rad * 3, y - rad * 3, x + rad * 3, y + rad * 3], fill=(160, 255, 120, int(al * 0.18)))
    fl = fl.filter(ImageFilter.GaussianBlur(3)).resize((BUFW, BUFH), Image.BILINEAR)
    img.alpha_composite(fl)
    return np.asarray(img.convert('RGB')).copy()

SCENE_FN = {
    'rain':      lambda t, s: scene_rain(t, s, 1.0),
    'storm':     lambda t, s: scene_storm(t, s, 1.0, bolts=False),
    'lightning': lambda t, s: scene_storm(t, s, 1.35, bolts=True),
    'ocean':     lambda t, s: scene_ocean(t, s),
    'snow':      lambda t, s: scene_snow(t, s),
    'fog':       lambda t, s: scene_fog(t, s),
    'sunset':    lambda t, s: scene_sunset(t, s),
    'fireflies': lambda t, s: scene_fireflies(t, s),
}

# ================================================================ captions (dip-aligned)
WHITE = (255, 255, 255); RED = (255, 64, 44); AMBER = (255, 178, 64); ICE = (170, 215, 255)
PHRASE_MAP = {'beautiful sky': AMBER, 'safe here': ICE, "death's fear": RED, 'explosions and fire': RED}
SOLO_RED = {'liar', 'explosions', 'fire', "death's", 'fear'}

CAPS = [
 (2.00,  8.13, "It's a beautiful sky,\nI agree, but I'm a liar", 78, 'verse'),
 (8.13, 13.35, "'Cause all that I see\nis explosions and fire", 78, 'verse'),
 (13.35, 17.37, "Not a real person,\njust a vessel for death's fear", 64, 'verse'),
 (17.37, 24.85, "Unsure of its purpose,\nbut I know that it's safe here", 64, 'verse'),
 (24.85, 29.72, "IT'S A BEAUTIFUL SKY,\nI AGREE, BUT I'M A LIAR", 70, 'drop'),
 (29.72, 36.76, "ALL THAT I SEE IS\nEXPLOSIONS AND FIRE", 78, 'drop'),
 (36.76, 42.03, "IT'S A BEAUTIFUL SKY", 96, 'drop'),
 (42.03, 45.05, "I AGREE,\nBUT I'M A LIAR", 88, 'drop'),
 (45.05, 49.06, "EXPLOSIONS\nAND FIRE", 100, 'drop'),
 (49.06, 55.19, "NOT A REAL PERSON,\nJUST A VESSEL FOR DEATH'S FEAR", 62, 'drop'),
 (55.19, 61.35, "UNSURE OF ITS PURPOSE,\nBUT I KNOW THAT IT'S SAFE HERE", 58, 'drop'),
 (61.35, 66.34, "WHAT A\nBEAUTIFUL SKY", 130, 'drop'),
 (66.34, 69.66, "I AGREE,\nBUT I'M A LIAR", 88, 'drop'),
 (69.66, 73.65, "EXPLOSIONS\nAND FIRE", 100, 'drop'),
 (73.65, 76.16, "BEAUTIFUL SKY", 124, 'bridge'),
 (76.16, 78.20, "BEAUTIFUL SKY", 124, 'bridge'),
 (78.20, 80.50, "BEAUTIFUL SKY", 124, 'bridge'),
 (80.50, 86.01, "NOT A REAL PERSON,\nJUST A VESSEL FOR DEATH'S FEAR", 62, 'drop'),
 (86.01, 87.89, "UNSURE\nOF ITS PURPOSE", 72, 'drop'),
 (87.89, 90.95, "WHAT A\nBEAUTIFUL SKY", 120, 'drop'),
 (90.95, 94.04, "I AGREE,\nBUT I'M A LIAR", 84, 'drop'),
 (94.04, 96.73, "EXPLOSIONS\nAND FIRE", 96, 'drop'),
 (97.30, 102.20, "unsure of its purpose,\nbut I know that it's safe here", 50, 'outro'),
]

def paint_colors(text):
    toks = text.replace('\n', ' \n ').split(' ')
    low = [t.lower().strip(',.?!') for t in toks]
    colors = [None] * len(toks)
    for i, t in enumerate(toks):
        if t == '\n': continue
        for span in (3, 2):
            if i + span - 1 < len(low) and ' '.join(low[i:i+span]) in PHRASE_MAP:
                c = PHRASE_MAP[' '.join(low[i:i+span])]
                for k in range(span): colors[i + k] = c
                break
        else:
            if low[i] in SOLO_RED: colors[i] = RED
    return colors, toks

font_cache = {}
def get_font(size):
    if size not in font_cache:
        font_cache[size] = ImageFont.truetype('assets/Anton-Regular.ttf', size)
    return font_cache[size]

print('pre-rendering caption sprites ...')
MAXW = 980
CAP_SPRITES = []
for (t0, t1, text, size, style) in CAPS:
    font = get_font(size)
    colors, toks = paint_colors(text)
    lines, cur, curw = [], [], 0
    spacew = font.getlength(' ')
    idx = 0
    for tok in toks:
        if tok == '\n':
            lines.append(cur); cur, curw = [], 0; continue
        wl = font.getlength(tok)
        if cur and curw + spacew + wl > MAXW:
            lines.append(cur); cur, curw = [], 0
        cur.append((tok, wl, idx)); curw += wl + (spacew if len(cur) > 1 else 0)
        idx += 1
    if cur: lines.append(cur)
    line_h = int(size * 1.22)
    line_widths = [sum(w for _, w, _ in ln) + spacew * (len(ln) - 1) for ln in lines]
    total_h = line_h * len(lines)
    sprites = []
    sw = int(size * 0.09) + 5
    for li, ln in enumerate(lines):
        x = 0.0
        for (tok, wl, ti) in ln:
            col = colors[ti] or WHITE
            sp = Image.new('RGBA', (int(wl) + sw * 2 + 40, line_h + sw * 2 + 12), (0, 0, 0, 0))
            dr = ImageDraw.Draw(sp)
            dr.text((sw + 20 + 5, sw + 9), tok, font=font, fill=(0, 0, 0, 200), stroke_width=sw, stroke_fill=(0, 0, 0, 200))
            sp = sp.filter(ImageFilter.GaussianBlur(5))
            dr = ImageDraw.Draw(sp)
            dr.text((sw + 20, sw + 4), tok, font=font, fill=col + (255,), stroke_width=sw, stroke_fill=(0, 0, 0, 255))
            sprites.append((np.asarray(sp).copy(), sp.width, sp.height, li, x, ti))
            x += wl + spacew
    CAP_SPRITES.append(dict(t0=t0, t1=t1, sprites=sprites, line_h=line_h,
                            total_h=total_h, line_widths=line_widths, style=style))
print(f'  {len(CAP_SPRITES)} captions ready')

# ================================================================ fx
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r_n = np.sqrt(((xx - W/2) / (W/2))**2 + ((yy - H/2) / (H/2))**2)
VIGNETTE = (0.66 + 0.34 * np.clip(1.15 - r_n * 0.8, 0, 1)).astype(np.float32)[..., None]
del yy, xx, r_n
GRAIN = [np.random.default_rng(7).normal(0, 7, (H, W, 1)).astype(np.float32) for _ in range(8)]

def grade(a, inten):
    if inten == 0:
        a[..., 0] *= 0.96; a[..., 1] *= 1.0; a[..., 2] = np.clip(a[..., 2] * 1.10 + 4, 0, 255)
        a[:] = 0.5 * a + 0.5 * np.clip(a - 18, 0, 255)  # gentle fade-crush
    elif inten == 1:
        a[..., 0] = np.clip(a[..., 0] * 1.06 + 4, 0, 255); a[..., 2] *= 0.96
    elif inten == 2:
        a[..., 0] = np.clip(a[..., 0] * 1.12 + 6, 0, 255); a[..., 1] *= 1.02; a[..., 2] *= 0.94
    else:
        a[..., 0] = np.clip(a[..., 0] * 1.18 + 10, 0, 255); a[..., 1] *= 1.02; a[..., 2] *= 0.88
    return a

def shake(t, inten):
    if inten == 0: return 0.0, 0.0
    near = HITS[np.abs(HITS - t) < 0.6]
    if len(near) == 0: return 0.0, 0.0
    dt = t - near.min()
    if dt < 0: return 0.0, 0.0
    env = float(np.exp(-dt * 10.0))
    A = {1: 4.0, 2: 7.0, 3: 10.0}[inten]
    rs = np.random.default_rng(int(near.min() * 1000))
    return rs.uniform(-1, 1) * A * env, rs.uniform(-1, 1) * A * env

def cap_pulse(t, style):
    i = int(np.searchsorted(GRID, t)) - 1
    if i < 0: return 1.0
    dt = t - GRID[min(i, len(GRID) - 1)]
    amp = 0.045 if style in ('drop', 'bridge') else 0.02
    return 1.0 + amp * float(np.exp(-dt * 10.0))

cf = get_font(34)
ct = 'CRYBABY BEARD BOY  ·  DYING OF DEATH PT. II'
CREDIT = Image.new('RGBA', (int(cf.getlength(ct)) + 40, 60), (0, 0, 0, 0))
ImageDraw.Draw(CREDIT).text((20, 8), ct, font=cf, fill=(255, 255, 255, 255))

# ================================================================ render
FF = imageio_ffmpeg.get_ffmpeg_exe()
out_v = f'{WORK}/video_silent.mp4'
enc = subprocess.Popen([FF, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                        '-r', str(FPS), '-i', '-', '-pix_fmt', 'yuv420p', '-c:v', 'libx264',
                        '-preset', 'medium', '-crf', '20', '-movflags', '+faststart', out_v],
                       stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def render_frame(f):
    t = f / FPS
    clip = clips[-1]
    for c in clips:
        if c['t0'] <= t < c['t1']: clip = c; break
    p = np.clip((t - clip['t0']) / (clip['t1'] - clip['t0']), 0, 1)
    z0, z1, px, py = clip['cam']
    z = z0 + (z1 - z0) * p
    sx, sy = shake(t, clip['inten'])
    cx = BUFW / 2 + px * (p - 0.5) + sx
    cy = BUFH / 2 + py * (p - 0.5) + sy
    ww, wh = W / z, H / z
    l = int(np.clip(cx - ww / 2, 0, BUFW - ww)); tp = int(np.clip(cy - wh / 2, 0, BUFH - wh))
    buf = SCENE_FN[clip['scene']](t + clip['seed'] % 13 * 0.37, clip['seed'])
    img = Image.fromarray(buf).crop((l, tp, l + int(ww), tp + int(wh))).resize((W, H), Image.BILINEAR)
    a = np.asarray(img, dtype=np.float32)
    a = grade(a, clip['inten'])
    # section boundary flash + glitch
    if f in SEC_STARTS:
        a = np.clip(a * 1.5 + 90, 0, 255)
    elif f - 1 in SEC_STARTS:
        a = np.clip(a * 1.18 + 30, 0, 255)
    a *= VIGNETTE
    a += GRAIN[(f // 2) % 8] * (0.08 if clip['inten'] == 0 else 0.13)
    if t > 101.8:
        a *= max(0.0, (103.06 - t) / 1.26)
    arr = np.clip(a, 0, 255).astype(np.uint8)
    frame = Image.fromarray(arr).convert('RGBA')
    for cap in CAP_SPRITES:
        if not (cap['t0'] <= t < cap['t1']): continue
        dtl = t - cap['t0']
        alpha = dtl / 0.22 if dtl < 0.22 else (max(0.0, (cap['t1'] - t) / 0.20) if t > cap['t1'] - 0.20 else 1.0)
        scale = cap_pulse(t, cap['style'])
        base_y = 0.50 * H if cap['style'] == 'drop' else (0.545 * H if cap['style'] == 'verse' else 0.52 * H)
        if cap['style'] == 'outro': base_y = 0.60 * H
        for (sp, sw, sh, li, xoff, ti) in cap['sprites']:
            dtw = t - cap['t0'] - 0.04 * ti
            if dtw <= 0: continue
            pop = min(1.0, dtw / 0.15)
            wsc = scale * (1 + 0.25 * (1 - pop) ** 2)
            nw, nh = max(1, int(sw * wsc)), max(1, int(sh * wsc))
            spi = Image.fromarray(sp).resize((nw, nh), Image.BILINEAR)
            if pop < 1 or alpha < 1:
                sa = np.asarray(spi).astype(np.float32); sa[..., 3] *= pop * alpha
                spi = Image.fromarray(sa.astype(np.uint8))
            lx = (W - cap['line_widths'][li] * scale) / 2 + xoff * scale
            ly = base_y - cap['total_h'] * scale / 2 + li * cap['line_h'] * scale
            frame.alpha_composite(spi, (int(lx - 20 * scale), int(ly)))
    if t < 4.5 or t > 97.5:
        ca = min(1.0, t / 1.2) if t < 4.5 else min(1.0, (103.0 - t) / 2.5)
        cs = np.asarray(CREDIT).astype(np.float32); cs[..., 3] *= ca * 0.7
        frame.alpha_composite(Image.fromarray(cs.astype(np.uint8)), ((W - CREDIT.width) // 2, int(H * 0.905)))
    return np.asarray(frame.convert('RGB')).copy()

print('rendering ...')
t0 = time.time()
for f in range(TOTAL_FRAMES):
    enc.stdin.write(render_frame(f).tobytes())
    if f % 200 == 0:
        el = time.time() - t0
        print(f'  {f}/{TOTAL_FRAMES}  {el:.0f}s  eta {el/max(f,1)*(TOTAL_FRAMES-f):.0f}s', flush=True)
enc.stdin.close(); enc.wait()
print(f'DONE {out_v} in {time.time()-t0:.0f}s')

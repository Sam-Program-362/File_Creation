#!/usr/bin/env python3
"""
Dying Of Death Pt. II - Instagram-style beat-synced edit renderer.
1080x1920 @30fps. Cuts snapped to audio onsets, Ken Burns motion + beat shake,
section color grades, vignette, film grain, bold Anton captions (word pop-in,
keyword accents, beat pulse), glitch/flash transitions. Audio muxed after.
"""
import numpy as np, json, glob, os, time
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, imageio_ffmpeg

W, H, FPS = 1080, 1920, 30
WORK = 'work'
meta = json.load(open(f'{WORK}/meta.json'))
DURATION = meta['duration']
TOTAL_FRAMES = int(os.environ.get('TEST_FRAMES', 0)) or int(DURATION * FPS)

beats = np.load(f'{WORK}/beats.npy')
onset = np.load(f'{WORK}/onset.npy')
onset_times = np.load(f'{WORK}/onset_times.npy')

# ---------------------------------------------------------------- sections
SECTIONS = [
    ('intro',  0.0,  0),
    ('build1', 24.2, 1),
    ('drop1',  44.0, 2),
    ('bridge', 71.9, 0),
    ('build2', 79.7, 1),
    ('drop2',  87.6, 3),
    ('outro',  96.4, 0),
]
SEC_END = {'intro':24.2,'build1':44.0,'drop1':71.9,'bridge':79.7,'build2':87.6,'drop2':96.4,'outro':103.0}

def snap(t):
    i0, i1 = np.searchsorted(onset_times, [t-0.15, t+0.15])
    if i1 > i0:
        return float(onset_times[i0 + int(np.argmax(onset[i0:i1]))])
    return float(t)

def section_cuts(start, end, pattern):
    b = beats[(beats >= start) & (beats < end)]
    cuts, i, k = [], 0, 0
    while i < len(b):
        c = snap(b[i])
        if not cuts or c - cuts[-1] > 0.5:
            cuts.append(c)
        i += pattern[k % len(pattern)]
        k += 1
    if not cuts or cuts[0] > start + 0.3:
        cuts.insert(0, snap(start) if start > 0 else 0.0)
    return cuts

PATTERNS = {
    'intro':  [8],
    'build1': [4],
    'drop1':  [4,4,2,2,4,4,2,2,4,4,2,2],
    'bridge': [4],
    'build2': [4,4,2,2],
    'drop2':  [2],
    'outro':  [8],
}

# ---------------------------------------------------------------- shots
SHOT_POOL = {
    'intro':  [18, 19, 12, 20, 27],
    'build1': [1, 10, 6, 28, 29, 21, 11, 30, 24],
    'drop1':  [16, 17, 1, 12, 3, 10, 4, 11, 26, 24, 6, 30],
    'bridge': [25, 31, 23],
    'build2': [3, 6, 27, 4, 26],
    'drop2':  [17, 16, 1, 12, 4, 3, 10, 24],
    'outro':  [22, 24],
}
MOTIONS = [
    (1.03, 1.13,  60, -40), (1.14, 1.04, -70,  50), (1.02, 1.15, -50, -60),
    (1.16, 1.03,  70,  40), (1.05, 1.20,  40,  60), (1.18, 1.05, -60, -30),
    (1.04, 1.12,  80,   0), (1.12, 1.02,   0, -70), (1.06, 1.18, -40,  50),
]

files = sorted(glob.glob('assets/shots/*.jpg'))
BUFW, BUFH = 1350, 2400
print('preprocessing shot buffers ...')
BUFFERS = {}
for i, p in enumerate(files):
    im = Image.open(p).convert('RGB')
    s = max(BUFW / im.width, BUFH / im.height)
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    l, t = (im.width - BUFW) // 2, (im.height - BUFH) // 2
    BUFFERS[i] = np.asarray(im.crop((l, t, l + BUFW, t + BUFH)), dtype=np.uint8)
print(f'  {len(BUFFERS)} buffers ready')

clips = []
for name, start, inten in SECTIONS:
    cuts = section_cuts(start, SEC_END[name], PATTERNS[name])
    cuts.append(SEC_END[name])
    pool = SHOT_POOL[name]
    for j in range(len(cuts) - 1):
        img = pool[j % len(pool)]
        z0, z1, px, py = MOTIONS[(j + len(name)) % len(MOTIONS)]
        if inten == 0:
            z0, z1 = z0 * 0.9 + 0.02, z1 * 0.9 + 0.02
        if inten == 3:
            z0, z1 = z0 + 0.04, z1 + 0.10
        clips.append(dict(start=cuts[j], end=cuts[j+1], img=img,
                          z0=z0, z1=z1, px=px, py=py, sec=name, inten=inten))
print(f'timeline: {len(clips)} clips')
for c in clips: print(f"   {c['sec']:6s} {c['start']:6.2f} -> {c['end']:6.2f}  img{c['img']:3d} z {c['z0']:.2f}-{c['z1']:.2f}")

# ---------------------------------------------------------------- captions
WHITE=(255,255,255); RED=(255,64,44); AMBER=(255,178,64)
PHRASE_MAP = {'beautiful sky': AMBER, 'safe here': AMBER, "death's fear": RED}
SOLO_RED = {'liar','explosions','fire',"death's",'fear'}

CAPTIONS = [
 (3.5,  11.6, "It's a beautiful sky, I agree, but I'm a liar", 86, 'verse'),
 (11.6, 19.9, "'Cause all that I see is explosions and fire", 86, 'verse'),
 (19.9, 28.2, "Not a real person, just a vessel for death's fear", 86, 'verse'),
 (28.2, 36.4, "Unsure of its purpose, but I know that it's safe here", 86, 'verse'),
 (36.4, 44.0, "IT'S A BEAUTIFUL SKY, I AGREE, BUT I'M A LIAR", 78, 'drop'),
 (44.0, 52.0, "ALL THAT I SEE IS EXPLOSIONS AND FIRE", 94, 'drop'),
 (52.0, 60.0, "NOT A REAL PERSON, JUST A VESSEL FOR DEATH'S FEAR", 84, 'drop'),
 (60.0, 67.8, "UNSURE OF ITS PURPOSE, BUT I KNOW THAT IT'S SAFE HERE", 78, 'drop'),
 (67.8, 71.9, "WHAT A BEAUTIFUL SKY", 108, 'drop'),
 (72.3, 75.6, "BEAUTIFUL SKY", 130, 'bridge'),
 (75.6, 79.5, "BEAUTIFUL SKY", 130, 'bridge'),
 (80.5, 84.0, "NOT A REAL PERSON", 92, 'drop'),
 (84.0, 87.6, "JUST A VESSEL FOR DEATH'S FEAR", 82, 'drop'),
 (87.6, 92.0, "WHAT A BEAUTIFUL SKY", 112, 'drop'),
 (92.0, 96.4, "I AGREE, BUT I'M A LIAR", 94, 'drop'),
 (97.6, 102.3, "unsure of its purpose,\nbut I know that it's safe here", 54, 'outro'),
]

font_cache = {}
def get_font(size):
    if size not in font_cache:
        font_cache[size] = ImageFont.truetype('assets/Anton-Regular.ttf', size)
    return font_cache[size]

def paint_colors(text):
    toks = text.replace('\n', ' \n ').split(' ')
    low = [t.lower().strip(',.?!') for t in toks]
    colors = [None] * len(toks)
    for i, t in enumerate(toks):
        if t == '\n':
            continue
        if i + 1 < len(low) and low[i] + ' ' + low[i+1] in PHRASE_MAP:
            c = PHRASE_MAP[low[i] + ' ' + low[i+1]]
            colors[i] = c; colors[i+1] = c
        elif low[i] in SOLO_RED:
            colors[i] = RED
    return colors, toks

print('pre-rendering caption sprites ...')
MAXW = 950
CAP_SPRITES = []
for (t0, t1, text, size, style) in CAPTIONS:
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
        cur.append((tok, wl, idx))
        curw += wl + (spacew if len(cur) > 1 else 0)
        idx += 1
    if cur: lines.append(cur)
    line_h = int(size * 1.20)
    total_h = line_h * len(lines)
    line_widths = [sum(w for _, w, _ in ln) + spacew * (len(ln)-1) for ln in lines]
    sprites = []
    sw = int(size * 0.10) + 6
    for li, ln in enumerate(lines):
        x = 0.0
        for (tok, wl, ti) in ln:
            col = colors[ti] or WHITE
            sp = Image.new('RGBA', (int(wl) + sw*2 + 40, line_h + sw*2 + 12), (0,0,0,0))
            d = ImageDraw.Draw(sp)
            d.text((sw+20+5, sw+9), tok, font=font, fill=(0,0,0,200),
                   stroke_width=sw, stroke_fill=(0,0,0,200))
            sp = sp.filter(ImageFilter.GaussianBlur(5))
            d = ImageDraw.Draw(sp)
            d.text((sw+20, sw+4), tok, font=font, fill=col+(255,),
                   stroke_width=sw, stroke_fill=(0,0,0,255))
            sprites.append((np.asarray(sp).copy(), sp.width, sp.height, li, x, ti))
            x += wl + spacew
    CAP_SPRITES.append(dict(t0=t0, t1=t1, sprites=sprites, line_h=line_h,
                            total_h=total_h, line_widths=line_widths, style=style))
print(f'  {len(CAP_SPRITES)} captions ready')

# ---------------------------------------------------------------- fx assets
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx - W/2) / (W/2))**2 + ((yy - H/2) / (H/2))**2)
VIGNETTE = (0.62 + 0.38 * np.clip(1.18 - r * 0.85, 0, 1)).astype(np.float32)[..., None]
del yy, xx, r

rng = np.random.default_rng(7)
GRAIN = [rng.normal(0, 8, (H, W, 1)).astype(np.float32) for _ in range(10)]
print('grain bank ready')

def grade_lut(inten):
    x = np.arange(256).astype(np.float32)
    if inten == 0:
        r = x*0.94 + 14; g = x*0.97 + 12; b = x*1.05 + 16
    elif inten == 1:
        r = (x-128)*1.10 + 132; g = (x-128)*1.04 + 126; b = (x-128)*0.94 + 118
    elif inten == 2:
        r = (x-128)*1.18 + 134; g = (x-128)*1.10 + 124; b = (x-128)*0.92 + 112
    else:
        r = (x-128)*1.24 + 138; g = (x-128)*1.14 + 124; b = (x-128)*0.90 + 108
    return np.clip(r,0,255).astype(np.uint8), np.clip(g,0,255).astype(np.uint8), np.clip(b,0,255).astype(np.uint8)
LUTS = {i: grade_lut(i) for i in range(4)}

SEC_BOUNDS = {round(s * FPS) for _, s, _ in SECTIONS if s > 0}

def shake_at(t, inten):
    if inten == 0: return 0.0, 0.0
    bi = int(np.searchsorted(beats, t)) - 1
    if bi < 0: return 0.0, 0.0
    dt = t - beats[bi]
    env = np.exp(-dt * 7.0)
    A = {1: 5.0, 2: 9.0, 3: 13.0}[inten]
    rs = np.random.default_rng(bi * 977 + inten)
    return float(rs.uniform(-1,1) * A * env), float(rs.uniform(-1,1) * A * env)

def cap_pulse(t, style):
    bi = int(np.searchsorted(beats, t)) - 1
    if bi < 0: return 1.0
    dt = t - beats[min(bi, len(beats)-1)]
    amp = 0.05 if style in ('drop','bridge') else 0.022
    return 1.0 + amp * float(np.exp(-dt * 9.0))

# credit sprite
cf = get_font(34)
ct = 'CRYBABY BEARD BOY  ·  DYING OF DEATH PT. II'
cw = int(cf.getlength(ct)) + 40
CREDIT_SPR = Image.new('RGBA', (cw, 60), (0,0,0,0))
ImageDraw.Draw(CREDIT_SPR).text((20, 8), ct, font=cf, fill=(255,255,255,255))

# ---------------------------------------------------------------- render
FF = imageio_ffmpeg.get_ffmpeg_exe()
out_v = f'{WORK}/video_silent.mp4'
enc = subprocess.Popen(
    [FF, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
     '-i', '-', '-pix_fmt', 'yuv420p', '-c:v', 'libx264', '-preset', 'medium',
     '-crf', '20', '-movflags', '+faststart', out_v],
    stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def render_frame(f):
    t = f / FPS
    clip = clips[-1]
    for c in clips:
        if c['start'] <= t < c['end']:
            clip = c; break
    p = np.clip((t - clip['start']) / (clip['end'] - clip['start']), 0, 1)
    inten = clip['inten']

    buf = BUFFERS[clip['img']]
    z = clip['z0'] + (clip['z1'] - clip['z0']) * p
    win_w, win_h = W / z, H / z
    sx, sy = shake_at(t, inten)
    cx_b = BUFW/2 + clip['px'] * (p - 0.5) + sx
    cy_b = BUFH/2 + clip['py'] * (p - 0.5) + sy
    l = int(np.clip(cx_b - win_w/2, 0, BUFW - win_w))
    tp = int(np.clip(cy_b - win_h/2, 0, BUFH - win_h))
    img = Image.fromarray(buf).crop((l, tp, l + int(win_w), tp + int(win_h))).resize((W, H), Image.BILINEAR)
    arr = np.asarray(img, dtype=np.uint8)

    lr, lg, lb = LUTS[inten]
    arr = np.stack([lr[arr[...,0]], lg[arr[...,1]], lb[arr[...,2]]], axis=-1)

    if f in SEC_BOUNDS:
        arr = np.clip(arr.astype(np.int16) + 110, 0, 255).astype(np.uint8)
    elif f - 1 in SEC_BOUNDS:
        arr = np.clip(arr.astype(np.int16) + 45, 0, 255).astype(np.uint8)
    if f in SEC_BOUNDS or f - 1 in SEC_BOUNDS:
        g = arr.copy()
        g[..., 0] = np.roll(arr[..., 0], 10, axis=1)
        g[..., 2] = np.roll(arr[..., 2], -10, axis=1)
        arr = g

    a = arr.astype(np.float32)
    a *= VIGNETTE
    a += GRAIN[(f // 2) % 10] * (0.10 if inten == 0 else 0.16)

    # fade to black at the very end
    if t > 101.6:
        a *= max(0.0, (103.0 - t) / 1.4)

    arr = np.clip(a, 0, 255).astype(np.uint8)

    need_composite = (t < 5.0 or t > 97.0) or any(c['t0'] <= t < c['t1'] for c in CAP_SPRITES)
    if need_composite:
        frame = Image.fromarray(arr).convert('RGBA')
        for cap in CAP_SPRITES:
            if not (cap['t0'] <= t < cap['t1']):
                continue
            dtl = t - cap['t0']
            if dtl < 0.25: alpha = dtl / 0.25
            elif t > cap['t1'] - 0.22: alpha = max(0.0, (cap['t1'] - t) / 0.22)
            else: alpha = 1.0
            scale = cap_pulse(t, cap['style'])
            base_y = 0.52 * H if cap['style'] == 'drop' else (0.56 * H if cap['style'] == 'verse' else 0.54 * H)
            if cap['style'] == 'outro': base_y = 0.60 * H
            for (sp, sw, sh, li, xoff, ti) in cap['sprites']:
                dtw = t - cap['t0'] - 0.045 * ti
                if dtw <= 0: continue
                pop = min(1.0, dtw / 0.16)
                wsc = scale * (1.0 + 0.28 * (1 - pop) ** 2)
                nw, nh = max(1, int(sw * wsc)), max(1, int(sh * wsc))
                spi = Image.fromarray(sp).resize((nw, nh), Image.BILINEAR)
                if pop < 1 or alpha < 1:
                    sa = np.asarray(spi).astype(np.float32)
                    sa[..., 3] *= pop * alpha
                    spi = Image.fromarray(sa.astype(np.uint8))
                lx = (W - cap['line_widths'][li] * scale) / 2 + xoff * scale
                ly = base_y - (cap['total_h'] * scale) / 2 + li * cap['line_h'] * scale
                frame.alpha_composite(spi, (int(lx - 20*scale), int(ly)))
        if t < 5.0 or t > 97.0:
            ca = min(1.0, t / 1.2) if t < 5 else min(1.0, (103.0 - t) / 2.5)
            cs = np.asarray(CREDIT_SPR).astype(np.float32)
            cs[..., 3] *= ca * 0.75
            frame.alpha_composite(Image.fromarray(cs.astype(np.uint8)), ((W - CREDIT_SPR.width)//2, int(H*0.90)))
        arr = np.asarray(frame.convert('RGB'), dtype=np.uint8)

    return arr

print('rendering frames ...')
t_start = time.time()
for f in range(TOTAL_FRAMES):
    enc.stdin.write(render_frame(f).tobytes())
    if f % 200 == 0:
        el = time.time() - t_start
        eta = el / max(f, 1) * (TOTAL_FRAMES - f)
        print(f'  frame {f}/{TOTAL_FRAMES}  elapsed {el:.0f}s  eta {eta:.0f}s', flush=True)
enc.stdin.close(); enc.wait()
print(f'DONE: {out_v}  ({time.time()-t_start:.0f}s total)')

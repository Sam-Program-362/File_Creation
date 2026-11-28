#!/usr/bin/env python3
"""Analysis v2: tempo-grid phase, vocal phrases, hit events -> plan.json + plot."""
import librosa, numpy as np, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

y, sr = librosa.load('assets/song.mp3', sr=22050, mono=True)
dur = len(y) / sr

# tempo + global phase-locked grid
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units='time')
tempo = float(np.atleast_1d(tempo)[0])
beat_period = 60.0 / tempo
onset = librosa.onset.onset_strength(y=y, sr=sr)
ot = librosa.times_like(onset, sr=sr)

# refine grid phase: test offsets, maximize mean onset energy at grid points
best_phase, best_score = 0.0, -1
t0, t1 = 0.0, dur
for phase in np.arange(0, beat_period, 0.01):
    grid = np.arange(phase, t1, beat_period)
    idx = np.clip((grid * sr / 512).astype(int), 0, len(onset) - 1)
    score = float(np.mean(onset[idx]))
    if score > best_score:
        best_score, best_phase = score, phase
grid = np.arange(best_phase, dur, beat_period)
print(f"tempo {tempo:.2f} BPM  period {beat_period:.4f}s  phase {best_phase:.3f}s  grid pts {len(grid)}")

# vocal phrase detection: HPSS -> harmonic -> vocal band energy
H, P = librosa.effects.hpss(y, margin=(2.0, 2.0))
S = np.abs(librosa.stft(H, n_fft=2048, hop_length=512))
freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
band = (freqs > 180) & (freqs < 3500)
vocal_energy = np.mean(S[band], axis=0)
# smooth
kernel = np.ones(26) / 26.0  # ~0.6s
ve = np.convolve(vocal_energy, kernel, mode='same')
ve_max = ve.max()
thr = 0.30 * ve_max
active = ve > thr
# segments
segments = []
in_seg = False
for i, a in enumerate(active):
    if a and not in_seg:
        start_i, in_seg = i, True
    elif not a and in_seg:
        in_seg = False
        if (i - start_i) / sr > 0.7:
            segments.append((start_i / sr, i / sr))
if in_seg:
    segments.append((start_i / sr, len(active) / sr))
# merge segments separated by < 0.45s
merged = []
for s in segments:
    if merged and s[0] - merged[-1][1] < 0.45:
        merged[-1] = (merged[-1][0], s[1])
    else:
        merged.append(list(map(float, s)))
print(f"vocal phrases ({len(merged)}):")
for s in merged:
    print(f"  {s[0]:6.2f} -> {s[1]:6.2f}  ({s[1]-s[0]:.2f}s)")

# big hit events (top onsets, min separation)
peaks = librosa.util.peak_pick(onset, pre_max=6, post_max=6, pre_avg=12, post_avg=12, delta=onset.max()*0.35, wait=14)
hits = [float(ot[i]) for i in peaks]
print(f"hit events ({len(hits)}): {['%.2f' % h for h in hits[:30]]}")

# rms energy curve for sections
rms = librosa.feature.rms(y=y, hop_length=512)[0]
t_rms = librosa.times_like(rms, sr=sr, hop_length=512)

json.dump({'tempo': tempo, 'beat_period': beat_period, 'phase': best_phase,
           'grid': grid.tolist(), 'phrases': merged, 'hits': hits, 'duration': dur},
          open('work/plan.json', 'w'))

# plot for visual review
fig, ax = plt.subplots(3, 1, figsize=(20, 12), sharex=True)
ax[0].plot(t_rms, rms, lw=0.8, color='gray'); ax[0].set_ylabel('rms')
ax[1].plot(ot, onset, lw=0.8, color='teal'); ax[1].set_ylabel('onset')
for h in hits: ax[1].axvline(h, color='red', alpha=0.5, lw=0.7)
ax[2].plot(ot, ve / ve_max, lw=1.0, color='purple'); ax[2].axhline(thr/ve_max, color='orange', lw=0.8); ax[2].set_ylabel('vocal')
for i, s in enumerate(merged):
    for a in ax: a.axvline(s[0], color='blue', alpha=0.45, lw=0.9)
    ax[2].text(s[0] + 0.1, 1.02, f'{i}', color='blue', fontsize=11)
for a in ax:
    for g in grid[::4]: a.axvline(g, color='green', alpha=0.10, lw=0.5)
plt.tight_layout(); plt.savefig('work/analysis2.png', dpi=85); print('plot saved')

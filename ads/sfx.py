"""Efectos de sonido y base rítmica generados por código (sin derechos de terceros)."""
import numpy as np, wave, os
SR = 44100
D = os.path.dirname(os.path.abspath(__file__)) + "/sfx"
rng = np.random.default_rng(7)

def save(name, x):
    x = np.clip(x, -1, 1); os.makedirs(D, exist_ok=True)
    with wave.open(f"{D}/{name}.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes())

def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR; e = np.minimum(1, t / a) * np.exp(-t / r); return e

def whoosh(d=0.45):
    n = int(d * SR); noise = rng.standard_normal(n)
    # ruido filtrado con barrido de frecuencia (paso banda simple)
    out = np.zeros(n); y1 = y2 = 0
    for i in range(n):
        f = 300 + 5000 * (i / n) ** 1.5; w0 = 2 * np.pi * f / SR; alpha = np.sin(w0) / 3
        b0, a1, a2 = alpha, -2 * np.cos(w0), 1 - alpha
        y = (b0 * noise[i] - a1 * y1 - a2 * y2) / (1 + alpha); y2, y1 = y1, y; out[i] = y
    e = np.sin(np.pi * np.arange(n) / n) ** 2
    return out / np.abs(out).max() * e * 0.6

def pop():
    n = int(0.12 * SR); t = np.arange(n) / SR
    f = 900 * np.exp(-t * 30) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.03) * 0.8

def click():
    n = int(0.05 * SR); return rng.standard_normal(n) * env(n, 0.0005, 0.006) * 0.5

def boom():
    n = int(0.7 * SR); t = np.arange(n) / SR
    f = 60 + 90 * np.exp(-t * 18)
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.25) + rng.standard_normal(n) * env(n, 0.001, 0.02) * 0.3) * 0.9

def ding():
    n = int(0.9 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1318 * t) + 0.5 * np.sin(2 * np.pi * 1976 * t)) * env(n, 0.002, 0.3) * 0.35

def beat(secs, bpm=118):
    """Base rítmica: bombo, palmas en 2 y 4, charles en corcheas y bajo simple."""
    n = int(secs * SR); x = np.zeros(n); spb = 60 / bpm
    kick = lambda: (lambda m: np.sin(2 * np.pi * np.cumsum(50 + 120 * np.exp(-np.arange(m) / SR * 35)) / SR) * env(m, 0.001, 0.16))(int(0.35 * SR))
    clap = lambda: (lambda m: rng.standard_normal(m) * env(m, 0.001, 0.05) * 0.45)(int(0.2 * SR))
    hat = lambda: (lambda m: np.diff(rng.standard_normal(m + 1)) * env(m, 0.0005, 0.02) * 0.12)(int(0.06 * SR))
    notes = [55, 55, 65.4, 49]  # La, La, Do, Sol (bajo)
    def add(s, t):
        i = int(t * SR); j = min(n, i + len(s)); x[i:j] += s[:j - i]
    b = 0; t = 0.0
    while t < secs:
        add(kick(), t)
        if b % 2 == 1: add(clap(), t)
        add(hat(), t); add(hat(), t + spb / 2)
        m = int(spb * 0.9 * SR); tt = np.arange(m) / SR
        add(np.sin(2 * np.pi * notes[(b // 4) % 4] * tt) * env(m, 0.01, 0.25) * 0.35, t)
        b += 1; t += spb
    return x / max(1e-6, np.abs(x).max()) * 0.7

if __name__ == "__main__":
    save("whoosh", whoosh()); save("pop", pop()); save("click", click()); save("boom", boom()); save("ding", ding())
    save("beat", beat(20)); print("ok")

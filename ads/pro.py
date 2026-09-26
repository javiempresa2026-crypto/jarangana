"""Edición "de creador": cortes al ritmo (118 bpm), zoom de impacto en cada corte, texto que entra con rebote,
efectos de sonido (whoosh, pop, boom, ding), color retocado y tarjeta final con precio. Audio real del clip + base propia.
Uso: python3 ads/pro.py [nombre]   (sin nombre: todos). Salida: ads/out/pro/*.mp4 + portadas en ads/out/pro/portadas/"""
import os, sys, subprocess, wave, math
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
import render as R
from render import FF, SUN, INK, rounded
from ugc import fill_frame, video_frames
from viral import native_text, clip_audio

D = R.D; W, H, FPS, SR = 1080, 1920, 30, 44100
SPB = 60 / 118                       # un pulso de la base
OUT = f"{D}/out/pro"; COV = f"{OUT}/portadas"
BRAND = {"naranja": ((224, 80, 15), (185, 58, 10)), "turquesa": ((11, 138, 138), (14, 110, 122)), "rosa": ((230, 46, 115), (181, 23, 79))}

# plano: (fuente, pulsos, texto, efecto, inicio_clip_s, marcas)   marcas: flash = destello blanco, boom = golpe grave
# fin: (color, foto, nombre, precio, extra)
VIDEOS = {
 "grifo-1080": dict(shots=[
   ("kling/grifo.mp4", 4, "tu grifo puede hacer ESTO 👀", "none", 0, ""),
   ("ugc_clips/grifo.mp4", 4, "gira 1080°", "none", 0, "flash"),
   ("kling/grifo.mp4", 4, "chorro suave… o a presión 💦", "none", 2.4, ""),
   ("grifo1", 2, "se enrosca en 1 minuto", "punch", 0, "boom"),
   ("grifo3", 2, "sin fontanero 🔧", "punch", 0, ""),
  ], fin=("turquesa", "kling/grifo4.jpg", "Grifo 1080°", "12,90 €", "2 por 19,90 €"),
  portada=("grifo4", "Tu grifo puede hacer [ESTO] 👀")),
 "luz-sensor": dict(shots=[
   ("luz4", 3, "POV: 7 de la mañana, sin despertar a nadie 🤫", "shake", 0, ""),
   ("kling/luz.mp4", 5, "abres… y se enciende sola 💡", "none", 0, "flash"),
   ("ugc_clips/luz.mp4", 4, "armario, pasillo, cocina…", "none", 0, ""),
   ("luz3", 2, "imán + adhesivo", "punch", 0, "boom"),
   ("luz5", 2, "cero agujeros 🙌", "punch", 0, ""),
  ], fin=("naranja", "kling/luz2.jpg", "Luz LED con sensor", "24,90 €", "2 por 44,90 €"),
  portada=("luz2", "Se acabó buscar [a oscuras] 🔦")),
 "mampara-10s": dict(shots=[
   ("kling/rasqueta.mp4", 3, "el truco de 10 segundos ✨", "none", 0, ""),
   ("kling/rasqueta.mp4", 5, "quitas el agua antes de que se seque", "none", 1.5, ""),
   ("ugc_clips/rasqueta.mp4", 4, "silicona: no raya el cristal", "none", 0, "flash"),
   ("ras3", 4, "y se queda colgada en la mampara", "punch", 0, "boom"),
  ], fin=("rosa", "ras3", "Rasqueta con soporte", "15,90 €", "para cada día"),
  portada=("ras5", "Mampara sin marcas en [10 segundos] ✨")),
 "ducha-sin-agujeros": dict(shots=[
   ("bal5", 3, "mi casero: «ni un agujero» 🙅", "shake", 0, ""),
   ("ugc_clips/balda.mp4", 3, "yo:", "none", 0, "flash"),
   ("bal4", 2, "balda que se cuelga del grifo", "punch", 0, "boom"),
   ("gan1", 2, "+ ganchos adhesivos", "punch", 0, ""),
   ("ras3", 2, "+ rasqueta con soporte", "punch", 0, ""),
   ("bal1", 4, "ducha ordenada en 5 minutos ✨", "zoom", 0, ""),
  ], fin=("naranja", "kling/bal2.jpg", "Kit Ducha sin taladro", "49,90 €", "envío GRATIS"),
  portada=("bal5", "Ducha ordenada [sin taladrar] 🚿")),
 "top3-menos-25": dict(shots=[
   ("kling/luz.mp4", 4, "3 cosas de menos de 25 € para tu piso de alquiler 👇", "none", 0, ""),
   ("kling/grifo.mp4", 4, "1 · grifo que gira 1080°\n12,90 €", "none", 1.0, "flash"),
   ("kling/rasqueta.mp4", 4, "2 · rasqueta para la mampara\n15,90 €", "none", 0.5, "flash"),
   ("kling/luz.mp4", 4, "3 · luz que se enciende sola\n24,90 €", "none", 1.5, "flash"),
   ("ras3", 2, "¿con cuál te quedas? 1, 2 o 3 👇", "punch", 0, "boom"),
  ], fin=("turquesa", "kling/grifo4.jpg", "Todo sin taladrar", "desde 12,90 €", "envío GRATIS +35 €"),
  portada=("grifo4", "3 cosas de [menos de 25 €] 👇")),
}

# ---------- imagen ----------
_yy, _xx = np.mgrid[0:H, 0:W]
VIG = (1 - 0.32 * (((_xx - W / 2) / (W / 2)) ** 2 + ((_yy - H / 2) / (H / 2)) ** 2) / 2).clip(0.6, 1)[..., None].astype(np.float32)
del _yy, _xx

def grade(im):
    """Contraste y color un punto por encima + viñeta suave (el "look" de creador)."""
    im = ImageEnhance.Color(im).enhance(1.14)
    a = np.asarray(im, dtype=np.float32)
    a = (a - 128) * 1.07 + 132
    return Image.fromarray((a * VIG).clip(0, 255).astype(np.uint8))

def ease_back(t):  # entrada con rebote
    t = max(0.0, min(1.0, t)); c = 1.9
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

def punch(im, k):
    """Zoom de impacto al entrar un plano: 112 % → 100 % en 6 fotogramas."""
    z = 1 + 0.12 * (1 - min(1, k / 6)) ** 2
    if z <= 1.001: return im
    cw, ch = W / z, H / z
    return im.crop((int((W - cw) / 2), int((H - ch) / 2), int((W + cw) / 2), int((H + ch) / 2))).resize((W, H), Image.BILINEAR)

def text_layer(text, y=300):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); native_text(lay, text, y=y)
    bb = lay.getbbox(); return lay.crop(bb), bb

def paste_pop(c, layer, bb, k):
    s = ease_back(k / 7) if k < 7 else 1.0
    if s <= 0.02: return
    lw, lh = layer.size; nw, nh = max(1, int(lw * s)), max(1, int(lh * s))
    l = layer.resize((nw, nh), Image.BILINEAR) if (nw, nh) != (lw, lh) else layer
    cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
    c.alpha_composite(l, (int(cx - nw / 2), int(cy - nh / 2)))

def load(src):
    if src.endswith(".mp4"): return video_frames(f"{D}/{src}")
    if "." in src: return Image.open(f"{D}/{src}").convert("RGB")
    p = next(f"{D}/img/{src}.{e}" for e in ("webp", "png") if os.path.exists(f"{D}/img/{src}.{e}"))
    return Image.open(p).convert("RGB")

def gradient(col):
    a, b = BRAND[col]
    t = np.linspace(0, 1, H)[:, None, None]
    g = (np.array(a) * (1 - t) + np.array(b) * t) * np.ones((1, W, 1))
    im = Image.fromarray(g.astype(np.uint8)).convert("RGBA")
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for yy in range(0, H, 90):
        for xx in range(0, W, 90):
            if (xx // 90 + yy // 90) % 2 == 0: d.rounded_rectangle((xx + 6, yy + 6, xx + 84, yy + 84), 16, fill=(255, 255, 255, 16))
    im.alpha_composite(lay); return im

def end_card(fin, k, n):
    """Tarjeta final animada: foto que entra, nombre, precio que late y llamada a la acción."""
    col, foto, name, price, extra = fin
    c = gradient(col).copy(); t = k / FPS
    logo = R.LOGO.resize((300, int(300 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
    c.alpha_composite(logo, (W // 2 - 150, 150))
    im = load(foto); s = min(im.size)
    im = im.crop(((im.width - s) // 2, (im.height - s) // 2, (im.width + s) // 2, (im.height + s) // 2))
    p = ease_back(k / 9); side = int(720 * max(0.05, p))
    ph = rounded(im.resize((side, side), Image.LANCZOS), 56)
    sh = Image.new("RGBA", (side + 30, side + 30), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((15, 25, side + 15, side + 25), 56, fill=(0, 0, 0, 70))
    c.alpha_composite(sh, (W // 2 - side // 2 - 15, 660 - side // 2 - 15)); c.alpha_composite(ph, (W // 2 - side // 2, 660 - side // 2))
    d = ImageDraw.Draw(c); f = FF(64)
    if k >= 5: d.text((W / 2 - f.getlength(name) / 2, 1060), name, font=f, fill=(255, 255, 255))
    if k >= 8:
        pulse = 1 + 0.05 * math.sin(t * 2 * math.pi / SPB) if k > 14 else ease_back((k - 8) / 6)
        R.pill(c, price, W / 2, 1165, 70, SUN, INK, scale=max(0.05, pulse))
    if k >= 12:
        f2 = FF(40, 600); d.text((W / 2 - f2.getlength(extra) / 2, 1320), extra, font=f2, fill=(255, 255, 255))
    if k >= 15:
        cta = "enlace en el perfil"; f3 = FF(46)
        bob = int(10 * math.sin(t * 2 * math.pi / SPB))
        tw = f3.getlength(cta) + 60; x0 = W / 2 - tw / 2
        d.rounded_rectangle((x0 - 40, 1420 + bob, x0 + tw + 40, 1520 + bob), 50, fill=(255, 255, 255))
        d.polygon([(x0 + 18, 1450 + bob), (x0 + 36, 1488 + bob), (x0, 1488 + bob)], fill=INK)  # flecha hacia arriba (perfil)
        d.text((x0 + 60, 1442 + bob), cta, font=f3, fill=INK)
        f4 = FF(34, 600); cod = "-10 % 1.er pedido: BIENVENIDA10"
        d.text((W / 2 - f4.getlength(cod) / 2, 1560), cod, font=f4, fill=(255, 255, 255))
    return c.convert("RGB")

# ---------- audio ----------
def wav_np(name):
    with wave.open(f"{D}/sfx/{name}.wav") as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32767

def mix(shots, total):
    n = int(total * SR); x = np.zeros(n, np.float32)
    beat = wav_np("beat"); beat = np.tile(beat, int(np.ceil(n / len(beat))))[:n]
    x += beat * 0.42
    def add(s, t, g):
        i = max(0, int(t * SR)); j = min(n, i + len(s))
        if j > i: x[i:j] += s[:j - i] * g
    wh, po, bo, di = wav_np("whoosh"), wav_np("pop"), wav_np("boom"), wav_np("ding")
    t = 0.0
    for src, beats, text, eff, st, marks in shots:
        dur = beats * SPB
        if src.endswith(".mp4"):
            a = np.frombuffer(clip_audio(f"{D}/{src}", st, dur), np.int16).astype(np.float32) / 32767
            add(a, t, 0.9)
        if t > 0: add(wh, t - 0.28, 0.55)
        add(po, t + 0.03, 0.5)
        if "boom" in marks: add(bo, t, 0.8)
        t += dur
    add(wh, t - 0.28, 0.55); add(bo, t, 0.7); add(di, t + 15 / FPS, 0.9)
    fade = int(0.3 * SR); x[-fade:] *= np.linspace(1, 0, fade)
    x = x / max(1.0, np.abs(x).max() / 0.95)
    return (x * 32767).astype(np.int16).tobytes()

# ---------- vídeo ----------
def render(key):
    v = VIDEOS[key]; shots = v["shots"]; end_beats = 6
    total = (sum(s[1] for s in shots) + end_beats) * SPB
    os.makedirs(OUT, exist_ok=True)
    wav = f"{OUT}/{key}.wav"
    with wave.open(wav, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(mix(shots, total))
    cache = {s[0]: load(s[0]) for s in shots}
    texts = [text_layer(s[2]) for s in shots]
    out = f"{OUT}/{key}.mp4"
    pr = subprocess.Popen([R.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-i", wav, "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    bounds = []; t = 0.0
    for s in shots: bounds.append((round(t * FPS), round((t + s[1] * SPB) * FPS))); t += s[1] * SPB
    end0 = bounds[-1][1]; nfr = int(total * FPS)
    for fi in range(nfr):
        if fi >= end0:
            k = fi - end0; fr = end_card(v["fin"], k, nfr - end0)
            fr = punch(fr, k)
            if k < 3: fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 255, 255)), 0.6 * (1 - k / 3))
            pr.stdin.write(fr.tobytes()); continue
        i = next(j for j, (a, b) in enumerate(bounds) if a <= fi < b)
        src, beats, text, eff, st, marks = shots[i]; k = fi - bounds[i][0]; dur = beats * SPB; tt = k / FPS
        if src.endswith(".mp4"):
            frs = cache[src]; idx = min(len(frs) - 1, int((st + tt) * FPS))
            c = fill_frame(frs[idx], tt / dur, "static", i)
        else:
            c = fill_frame(cache[src], tt / dur, "zoom" if eff in ("punch", "zoom") else eff, i)
        c = punch(grade(c), k)
        if "flash" in marks and k < 4: c = Image.blend(c, Image.new("RGB", (W, H), (255, 255, 255)), 0.75 * (1 - k / 4))
        c = c.convert("RGBA"); paste_pop(c, *texts[i], k)
        ImageDraw.Draw(c).text((44, 1700), "@jarandana", font=FF(32, 600), fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0))
        pr.stdin.write(c.convert("RGB").tobytes())
    pr.stdin.close(); pr.wait(); os.remove(wav); print("ok", out, round(total, 1), "s")

# ---------- portadas (1080x1920; el texto va en la zona central que también se ve en la cuadrícula 3:4) ----------
def cover(key):
    os.makedirs(COV, exist_ok=True)
    src, title = VIDEOS[key]["portada"]
    c = grade(fill_frame(load(src), 0.6, "zoom", 0)).convert("RGBA")
    a = np.zeros((H, W), np.float32); a[:] = np.linspace(0, 1, H)[:, None]
    shade = (np.clip(np.abs(a - 0.5) * -2 + 1, 0, 1) ** 1.5 * 150).astype(np.uint8)  # oscurece el centro para el título
    c.alpha_composite(Image.merge("RGBA", [Image.new("L", (W, H), 0)] * 3 + [Image.fromarray(shade)]))
    R.draw_text_block(c, title, 700, 104, (255, 255, 255), SUN, 10, maxw=900)
    lg = R.LOGO.resize((260, int(260 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
    c.alpha_composite(lg, (W // 2 - 130, 1180))
    c.convert("RGB").save(f"{COV}/{key}.jpg", quality=92); print("portada", key)

if __name__ == "__main__":
    for key in sys.argv[1:] or list(VIDEOS):
        cover(key); render(key)

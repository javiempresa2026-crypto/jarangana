"""Vídeos estilo nativo TikTok/Reels: pantalla completa, cortes rápidos, subtítulos palabra a palabra y voz en off.
Uso: python3 ads/ugc.py [nombre]"""
import os, sys, math, random, subprocess, wave
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import render as R
from organico import tts

D = R.D; W, H, FPS = 1080, 1920, 30
F = lambda s: ImageFont.truetype(f"{D}/fonts/P800.ttf", s)
EMO = R.EMO

# (fuente, voz en off, efecto) — la voz marca la duración de cada plano
VIDEOS = {
 "no-sabia-que-lo-necesitaba": [
   ("kling/grifo.mp4", "Cosas que no sabía que necesitaba en mi piso de alquiler.", "zoom"),
   ("kling/grifo.mp4", "Un grifo que gira hacia donde quieras y cambia a modo ducha.", "shake"),
   ("kling/luz.mp4", "Una luz que se enciende sola al abrir el armario.", "zoom"),
   ("kling/rasqueta.mp4", "Y esto. Diez segundos y la mampara sin marcas.", "shake"),
   ("ras3", "Todo sin taladrar. Lo tienes en el enlace del perfil.", "zoom"),
 ],
 "mampara-sin-marcas": [
   ("kling/rasqueta.mp4", "Si tu mampara siempre tiene marcas de agua, mira esto.", "zoom"),
   ("ras5", "El truco no es frotar más.", "shake"),
   ("kling/rasqueta.mp4", "Es quitar el agua justo después de ducharte. Diez segundos.", "slow"),
   ("ras3", "Y la rasqueta se queda colgada en la mampara, siempre a mano.", "zoom"),
   ("ras1", "Silicona, no raya. Enlace en el perfil.", "shake"),
 ],
 "casero-ni-un-agujero": [
   ("bal2", "Mi casero: ni un agujero en la pared.", "shake"),
   ("bal4", "Yo, con la ducha ordenada igualmente.", "zoom"),
   ("gan1", "Ganchos adhesivos para las toallas.", "shake"),
   ("esq3", "Estantería de esquina, dos alturas.", "zoom"),
   ("bal6", "Y cuando me mude, me lo llevo. Todo sin taladrar.", "shake"),
 ],
 "armario-a-oscuras": [
   ("kling/luz.mp4", "Deja de buscar la ropa con la linterna del móvil.", "zoom"),
   ("luz4", "Esta luz tiene sensor de movimiento.", "shake"),
   ("kling/luz.mp4", "Abres y se enciende sola.", "slow"),
   ("luz3", "Se pega con imán y adhesivo. Se recarga por USB.", "zoom"),
   ("luz5", "Armario, cocina o pasillo. Enlace en el perfil.", "shake"),
 ],
}

HOOKS = {
 "no-sabia-que-lo-necesitaba": "Cosas que NO sabía que necesitaba",
 "mampara-sin-marcas": "Adiós marcas en la mampara",
 "casero-ni-un-agujero": "POV: tu casero dice «ni un agujero»",
 "armario-a-oscuras": "Tu armario, pero con luz",
}

def fill_frame(img, t, eff, seed):
    """Imagen a pantalla completa 9:16: si es cuadrada, fondo difuminado + imagen grande con zoom."""
    iw, ih = img.size
    if abs(iw / ih - W / H) < 0.05:
        base = img.resize((W, H), Image.LANCZOS)
    else:
        bg = img.resize((int(H * iw / ih) if iw / ih > W / H else W, H if iw / ih > W / H else int(W * ih / iw)), Image.LANCZOS)
        bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H)).filter(ImageFilter.GaussianBlur(40))
        bg = Image.eval(bg, lambda v: int(v * 0.75))
        # recorte vertical de la imagen: aprovecha el centro, rellena 80 % del alto
        tw = int(W * 1.0); th = int(tw * ih / iw)
        fg = img.resize((tw, th), Image.LANCZOS)
        bg.paste(fg, (0, (H - th) // 2 - 40)); base = bg
    z = 1.0 + (0.12 * t if eff in ("zoom", "slow") else 0.05)
    cw, ch = W / z, H / z
    rnd = random.Random(seed)
    sx = math.sin(t * 17 + seed) * 6 + math.sin(t * 29) * 3 if eff == "shake" else 0
    sy = math.cos(t * 13 + seed) * 6 if eff == "shake" else 0
    x0 = (W - cw) / 2 + sx; y0 = (H - ch) / 2 + sy
    return base.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)

def video_frames(path):
    """Clip cuadrado → fotogramas 9:16 recortando el centro."""
    side = 1920
    cmd = [R.FFMPEG, "-loglevel", "error", "-i", path, "-vf", f"scale={side}:{side},crop={W}:{H},fps={FPS}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (W * H * 3)
    return [Image.frombytes("RGB", (W, H), raw[i * W * H * 3:(i + 1) * W * H * 3]) for i in range(n)]

def caption(c, text, y=1050, size=78):
    """Subtítulo estilo TikTok: blanco con contorno negro y la palabra actual en amarillo."""
    d = ImageDraw.Draw(c); f = F(size)
    words = text.split(); lines, cur = [], []
    for w in words:
        if f.getlength(" ".join(cur + [w])) > 900 and cur: lines.append(cur); cur = [w]
        else: cur.append(w)
    lines.append(cur)
    for li, ln in enumerate(lines):
        tw = f.getlength(" ".join(ln)); x = (W - tw) / 2; yy = y + li * int(size * 1.2)
        for wi, w in enumerate(ln):
            col = (255, 214, 10) if (li == len(lines) - 1 and wi == len(ln) - 1) else (255, 255, 255)
            d.text((x, yy), w, font=f, fill=col, stroke_width=9, stroke_fill=(0, 0, 0))
            x += f.getlength(w + " ")

def chunks(text, n=3):
    w = text.split(); return [" ".join(w[i:i + n]) for i in range(0, len(w), n)]

def main(keys):
    os.makedirs(f"{D}/out/ugc", exist_ok=True)
    for key in keys:
        scenes = VIDEOS[key]; tmp = f"{D}/voz/ugc-{key}"; os.makedirs(tmp, exist_ok=True)
        durs, params = [], None
        for i, (_, vo, _) in enumerate(scenes):
            d, params = tts(vo, f"{tmp}/{i}.wav"); durs.append(d + 0.15)
        with wave.open(f"{tmp}/voz.wav", "wb") as out:
            out.setparams(params)
            for i, dd in enumerate(durs):
                with wave.open(f"{tmp}/{i}.wav") as w: data = w.readframes(w.getnframes())
                out.writeframes(data)
                pad = int((dd - w.getnframes() / params.framerate) * params.framerate)
                out.writeframes(b"\x00" * max(0, pad) * params.sampwidth * params.nchannels)
        srcs = {}
        for s, _, _ in scenes:
            if s not in srcs:
                srcs[s] = video_frames(f"{D}/{s}") if s.endswith(".mp4") else Image.open(next(f"{D}/img/{s}.{e}" for e in ("webp", "png") if os.path.exists(f"{D}/img/{s}.{e}"))).convert("RGB")
        outp = f"{D}/out/ugc/{key}.mp4"
        pr = subprocess.Popen([R.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", f"{tmp}/voz.wav", "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", outp], stdin=subprocess.PIPE)
        starts = [sum(durs[:i]) for i in range(len(durs))]
        vid_pos = {}  # posición de reproducción de cada clip, para no repetir el principio
        for fi in range(int(sum(durs) * FPS)):
            t = fi / FPS; i = sum(1 for s in starts if t >= s) - 1; tt = t - starts[i]
            src, vo, eff = scenes[i]; lt = tt / durs[i]
            if src.endswith(".mp4"):
                fr = srcs[src]; key_i = (src, i)
                if key_i not in vid_pos:
                    prev = [p for (s2, j), p in vid_pos.items() if s2 == src]
                    vid_pos[key_i] = (max(prev) + 1) if prev else 0
                speed = 0.5 if eff == "slow" else 1.0
                idx = (vid_pos[key_i] * 45 + int(tt * FPS * speed)) % len(fr)
                c = fill_frame(fr[idx], lt, "zoom" if eff == "slow" else eff, i)
            else:
                c = fill_frame(srcs[src], lt, eff, i)
            c = c.convert("RGBA")
            # destello blanco en cada corte
            if tt < 0.08 and i > 0:
                c.alpha_composite(Image.new("RGBA", (W, H), (255, 255, 255, int(160 * (1 - tt / 0.08)))))
            # subtítulo por trozos de 3 palabras, sincronizado con la voz
            ch = chunks(vo); k = min(len(ch) - 1, int(lt * len(ch)))
            pop = 1 + 0.12 * max(0, 1 - ((lt * len(ch)) % 1) * 6)
            caption(c, ch[k], y=1080, size=int(80 * pop))
            # gancho fijo arriba en el primer plano
            if t < 3.0:
                d = ImageDraw.Draw(c); f = F(66); hook = HOOKS[key]
                ws = hook.split(); ls, cu = [], []
                for w in ws:
                    if f.getlength(" ".join(cu + [w])) > 880 and cu: ls.append(cu); cu = [w]
                    else: cu.append(w)
                ls.append(cu)
                for li, ln in enumerate(ls):
                    tx = " ".join(ln); tw = f.getlength(tx); yy = 250 + li * 96
                    d.rounded_rectangle((W / 2 - tw / 2 - 26, yy - 8, W / 2 + tw / 2 + 26, yy + 84), 22, fill=(255, 255, 255))
                    d.text((W / 2 - tw / 2, yy), tx, font=f, fill=(0, 0, 0))
            # marca discreta
            ImageDraw.Draw(c).text((40, 1730), "@jarandana", font=F(34), fill=(255, 255, 255, 200), stroke_width=4, stroke_fill=(0, 0, 0))
            pr.stdin.write(c.convert("RGB").tobytes())
        pr.stdin.close(); pr.wait(); print("ok", outp, round(sum(durs), 1), "s")

if __name__ == "__main__":
    main(sys.argv[1:] or list(VIDEOS))

"""Vídeos con los formatos virales de TikTok/Reels para productos de hogar (sin voz sintética).
Patrones: producto en acción desde el fotograma 0, texto nativo (recuadro blanco) en <0,5 s,
problema → solución, números concretos, bucle, sonido real (ASMR) cuando el clip lo tiene."""
import os, sys, subprocess, wave, struct
from PIL import Image, ImageDraw, ImageFont
import render as R
from ugc import fill_frame, video_frames

D = R.D; W, H, FPS = 1080, 1920, 30
F = lambda s, w=600: ImageFont.truetype(f"{D}/fonts/P{w}.ttf", s)
SR = 44100

# plano: (fuente, segundos, texto, efecto, inicio_clip_s)
VIDEOS = {
 # ===== UGC en primera persona (fotos POV animadas en 3D + clips reales) =====
 "ugc-grifo": [
  ("ugc_clips/grifo.mp4", 2.6, "POV: le pones esto a tu grifo de siempre 👀", "none", 0),
  ("kling/grifo.mp4", 2.6, "y ahora gira 1080° y cambia a modo ducha 🤯", "none", 0),
  ("grifo1", 1.6, "se enrosca en 1 minuto, sin fontanero", "zoom", 0),
  ("kling/grifo.mp4", 2.2, "12,90 € · enlace en el perfil", "none", 2.6),
 ],
 "ugc-luz": [
  ("ugc_clips/luz.mp4", 2.8, "cosas que tu piso de alquiler necesita y no sabías 💡", "none", 0),
  ("kling/luz.mp4", 2.6, "se enciende sola cuando abres", "none", 0),
  ("luz3", 1.8, "imán + adhesivo · cero agujeros", "zoom", 0),
  ("ugc_clips/luz.mp4", 1.6, "enlace en el perfil 🔗", "none", 2.2),
 ],
 "ugc-mampara": [
  ("ugc_clips/rasqueta.mp4", 2.8, "el truco de 10 segundos para que la mampara no tenga marcas ✨", "none", 0),
  ("kling/rasqueta.mp4", 3.0, "quitas el agua antes de que se seque", "none", 0.5),
  ("ras3", 1.8, "y se queda colgada en la mampara", "zoom", 0),
  ("ugc_clips/rasqueta.mp4", 1.4, "15,90 € · enlace en el perfil", "none", 2.4),
 ],
 "ugc-ducha": [
  ("ugc_clips/balda.mp4", 2.6, "tu casero: «ni un agujero» 🙅\ntú:", "none", 0),
  ("bal4", 1.8, "balda que se cuelga del grifo", "zoom", 0),
  ("gan1", 1.6, "+ ganchos adhesivos", "shake", 0),
  ("ugc_clips/balda.mp4", 2.0, "todo sin taladrar 🙌 enlace en el perfil", "none", 1.8),
 ],
 # 1 · Frustración → solución
 "frustracion-ducha": [
  ("bal5", 2.2, "nadie te avisa de lo difícil que es tener la ducha ordenada en un piso de alquiler 😩", "shake", 0),
  ("bal2", 1.8, "y el casero: «ni un agujero» 🙅", "zoom", 0),
  ("bal4", 2.0, "hasta que encontré esto", "zoom", 0),
  ("bal6", 2.0, "se cuelga del grifo. cero taladro", "shake", 0),
  ("gan1", 1.8, "+ ganchos adhesivos para las toallas", "zoom", 0),
  ("bal1", 2.2, "baño ordenado en 5 minutos ✨\nenlace en el perfil", "zoom", 0),
 ],
 # 2 · Satisfactorio con sonido real (bucle)
 "asmr-grifo": [
  ("kling/grifo.mp4", 2.4, "no sabía que un grifo podía hacer esto 🤯", "none", 0),
  ("kling/grifo.mp4", 2.6, "sube el volumen 🔊", "none", 2.4),
  ("grifo1", 1.6, "gira 1080°", "zoom", 0),
  ("kling/grifo.mp4", 2.4, "12,90 € y se pone en 1 minuto", "none", 0),
 ],
 # 3 · Lista con números concretos
 "3-cosas-menos-25": [
  ("kling/luz.mp4", 2.2, "3 cosas de menos de 25 € que cambiaron mi piso de alquiler 👇", "none", 0),
  ("kling/grifo.mp4", 2.3, "1. grifo que gira 1080° · 12,90 €", "none", 1.0),
  ("kling/rasqueta.mp4", 2.3, "2. rasqueta para la mampara · 15,90 €", "none", 0.5),
  ("kling/luz.mp4", 2.3, "3. luz que se enciende sola · 24,90 €", "none", 1.5),
  ("ras3", 2.0, "todo sin taladrar 🙌\n¿cuál te llevas? 1, 2 o 3", "zoom", 0),
 ],
 # 4 · Antes / después
 "antes-despues-mampara": [
  ("kling/rasqueta.mp4", 1.2, "mi mampara ANTES 😬", "none", 0),
  ("kling/rasqueta.mp4", 3.0, "10 segundos después de ducharme…", "none", 0.2),
  ("kling/rasqueta.mp4", 1.8, "DESPUÉS ✨", "none", 3.2),
  ("ras3", 2.0, "y se queda colgada en la mampara\nenlace en el perfil", "zoom", 0),
 ],
 # 5 · POV / meme de texto
 "pov-armario": [
  ("luz4", 2.0, "POV: buscas un calcetín a las 7 de la mañana sin despertar a nadie 🧦", "shake", 0),
  ("kling/luz.mp4", 2.6, "y la luz se enciende sola 💡", "none", 0),
  ("luz3", 1.8, "imán + adhesivo · recargable por USB", "zoom", 0),
  ("kling/luz.mp4", 2.0, "la mejor compra de 24,90 € de mi vida\nenlace en el perfil", "none", 2.6),
 ],
}

def native_text(c, text, y=330, size=62):
    """Estilo "texto con fondo" de TikTok: recuadro blanco redondeado por línea, letra negra."""
    d = ImageDraw.Draw(c); f = F(size, 600); maxw = 880
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if f.getlength(t) > maxw and cur: lines.append(cur); cur = w
            else: cur = t
        lines.append(cur)
    lh = int(size * 1.32)
    for i, ln in enumerate(lines):
        # emojis con la fuente de color
        parts = R.split_emoji(ln)
        tw = sum(f.getlength(p) if k == "t" else size * 1.05 for k, p in parts)
        x0 = (W - tw) / 2; yy = y + i * lh
        d.rounded_rectangle((x0 - 22, yy - 10, x0 + tw + 22, yy + lh - 8), 18, fill=(255, 255, 255))
        x = x0
        for k, p in parts:
            if k == "t":
                d.text((x, yy), p, font=f, fill=(0, 0, 0)); x += f.getlength(p)
            else:
                em = Image.new("RGBA", (136, 128)); ImageDraw.Draw(em).text((0, 0), p, font=R.EMO, embedded_color=True)
                em = em.resize((int(size * 0.95), int(size * 0.9)), Image.LANCZOS); c.alpha_composite(em, (int(x), int(yy + size * 0.12))); x += size * 1.05

def clip_audio(path, start, dur):
    """Audio real del clip (mono 44,1 kHz, 16 bits) o silencio si no tiene."""
    r = subprocess.run([R.FFMPEG, "-loglevel", "error", "-ss", str(start), "-t", str(dur), "-i", path, "-vn", "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", "-"], capture_output=True)
    data = r.stdout; need = int(dur * SR) * 2
    return (data + b"\x00" * need)[:need]

def main(keys):
    os.makedirs(f"{D}/out/viral", exist_ok=True)
    cache = {}
    for key in keys:
        shots = VIDEOS[key]; total = sum(s[1] for s in shots)
        # pista de audio: sonido real de los clips que lo tienen
        audio = b"".join(clip_audio(f"{D}/{s}", st, d) if s.endswith(".mp4") else b"\x00" * (int(d * SR) * 2) for s, d, _, _, st in shots)
        wav = f"{D}/out/viral/{key}.wav"
        with wave.open(wav, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(audio)
        for s, *_ in shots:
            if s not in cache:
                cache[s] = video_frames(f"{D}/{s}") if s.endswith(".mp4") else Image.open(next(f"{D}/img/{s}.{e}" for e in ("webp", "png") if os.path.exists(f"{D}/img/{s}.{e}"))).convert("RGB")
        out = f"{D}/out/viral/{key}.mp4"
        pr = subprocess.Popen([R.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", wav, "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        starts = [sum(s[1] for s in shots[:i]) for i in range(len(shots))]
        for fi in range(int(total * FPS)):
            t = fi / FPS; i = sum(1 for s in starts if t >= s) - 1; tt = t - starts[i]
            src, dur, text, eff, st = shots[i]
            if src.endswith(".mp4"):
                fr = cache[src]; idx = min(len(fr) - 1, int((st + tt) * FPS))
                c = fill_frame(fr[idx], tt / dur, eff if eff != "none" else "static", i)
            else:
                c = fill_frame(cache[src], tt / dur, eff, i)
            c = c.convert("RGBA")
            native_text(c, text)
            ImageDraw.Draw(c).text((44, 1700), "@jarandana", font=F(32, 600), fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0))
            pr.stdin.write(c.convert("RGB").tobytes())
        pr.stdin.close(); pr.wait(); os.remove(wav); print("ok", out, round(total, 1), "s")

if __name__ == "__main__":
    main(sys.argv[1:] or list(VIDEOS))

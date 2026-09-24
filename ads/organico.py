"""Vídeos orgánicos (TikTok/Reels) con voz en off sintética (Piper, voz es_ES davefx, licencia CC0) y subtítulos."""
import subprocess, wave, os, sys
from PIL import Image, ImageDraw
import render as R
from render import W, H, FPS, OR, PK, INK, SUN, TEAL, FF, ease, pill, draw_text_block, photo_frame, load_video
from campana import bg

D = R.D
VOZ = f"{D}/voz/davefx.onnx"

VIDEOS = {
 "3-inventos": dict(col=OR, scenes=[
   (None, "3 inventos para tu casa [de alquiler] 🏠", "¿Vives de alquiler? Mira estos tres inventos que se ponen sin taladrar."),
   ("kling/grifo.mp4", "1. Grifo [1080°]", "Uno. Este grifo gira hacia donde quieras y cambia a modo ducha. Se enrosca en un minuto."),
   ("kling/luz.mp4", "2. Luz con [sensor]", "Dos. Una luz con sensor de movimiento. Abres el armario y se enciende sola."),
   ("kling/rasqueta.mp4", "3. Rasqueta para [la mampara]", "Tres. Diez segundos con la rasqueta después de ducharte y la mampara sin marcas."),
   (None, "¿Cuál te llevas? [1, 2 o 3] 👇", "¿Cuál te llevarías? Te leo en comentarios. Los tienes en el enlace del perfil."),
 ]),
 "casero": dict(col=PK, scenes=[
   (None, "POV: tu casero dice [«ni un agujero»] 🙅", "Cuando tu casero te dice: ni un agujero en la pared."),
   ("bal2", "Balda de ducha [sin taladro]", "Pues balda de ducha igualmente. Sin taladro y sin obras."),
   ("ras4", "Rasqueta [siempre a mano]", "Rasqueta colgada en la mampara, siempre a mano."),
   ("gan1", "Ganchos [adhesivos]", "Y ganchos para las toallas. Todo adhesivo."),
   ("esq3", "Y cuando te mudas… [te lo llevas]", "Y cuando te mudes, calor con el secador, lo despegas y te lo llevas."),
   (None, "Tu casa, [sin taladrar] 🧡", "Tu casa, sin taladrar. Jarandana. Enlace en el perfil."),
 ]),
}

def tts(text, path):
    subprocess.run([sys.executable, "-m", "piper", "-m", VOZ, "-f", path, "--length-scale", "0.9", "--sentence-silence", "0.15"],
                   input=text.encode(), check=True, capture_output=True)
    with wave.open(path) as w: return w.getnframes() / w.getframerate(), w.getparams()

def main(keys):
    for key in keys:
        v = VIDEOS[key]; col = v["col"]; tmp = f"{D}/voz/{key}"; os.makedirs(tmp, exist_ok=True)
        durs, frames_audio, params = [], [], None
        for i, (_, _, vo) in enumerate(v["scenes"]):
            dur, params = tts(vo, f"{tmp}/{i}.wav"); durs.append(dur + 0.45)
        # audio concatenado con silencio entre escenas
        with wave.open(f"{tmp}/voz.wav", "wb") as out:
            out.setparams(params)
            for i, dd in enumerate(durs):
                with wave.open(f"{tmp}/{i}.wav") as w: data = w.readframes(w.getnframes())
                out.writeframes(data)
                pad = int((dd - len(data) / params.sampwidth / params.nchannels / params.framerate) * params.framerate)
                out.writeframes(b"\x00" * max(0, pad) * params.sampwidth * params.nchannels)
        clips = {}
        for s, *_ in v["scenes"]:
            if s and s not in clips: clips[s] = load_video(f"{D}/{s}") if s.endswith(".mp4") else Image.open(f"{D}/img/{s}.webp").convert("RGB")
        base = bg(col); logo = R.LOGO.resize((280, int(280 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
        biglogo = R.LOGO.resize((620, int(620 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
        outp = f"{D}/out/organico-{key}.mp4"
        pr = subprocess.Popen([R.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", f"{tmp}/voz.wav", "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", outp], stdin=subprocess.PIPE)
        starts = [sum(durs[:i]) for i in range(len(durs))]
        for fi in range(int(sum(durs) * FPS)):
            t = fi / FPS; i = sum(1 for s in starts if t >= s) - 1; tt = t - starts[i]
            src, title, vo = v["scenes"][i]
            c = base.copy(); c.alpha_composite(logo, (int(W / 2 - 140), 60))
            if src is None:
                sc = 0.9 + 0.1 * ease(tt / 0.4)
                lg = biglogo.resize((int(biglogo.width * sc), int(biglogo.height * sc)), Image.LANCZOS)
                if i == len(v["scenes"]) - 1: c.alpha_composite(lg, (int(W / 2 - lg.width / 2), 420))
                draw_text_block(c, title, 760 if i else 620, 90, (255, 255, 255), SUN if col != SUN else OR, tt / 0.7)
            else:
                draw_text_block(c, title, 220, 84, (255, 255, 255), SUN, tt / 0.6)
                fr = clips[src]
                ph = fr[min(len(fr) - 1, int(tt * FPS))] if isinstance(fr, list) else photo_frame(fr, tt / durs[i], i)
                enter = ease(tt / 0.35); x = int(60 + (1 - enter) * 1080 * (1 if i % 2 else -1))
                c.alpha_composite(ph, (x, 450))
            # subtítulo de la voz (fuera de la zona de interfaz inferior)
            f = FF(40, 600); lines = R.wrap(vo, f, 900)
            d = ImageDraw.Draw(c); y0 = 1440
            for k, ln in enumerate(lines[:3]):
                tw = f.getlength(ln); yy = y0 + k * 62
                d.rounded_rectangle((W / 2 - tw / 2 - 18, yy - 6, W / 2 + tw / 2 + 18, yy + 56), 14, fill=(0, 0, 0, 150))
                d.text((W / 2 - tw / 2, yy), ln, font=f, fill=(255, 255, 255))
            pr.stdin.write(c.convert("RGB").tobytes())
        pr.stdin.close(); pr.wait(); print("ok", outp)

if __name__ == "__main__":
    main(sys.argv[1:] or list(VIDEOS))

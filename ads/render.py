"""Genera anuncios verticales 1080x1920 para Reels/TikTok/Stories con fotos reales del producto.
Uso: python3 ads/render.py [nombre]   (sin nombre: todos)"""
import os, sys, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
OR, PK, INK, CREAM, SUN, TEAL = (255,107,44), (255,77,141), (29,29,31), (255,248,238), (255,200,61), (0,168,150)
FF = lambda s, w=800: ImageFont.truetype(f"{D}/fonts/P{w}.ttf", s)
EMO = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)
LOGO = Image.open(f"{D}/../brand/logo/png/jarandana-logo-mono-blanco@2x.png").convert("RGBA")
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")

ADS = {
 "grifo": dict(bg=TEAL, price="12,90 €", name="Grifo 1080°", scenes=[
   ("grifo4", "Tu grifo puede hacer [ESTO] 👀"),
   ("grifo1", "Gira 1080° hacia donde quieras"),
   ("paso_grifo", "2 chorros: suave o a presión"),
   ("grifo3", "Se enrosca en 1 minuto. Sin fontanero"),
 ]),
 "luz": dict(bg=INK, price="24,90 €", name="Luz LED con sensor", scenes=[
   ("luz2", "Se acabó buscar [a oscuras] 🔦"),
   ("luz4", "Pasas… y se enciende sola"),
   ("luz3", "Imán + adhesivo. Cero agujeros"),
   ("luz5", "Armario, cocina, pasillo o baño"),
 ]),
 "rasqueta": dict(bg=OR, price="15,90 €", name="Rasqueta con soporte", scenes=[
   ("ras5", "El truco para una mampara [sin cal] ✨"),
   ("ras4", "10 segundos después de ducharte"),
   ("ras3", "Se cuelga en la mampara. Siempre a mano"),
   ("ras1", "Silicona: no raya el cristal"),
 ]),
 "kit-ducha": dict(bg=PK, price="49,90 €", name="Kit Ducha Sin Cal", scenes=[
   ("bal2", "Mi casero: [«ni un agujero»] 🙅"),
   ("bal4", "Yo: balda en la ducha igualmente"),
   ("bal6", "Sin taladro, sin obras"),
   ("ras4", "+ rasqueta y ganchos en un solo kit"),
 ]),
 "fregadero": dict(bg=SUN, price="19,90 €", name="Kit Fregadero", scenes=[
   ("fre1", "Friegas con [una mano] 🧽"),
   ("fre3", "Presionas y sale el jabón justo"),
   ("fre2", "La esponja se seca encima"),
   ("fre1", "Fregadero ordenado en 1 segundo"),
 ]),
}

def ease(t): return 1 - (1 - max(0, min(1, t))) ** 3

def rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, *im.size), r, fill=255)
    o = Image.new("RGBA", im.size); o.paste(im, (0, 0), m); return o

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t.replace("[", "").replace("]", "")) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def split_emoji(line):
    out, buf = [], ""
    for ch in line:
        if ord(ch) > 0x2600 and ch not in "«»…°€": 
            if buf: out.append(("t", buf)); buf = ""
            out.append(("e", ch))
        elif ch == "️": continue
        else: buf += ch
    if buf: out.append(("t", buf))
    return out

def draw_text_block(canvas, text, y, size, color, hl, prog, maxw=940):
    font = FF(size)
    lines = wrap(text, font, maxw)
    lh = int(size * 1.18)
    inhl = False
    for i, line in enumerate(lines):
        p = ease(prog * 1.6 - i * 0.18)
        if p <= 0: continue
        segs = split_emoji(line)
        wid = sum(font.getlength(s.replace("[", "").replace("]", "")) if k == "t" else size * 1.05 for k, s in segs)
        layer = Image.new("RGBA", (W, lh + 30), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
        x = (W - wid) / 2
        for k, s in segs:
            if k == "e":
                em = Image.new("RGBA", (136, 128)); ImageDraw.Draw(em).text((0, 0), s, font=EMO, embedded_color=True)
                em = em.resize((int(size * 1.0), int(size * 0.94)), Image.LANCZOS); layer.alpha_composite(em, (int(x), int(size * 0.14))); x += size * 1.05; continue
            for part in s.replace("[", "\x00[").replace("]", "]\x00").split("\x00"):
                if not part: continue
                if part.startswith("["): inhl = True; part = part[1:]
                end = part.endswith("]")
                if end: part = part[:-1]
                pw = font.getlength(part)
                if inhl and part.strip():
                    d.rounded_rectangle((x - 8, size * 0.28, x + pw + 8, size * 1.12), 14, fill=hl)
                d.text((x, 0), part, font=font, fill=color)
                x += pw
                if end: inhl = False
        dy = int((1 - p) * 60)
        layer.putalpha(Image.eval(layer.getchannel("A"), lambda a: int(a * p)))
        canvas.alpha_composite(layer, (0, y + i * lh + dy))
    return len(lines) * lh

def pill(canvas, text, cx, y, size, bg, fg, scale=1.0, font_w=800):
    f = FF(int(size * scale), font_w); tw = f.getlength(text)
    pw, ph = tw + size * 1.2 * scale, size * 1.7 * scale
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle((cx - pw / 2, y, cx + pw / 2, y + ph), ph / 2, fill=bg)
    d.text((cx - tw / 2, y + ph * 0.2), text, font=f, fill=fg)

def photo_frame(img, t, idx):
    side = 960
    z = 1.0 + 0.10 * t
    iw, ih = img.size; s = min(iw, ih)
    cw = s / z
    ox = [(0.5, 0.5), (0.35, 0.5), (0.65, 0.5), (0.5, 0.4)][idx % 4]
    cx = iw * 0.5 + (iw * ox[0] - iw * 0.5) * t; cy = ih * 0.5 + (ih * ox[1] - ih * 0.5) * t
    box = (cx - cw / 2, cy - cw / 2, cx + cw / 2, cy + cw / 2)
    box = (max(0, box[0]), max(0, box[1]), min(iw, box[2]), min(ih, box[3]))
    return rounded(img.crop(tuple(map(int, box))).resize((side, side), Image.LANCZOS), 48)

def render(key):
    ad = ADS[key]; bg = ad["bg"]; dark = bg in (INK, TEAL, PK, OR)
    fg = (255, 255, 255) if dark else INK
    hl = SUN if bg != SUN else OR
    hlc = INK
    imgs = {n: Image.open(next(f"{D}/img/{n}.{e}" for e in ("webp", "png", "jpg") if os.path.exists(f"{D}/img/{n}.{e}"))).convert("RGB") for n, _ in ad["scenes"]}
    SC, END = 2.6, 3.4
    total = SC * len(ad["scenes"]) + END
    out = f"{D}/out/jarandana-{key}.mp4"; os.makedirs(f"{D}/out", exist_ok=True)
    p = subprocess.Popen([FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
                          "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    base = Image.new("RGBA", (W, H), bg + (255,))
    # patrón de azulejo sutil
    pat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(pat)
    for yy in range(0, H, 90):
        for xx in range(0, W, 90):
            if (xx // 90 + yy // 90) % 2 == 0: pd.rounded_rectangle((xx + 6, yy + 6, xx + 84, yy + 84), 16, fill=(255, 255, 255, 14 if dark else 40))
    base.alpha_composite(pat)
    logo = LOGO if dark else Image.open(f"{D}/../brand/logo/png/jarandana-logo-mono-negro@2x.png").convert("RGBA")
    logo = logo.resize((300, int(300 * logo.height / logo.width)), Image.LANCZOS)
    n = int(total * FPS)
    for fi in range(n):
        t = fi / FPS
        c = base.copy()
        si = int(t // SC)
        if si < len(ad["scenes"]):
            name, txt = ad["scenes"][si]; lt = (t - si * SC) / SC
            ph = photo_frame(imgs[name], lt, si)
            enter = ease((t - si * SC) / 0.35)
            sh = Image.new("RGBA", (1000, 1000), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((20, 20, 980, 980), 48, fill=(0, 0, 0, 90))
            sh = sh.filter(ImageFilter.GaussianBlur(18))
            x = int(60 + (1 - enter) * 1080 * (1 if si % 2 == 0 else -1)) if si else 60
            y = 540
            c.alpha_composite(sh, (x - 20, y - 5)); c.alpha_composite(ph, (x, y))
            draw_text_block(c, txt, 230, 92 if si == 0 else 72, fg, hl, (t - si * SC) / 0.9)
            # barra de progreso de escenas
            for k in range(len(ad["scenes"])):
                d = ImageDraw.Draw(c); x0 = 90 + k * (900 / len(ad["scenes"]))
                d.rounded_rectangle((x0, 170, x0 + 900 / len(ad["scenes"]) - 14, 180), 5, fill=(255, 255, 255, 90) if dark else (0, 0, 0, 40))
                fill = 1 if k < si else (lt if k == si else 0)
                if fill > 0: d.rounded_rectangle((x0, 170, x0 + (900 / len(ad["scenes"]) - 14) * fill, 180), 5, fill=hl)
            pill(c, f"{ad['name']} · {ad['price']}", W / 2, 1540, 46, (255, 255, 255), INK, font_w=600)
            c.alpha_composite(logo, (int(W / 2 - logo.width / 2), 60))
        else:
            et = t - SC * len(ad["scenes"])
            c = Image.new("RGBA", (W, H), OR + (255,)); c.alpha_composite(pat)
            lg = LOGO.resize((760, int(760 * LOGO.height / LOGO.width)), Image.LANCZOS)
            sc = 0.85 + 0.15 * ease(et / 0.5)
            lg = lg.resize((int(lg.width * sc), int(lg.height * sc)), Image.LANCZOS)
            c.alpha_composite(lg, (int(W / 2 - lg.width / 2), 430))
            draw_text_block(c, "Tu casa, [sin taladrar].", 760, 74, (255, 255, 255), SUN, et / 0.8)
            if et > 0.5: pill(c, f"{ad['name']} · {ad['price']}", W / 2, 1000, 46, (255, 255, 255), INK, font_w=800)
            if et > 0.9: pill(c, "🚚 Envío GRATIS desde 35 €".replace("🚚 ", ""), W / 2, 1150, 40, INK, (255, 255, 255), font_w=600)
            if et > 1.2:
                bounce = 1 + 0.05 * math.sin(et * 7)
                pill(c, "Pídelo en el enlace 👆".replace(" 👆", ""), W / 2, 1300, 52, SUN, INK, scale=bounce)
            if et > 1.5: pill(c, "-10 % con BIENVENIDA10", W / 2, 1480, 38, PK, (255, 255, 255), font_w=600)
        p.stdin.write(c.convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    for k in (sys.argv[1:] or ADS): render(k)

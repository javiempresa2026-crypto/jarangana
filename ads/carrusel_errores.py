"""Carrusel educativo 1080x1350: «3 errores que hacen que tu balda adhesiva se caiga».
Formato "guardable" (lo que más alcance da en Instagram): error ❌ → solución ✅, con fotos reales."""
import os
from PIL import Image, ImageDraw
import render as R
from render import FF, INK, SUN, OR, draw_text_block, rounded, pill
from campana import bg as bg_full

D = R.D; W, H = 1080, 1350
OUT = f"{D}/out/posts"; os.makedirs(OUT, exist_ok=True)
WHITE, RED, GREEN, CREAM = (255, 255, 255), (214, 40, 57), (22, 150, 90), (255, 248, 238)

def bg(col): return bg_full(col).crop((0, 0, W, H))
def logo(w=240):
    l = R.LOGO; return l.resize((w, int(w * l.height / l.width)), Image.LANCZOS)
def photo(name, side, box=None):
    im = Image.open(f"{D}/img/{name}.webp").convert("RGB"); w, h = im.size; s = min(w, h)
    return rounded(im.crop(box or ((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)).resize((side, side), Image.LANCZOS), 40)
def badge(c, cx, cy, ok):
    d = ImageDraw.Draw(c); r = 54
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GREEN if ok else RED, outline=WHITE, width=6)
    if ok: d.line([(cx - 24, cy + 2), (cx - 6, cy + 22), (cx + 26, cy - 20)], fill=WHITE, width=13, joint="curve")
    else:
        d.line([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=WHITE, width=13); d.line([(cx - 20, cy + 20), (cx + 20, cy - 20)], fill=WHITE, width=13)
def counter(c, i, n=5):
    f = FF(30, 600); t = f"{i}/{n}"; d = ImageDraw.Draw(c)
    d.rounded_rectangle((W - 150, 56, W - 50, 106), 25, fill=(0, 0, 0, 90)); d.text((W - 100 - f.getlength(t) / 2, 62), t, font=f, fill=WHITE)
def swipe(c):
    f = FF(34); t = "Desliza »"; tw = f.getlength(t); d = ImageDraw.Draw(c)
    d.rounded_rectangle((W - tw - 110, H - 130, W - 50, H - 66), 32, fill=SUN); d.text((W - tw - 80, H - 123), t, font=f, fill=INK)
def save(c, name): c.convert("RGB").save(f"{OUT}/{name}.jpg", quality=93); print(name)

# 1 · Portada
c = bg(INK); c.alpha_composite(logo(), (70, 60)); counter(c, 1)
draw_text_block(c, "3 errores que hacen que tu balda adhesiva [se caiga] 😱", 170, 84, WHITE, OR, 10, 940)
c.alpha_composite(photo("bal4", 520), (280, 610))
pill(c, "Guárdalo antes de instalarla", W / 2, 1180, 34, SUN, INK)
swipe(c); save(c, "10-errores-1-portada")

# 2-4 · Errores
ERR = [
 ("Pegarla en gotelé, pintura o madera sin lacar", "Solo en superficie lisa: [azulejo, cristal o metal]", "bal5"),
 ("Pegarla sin limpiar la pared", "Limpia con [alcohol] y seca bien: la grasa y el jabón no dejan pegar", "gan1"),
 ("Cargarla el mismo día", "Presiona fuerte 30 s y [espera 24 h] antes de mojarla o cargarla", "bal1"),
]
for i, (mal, bien, img) in enumerate(ERR, 2):
    c = bg(OR if i % 2 else INK).convert("RGBA"); c.alpha_composite(logo(200), (70, 64)); counter(c, i)
    d = ImageDraw.Draw(c)
    d.text((70, 150), f"ERROR {i - 1}", font=FF(40), fill=SUN)
    # tarjeta del error
    d.rounded_rectangle((60, 220, W - 60, 520), 36, fill=WHITE)
    badge(c, 150, 370, False)
    tl = R.wrap(mal, FF(52), 720); y0 = 370 - len(tl) * 31
    for k, ln in enumerate(tl): d.text((240, y0 + k * 62), ln, font=FF(52), fill=INK)
    # tarjeta de la solución
    d.rounded_rectangle((60, 560, W - 60, 900), 36, fill=CREAM)
    badge(c, 150, 730, True)
    tl = R.wrap(bien, FF(46, 600), 720); y0 = 730 - len(tl) * 28
    for k, ln in enumerate(tl):
        x = 240
        for part in ln.replace("[", "\x00[").replace("]", "]\x00").split("\x00"):
            if not part: continue
            hl = part.startswith("[") or part.endswith("]"); part = part.strip("[]"); pw = FF(46, 600).getlength(part)
            if hl: d.rounded_rectangle((x - 6, y0 + k * 56 + 6, x + pw + 6, y0 + k * 56 + 54), 12, fill=SUN)
            d.text((x, y0 + k * 56), part, font=FF(46, 600), fill=INK); x += pw
    c.alpha_composite(photo(img, 330), (W // 2 - 165, 940))
    if i < 4: swipe(c)
    save(c, f"10-errores-{i}")

# 5 · Cierre
c = bg(SUN).convert("RGBA"); counter(c, 5)
l = Image.open(f"{D}/../brand/logo/png/jarandana-logo-mono-negro@2x.png").convert("RGBA"); l = l.resize((420, int(420 * l.height / l.width)), Image.LANCZOS)
c.alpha_composite(l, (W // 2 - 210, 120))
draw_text_block(c, "Ahora ya lo sabes ✅", 330, 80, INK, WHITE, 10)
draw_text_block(c, "Mándaselo a quien se acaba de [mudar] 📩", 480, 56, INK, WHITE, 10, 900)
c.alpha_composite(photo("bal1", 440), (W // 2 - 220, 680))
pill(c, "Baldas y ganchos sin taladrar · enlace en el perfil", W / 2, 1160, 32, INK, WHITE, font_w=600)
save(c, "10-errores-5")

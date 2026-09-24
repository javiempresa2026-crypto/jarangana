"""Posts de Instagram 1080x1350 (4:5) con fotos reales y la identidad de jarandana."""
import os
from PIL import Image, ImageDraw
import render as R
from render import OR, PK, INK, SUN, TEAL, FF, draw_text_block, rounded, pill
from campana import bg as bg_full

D = R.D; W, H = 1080, 1350
OUT = f"{D}/out/posts"; os.makedirs(OUT, exist_ok=True)
WHITE = (255, 255, 255)

def bg(col): return bg_full(col).crop((0, 0, W, H))
def logo(dark=True, w=260):
    l = R.LOGO if dark else Image.open(f"{D}/../brand/logo/png/jarandana-logo-mono-negro@2x.png").convert("RGBA")
    return l.resize((w, int(w * l.height / l.width)), Image.LANCZOS)
def photo(name, side=820, crop=None):
    im = Image.open(next(f"{D}/img/{name}.{e}" for e in ("webp", "png") if os.path.exists(f"{D}/img/{name}.{e}"))).convert("RGB")
    w, h = im.size; s = min(w, h)
    box = crop or ((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)
    return rounded(im.crop(box).resize((side, side), Image.LANCZOS), 44)
def sticker(c, text, cx, cy, r=110, fill=SUN, size=48):
    d = ImageDraw.Draw(c); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill, outline=INK, width=5)
    lines = text.split("\n"); f = FF(size)
    for i, ln in enumerate(lines):
        y = cy - len(lines) * size * 0.62 + i * size * 1.2
        d.text((cx - f.getlength(ln) / 2, y), ln, font=f, fill=INK)
def footer(c, dark=True, text="Tu casa, sin taladrar · jarandana"):
    f = FF(30, 600); col = (255, 255, 255, 200) if dark else (29, 29, 31, 200)
    ImageDraw.Draw(c).text((W / 2 - f.getlength(text) / 2, H - 70), text, font=f, fill=col)
def swipe(c, dark=True):
    f = FF(34, 800); t = "Desliza »"
    d = ImageDraw.Draw(c); tw = f.getlength(t)
    d.rounded_rectangle((W - tw - 110, H - 150, W - 50, H - 86), 32, fill=SUN if dark else INK)
    d.text((W - tw - 80, H - 143), t, font=f, fill=INK if dark else WHITE)
def text(c, t, y, size, dark=True, hl=SUN, maxw=940):
    return draw_text_block(c, t, y, size, WHITE if dark else INK, hl, 10, maxw)
def save(c, name): c.convert("RGB").save(f"{OUT}/{name}.jpg", quality=93); print(name)

def product_post(name, col, img, head, price, sub, crop=None):
    dark = col != SUN; c = bg(col); c.alpha_composite(logo(dark), (W // 2 - 130, 50))
    text(c, head, 150, 72, dark, SUN if dark else OR)
    c.alpha_composite(photo(img, 780, crop), (150, 390))
    sticker(c, price, 880, 430)
    pill(c, sub, W / 2, 1195, 36, WHITE if dark else INK, INK if dark else WHITE, font_w=600)
    footer(c, dark); save(c, name)

# 1 · Presentación de marca
c = bg(OR); l = logo(True, 700); c.alpha_composite(l, (W // 2 - 350, 330))
text(c, "¡Hola! Somos [jarandana] 👋", 620, 74)
text(c, "Accesorios de baño y cocina que se ponen [sin taladrar].", 840, 52)
pill(c, "Ni un agujero · Ni una marca", W / 2, 1060, 38, INK, WHITE, font_w=600); save(c, "01-hola-somos-jarandana")

# 2 · Carrusel: 3 inventos para tu baño de alquiler
c = bg(PK); c.alpha_composite(logo(), (W // 2 - 130, 50))
text(c, "3 inventos para tu casa [de alquiler] 🏠", 260, 96)
text(c, "(que tu casero ni va a notar)", 720, 52)
sticker(c, "SIN\nTALADRO", 540, 1000, 150, SUN, 56); swipe(c); save(c, "02-carrusel-1-portada")
for i, (img, col, h, p) in enumerate([("grifo4", TEAL, "1 · Grifo que gira [1080°]", "12,90 €"),
                                      ("luz2", INK, "2 · Luz que se [enciende sola]", "24,90 €"),
                                      ("ras4", OR, "3 · Mampara [sin marcas]", "15,90 €")], 2):
    c = bg(col); c.alpha_composite(logo(), (W // 2 - 130, 50)); text(c, h, 150, 72)
    c.alpha_composite(photo(img, 780), (150, 390)); sticker(c, p, 880, 430)
    if i < 4: swipe(c)
    else: pill(c, "Los 3 en el enlace del perfil 🔗".replace(" 🔗", ""), W / 2, 1195, 38, SUN, INK)
    footer(c); save(c, f"02-carrusel-{i}")

# 3 · Grifo
product_post("03-grifo", TEAL, "grifo1", "Tu grifo, pero [gira 1080°]", "12,90 €", "2 chorros · Se enrosca en 1 minuto")

# 4 · Meme / frase
c = bg(SUN); c.alpha_composite(logo(False), (W // 2 - 130, 50))
d = ImageDraw.Draw(c)
d.rounded_rectangle((90, 260, 990, 560), 40, fill=WHITE, outline=INK, width=5)
d.text((140, 300), "Mi casero:", font=FF(46, 600), fill=(120, 120, 120))
draw_text_block(c, "«Ni un [agujero] en la pared»", 370, 70, INK, PK, 10, 820)
d.rounded_rectangle((90, 620, 990, 1200), 40, fill=INK)
d.text((140, 660), "Yo:", font=FF(46, 600), fill=(200, 200, 200))
c.alpha_composite(photo("bal2", 400), (340, 700))
draw_text_block(c, "balda puesta igualmente 😎", 1115, 44, WHITE, SUN, 10, 820)
footer(c, False); save(c, "04-meme-casero")

# 5 · Carrusel tutorial: cómo se instala
steps = [("🧼", "Limpia", "con alcohol y seca bien"), ("🩹", "Pega", "en azulejo, cristal o metal lisos"),
         ("💪", "Presiona", "fuerte durante 30 segundos"), ("⏳", "Espera 24 h", "antes de mojar o cargar")]
c = bg(TEAL); c.alpha_composite(logo(), (W // 2 - 130, 50))
text(c, "Cómo instalar [sin taladrar] en 4 pasos", 300, 92)
text(c, "Guárdalo para tu próxima mudanza 📌", 820, 48); swipe(c); save(c, "05-tutorial-1-portada")
for i, (e, t1, t2) in enumerate(steps, 2):
    c = bg([TEAL, OR, PK, INK][i - 2]); c.alpha_composite(logo(), (W // 2 - 130, 50))
    d = ImageDraw.Draw(c); d.ellipse((W / 2 - 150, 250, W / 2 + 150, 550), fill=WHITE)
    em = Image.new("RGBA", (136, 128)); ImageDraw.Draw(em).text((0, 0), e, font=R.EMO, embedded_color=True)
    em = em.resize((200, 188), Image.LANCZOS); c.alpha_composite(em, (W // 2 - 100, 306))
    pill(c, f"PASO {i - 1}", W / 2, 600, 40, SUN, INK)
    text(c, f"[{t1}]", 740, 110); text(c, t2, 900, 56)
    if i < 5: swipe(c)
    else: pill(c, "Superficies NO válidas: gotelé, pintura, madera sin lacar", W / 2, 1110, 28, WHITE, INK, font_w=600)
    footer(c); save(c, f"05-tutorial-{i}")

# 6 · Luz
product_post("06-luz", INK, "luz4", "Pasas… y [se enciende sola] 💡", "24,90 €", "Sensor de movimiento · Recargable USB")

# 7 · Oferta bienvenida
c = bg(PK); c.alpha_composite(logo(), (W // 2 - 130, 50))
text(c, "Tu primer pedido", 230, 70)
f = FF(260); t = "-10 %"; ImageDraw.Draw(c).text((W / 2 - f.getlength(t) / 2, 330), t, font=f, fill=SUN)
pill(c, "Código: BIENVENIDA10", W / 2, 720, 56, WHITE, INK)
pill(c, "Envío GRATIS desde 35 €", W / 2, 880, 44, INK, WHITE, font_w=600)
text(c, "Válido en pedidos desde 25 €", 1030, 40); footer(c); save(c, "07-oferta-bienvenida")

# 8 · Rasqueta
product_post("08-rasqueta", OR, "ras5", "10 segundos y [adiós marcas] ✨", "15,90 €", "Silicona · Con soporte para colgar")

# 9 · Kit ducha
product_post("09-kit-ducha", PK, "bal4", "El kit de la [ducha ordenada]", "49,90 €", "Balda + rasqueta + 2 ganchos · Sin taladro")

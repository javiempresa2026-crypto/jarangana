"""Vídeo largo de campaña (9:16, ~37 s): productos destacados en movimiento, ofertas y llamada a la acción."""
import math, subprocess, os
from PIL import Image, ImageDraw
import render as R
from render import W, H, FPS, OR, PK, INK, SUN, TEAL, FF, ease, pill, draw_text_block, photo_frame, load_video, rounded

D = R.D
URL = "jarandana.myshopify.com"
P = [  # (fuente, color fondo, nombre, precio, frase, duración)
 ("kling/grifo.mp4", TEAL, "Grifo 1080°", "12,90 €", "Gira 1080° y [cambia de chorro]", 5.0),
 ("kling/luz.mp4", INK, "Luz LED con sensor", "24,90 €", "Pasas… y [se enciende sola]", 5.0),
 ("kling/rasqueta.mp4", OR, "Rasqueta con soporte", "15,90 €", "Mampara [sin marcas] en 10 s", 5.0),
 ("bal2", PK, "Kit Ducha Sin Cal", "49,90 €", "Balda + rasqueta + ganchos [sin taladro]", 3.0),
 ("fre3", SUN, "Kit Fregadero", "19,90 €", "Jabón y esponja [con una mano]", 3.0),
 ("esq3", TEAL, "Esquinera Doble", "39,90 €", "2 alturas en la esquina, [cero agujeros]", 3.0),
]
INTRO, OFF, CTA = 3.0, 4.0, 6.0

def bg(color):
    c = Image.new("RGBA", (W, H), color + (255,)); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    a = 18 if color in (INK, TEAL, PK, OR) else 45
    for yy in range(0, H, 90):
        for xx in range(0, W, 90):
            if (xx // 90 + yy // 90) % 2 == 0: d.rounded_rectangle((xx + 6, yy + 6, xx + 84, yy + 84), 16, fill=(255, 255, 255, a))
    c.alpha_composite(lay); return c

def cta_button(c, t, y=1560, big=False, text="COMPRAR AHORA"):
    s = 1 + (0.06 if big else 0.035) * math.sin(t * 6.5)
    size = 60 if big else 44
    f = FF(int(size * s)); tw = f.getlength(text)
    pw, ph = tw + 190 * s, size * 2.0 * s
    x0, y0 = W / 2 - pw / 2, y - ph / 2 + size
    d = ImageDraw.Draw(c)
    d.rounded_rectangle((x0 + 8, y0 + 12, x0 + pw + 8, y0 + ph + 12), ph / 2, fill=(0, 0, 0, 90))
    d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), ph / 2, fill=SUN, outline=INK, width=6)
    d.text((x0 + 60 * s, y0 + ph * 0.2), text, font=f, fill=INK)
    # flecha
    ax = x0 + pw - 95 * s; ay = y0 + ph / 2
    d.polygon([(ax, ay - 22 * s), (ax + 40 * s, ay), (ax, ay + 22 * s)], fill=INK)
    return y0 + ph

def hand(c, x, y, t):
    em = Image.new("RGBA", (136, 128)); ImageDraw.Draw(em).text((0, 0), "👆", font=R.EMO, embedded_color=True)
    tap = abs(math.sin(t * 3.2))
    sz = int(150 - 20 * tap)
    em = em.resize((sz, int(sz * 0.94)), Image.LANCZOS)
    c.alpha_composite(em, (int(x), int(y + 30 * tap)))

def main():
    clips = {s: (load_video(f"{D}/{s}") if s.endswith(".mp4") else Image.open(f"{D}/img/{s}.webp").convert("RGB")) for s, *_ in P}
    logo_w = R.LOGO.resize((700, int(700 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
    logo_s = R.LOGO.resize((280, int(280 * R.LOGO.height / R.LOGO.width)), Image.LANCZOS)
    logo_n = Image.open(f"{D}/../brand/logo/png/jarandana-logo-mono-negro@2x.png").convert("RGBA")
    logo_n = logo_n.resize((280, int(280 * logo_n.height / logo_n.width)), Image.LANCZOS)
    bgs = {col: bg(col) for col in {OR, PK, INK, SUN, TEAL}}
    total = INTRO + sum(p[5] for p in P) + OFF + CTA
    out = f"{D}/out/jarandana-campana.mp4"
    pr = subprocess.Popen([R.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                           "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for fi in range(int(total * FPS)):
        t = fi / FPS
        if t < INTRO:
            c = bgs[OR].copy(); sc = 0.8 + 0.2 * ease(t / 0.5)
            lg = logo_w.resize((int(logo_w.width * sc), int(logo_w.height * sc)), Image.LANCZOS)
            c.alpha_composite(lg, (int(W / 2 - lg.width / 2), 380))
            draw_text_block(c, "¿Vives de alquiler? 🏠", 760, 84, (255, 255, 255), SUN, t / 0.7)
            if t > 1.1: draw_text_block(c, "Baño y cocina ordenados [sin taladrar].", 1000, 66, (255, 255, 255), SUN, (t - 1.1) / 0.7)
        elif t < INTRO + sum(p[5] for p in P):
            tt = t - INTRO; i = 0
            while tt >= P[i][5]: tt -= P[i][5]; i += 1
            src, col, name, price, txt, dur = P[i]
            c = bgs[col].copy(); dark = col != SUN; fg = (255, 255, 255) if dark else INK
            c.alpha_composite(logo_s if dark else logo_n, (int(W / 2 - 140), 60))
            # contador de producto
            ImageDraw.Draw(c).text((W - 190, 70), f"{i + 1}/{len(P)}", font=FF(40, 600), fill=fg)
            draw_text_block(c, txt, 210, 76, fg, SUN if col != SUN else OR, tt / 0.8)
            fr = clips[src]
            ph = fr[min(len(fr) - 1, int(tt * FPS))] if isinstance(fr, list) else photo_frame(fr, tt / dur, i)
            enter = ease(tt / 0.35); x = int(60 + (1 - enter) * 1080 * (1 if i % 2 else -1)); y = 470
            c.alpha_composite(ph, (x, y))
            # etiqueta de precio tipo pegatina
            d = ImageDraw.Draw(c); r = 118; cx, cy = x + 960 - 70, y + 70
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SUN if col != SUN else PK, outline=INK, width=5)
            pf = FF(52); d.text((cx - pf.getlength(price) / 2, cy - 36), price, font=pf, fill=INK)
            pill(c, name, W / 2, 1460, 46, (255, 255, 255), INK, font_w=800)
            cta_button(c, t, y=1590, text="VER EN LA WEB")
        elif t < total - CTA:
            tt = t - INTRO - sum(p[5] for p in P)
            c = bgs[PK].copy()
            c.alpha_composite(logo_s, (int(W / 2 - 140), 60))
            draw_text_block(c, "Ofertas de [bienvenida] 🎁", 230, 84, (255, 255, 255), SUN, tt / 0.6)
            items = [("2 Grifos 1080°", "19,90 €"), ("2 Luces LED", "44,90 €"), ("Kit Ducha", "49,90 €"), ("1.er pedido", "-10 %")]
            for k, (a, b) in enumerate(items):
                p = ease((tt - 0.4 - k * 0.3) / 0.4)
                if p <= 0: continue
                yy = 520 + k * 200; xo = int((1 - p) * 700)
                d = ImageDraw.Draw(c)
                d.rounded_rectangle((90 + xo, yy, 990 + xo, yy + 160), 40, fill=(255, 255, 255))
                d.text((140 + xo, yy + 45), a, font=FF(52, 600), fill=INK)
                bf = FF(60); bw = bf.getlength(b)
                d.rounded_rectangle((940 + xo - bw - 50, yy + 25, 960 + xo, yy + 135), 30, fill=SUN)
                d.text((950 + xo - bw - 30, yy + 38), b, font=bf, fill=INK)
            if tt > 1.8: draw_text_block(c, "Código [BIENVENIDA10] · Envío GRATIS desde 35 €", 1360, 50, (255, 255, 255), INK, (tt - 1.8) / 0.5)
        else:
            tt = t - (total - CTA)
            c = bgs[OR].copy()
            sc = 0.85 + 0.15 * ease(tt / 0.5)
            lg = logo_w.resize((int(logo_w.width * sc), int(logo_w.height * sc)), Image.LANCZOS)
            c.alpha_composite(lg, (int(W / 2 - lg.width / 2), 250))
            draw_text_block(c, "Tu casa, [sin taladrar].", 580, 80, (255, 255, 255), SUN, tt / 0.6)
            if tt > 0.6:
                bottom = cta_button(c, tt, y=820, big=True)
                hand(c, W / 2 + 180, bottom - 20, tt)
            if tt > 1.2:
                f = FF(46, 600); tw = f.getlength(URL)
                ImageDraw.Draw(c).text((W / 2 - tw / 2, 1160), URL, font=f, fill=(255, 255, 255))
            if tt > 1.6:
                for k, s in enumerate(["🚚 Envío 7-15 días", "↩ 14 días devolución", "🔒 Pago seguro"]):
                    s = s.split(" ", 1)[1]
                    pill(c, s, W / 2, 1270 + k * 105, 36, INK, (255, 255, 255), font_w=600)
        pr.stdin.write(c.convert("RGB").tobytes())
    pr.stdin.close(); pr.wait(); print("ok", out)

if __name__ == "__main__":
    main()

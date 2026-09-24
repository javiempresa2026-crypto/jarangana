"""Genera el packaging jarandana: una caja de solapa (troquel plano) por producto + pegatina + tarjeta de gracias.
Salida: packaging/cajas/<producto>.svg (vectorial, para imprenta) y packaging/index.html (vista previa).
Las medidas son ORIENTATIVAS: pide al proveedor las medidas reales del producto/caja y cámbialas en PRODUCTOS.
"""
import os, re, html
D = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(D, "..", "brand", "logo", "svg")

def inner(name):
    s = open(os.path.join(LOGO, name)).read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    body = s[s.index(">", s.index("<svg")) + 1:s.rindex("</svg>")]
    return vb, body

LOGO_COLOR, LOGO_WHITE, ISO = inner("jarandana-logo-horizontal.svg"), inner("jarandana-logo-mono-blanco.svg"), inner("jarandana-isotipo-transparente.svg")
INK, CREAM, ORANGE = "#1E2B37", "#F5EFE4", "#FF6B2C"
LINES = {"Baño": ("#0FA3A3", "#19C2B0"), "Cocina": ("#FF6B2C", "#FF9A3D"), "Novedad": ("#E0245E", "#FF7A9A")}

# clave, nombre, línea, frase, 3 ventajas, contenido, (ancho, fondo, alto) mm ORIENTATIVO
PRODUCTOS = [
 ("balda", "Balda de ducha", "Baño", "Se pega. Aguanta. Se va contigo.", ["Sin taladrar", "Para azulejo, cristal y metal", "Se quita con un secador"], "1 balda de ducha", (300, 100, 60)),
 ("rasqueta", "Rasqueta para mampara", "Baño", "Mampara limpia en 20 segundos.", ["Silicona que no raya", "Con soporte adhesivo", "Sin productos químicos"], "1 rasqueta + 1 soporte", (100, 40, 260)),
 ("ganchos", "Ganchos adhesivos", "Baño", "Toallas en su sitio, azulejo intacto.", ["Sin taladrar", "Acero para zonas húmedas", "Se quitan sin marcas"], "2 o 4 ganchos", (110, 30, 160)),
 ("kit-fregadero", "Kit Fregadero", "Cocina", "Jabón con una mano. Esponja seca.", ["Dispensador de pulsar", "Esponjero que escurre", "Ocupa muy poco"], "1 dispensador + 1 esponjero", (180, 90, 190)),
 ("esquinera", "Esquinera doble", "Baño", "Dos alturas de orden, cero agujeros.", ["Sin taladrar", "2 baldas de esquina", "Para azulejo y cristal"], "Estantería de esquina de 2 alturas", (250, 250, 70)),
 ("bayetas", "Bayetas de microfibra", "Cocina", "Cristales y grifos sin marcas.", ["Microfibra gruesa", "Sin productos químicos", "Lavables"], "8 bayetas", (160, 60, 160)),
 ("recambio", "Recambio de adhesivos", "Baño", "Para volver a pegarlo al mudarte.", ["Cinta doble cara", "3 metros", "Cortas a medida"], "1 rollo de 3 m", (100, 100, 30)),
 ("kit-ducha", "Kit Ducha Sin Cal", "Baño", "Tu ducha, ordenada en 1 minuto.", ["Balda + Rasqueta + 2 Ganchos", "Sin taladrar", "Adiós a la cal"], "1 balda, 1 rasqueta y 2 ganchos", (320, 120, 110)),
 ("grifo", "Grifo 1080°", "Novedad", "Gira hacia donde lo necesites.", ["Giro 1080°", "2 tipos de chorro", "Se enrosca sin herramientas"], "1 o 2 cabezales giratorios", (70, 70, 120)),
 ("luz", "Luz LED con sensor", "Novedad", "Se enciende sola cuando pasas.", ["Sensor de movimiento", "Recargable", "Magnética, sin taladrar"], "1 o 2 luces LED", (80, 40, 240)),
 ("alcachofa", "Alcachofa 5 chorros", "Novedad", "5 chorros para una ducha nueva.", ["5 tipos de chorro", "Con filtro", "Rosca estándar"], "1 alcachofa de ducha", (110, 80, 250)),
 ("dispensador", "Dispensador de pasta", "Novedad", "Pasta justa, lavabo despejado.", ["Dispensa la pasta solo", "Con portacepillos", "Sin taladrar"], "1 dispensador con portacepillos", (180, 70, 150)),
]
S = 4  # px por mm en el SVG (el SVG está en mm vía viewBox; S solo escala el texto)
TUCK, GLUE = 15, 12
e = html.escape

def logo(x, y, w, white=False):
    vb, body = LOGO_WHITE if white else LOGO_COLOR
    _, _, vw, vh = map(float, vb.split())
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{w*vh/vw:.1f}" viewBox="{vb}">{body}</svg>'

def iso(x, y, h, color=None):
    vb, body = ISO
    if color: body = body.replace(INK, color).replace(ORANGE, color).replace("#E4702E", color)
    _, _, vw, vh = map(float, vb.split())
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{h*vw/vh:.1f}" height="{h:.1f}" viewBox="{vb}">{body}</svg>'

def wrap(text, width, size):
    """Parte el texto en líneas según un ancho medio de carácter (0,56 em)."""
    maxc = max(4, int(width / (size * 0.56)))
    out, cur = [], ""
    for w in text.split(" "):
        if len(cur) + len(w) + 1 > maxc and cur: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + [cur] if cur else out

def txt(x, y, text, size, width, color=INK, weight=700, anchor="start", lh=1.18):
    lines = wrap(text, width, size)
    t = "".join(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else size*lh:.1f}">{e(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="DM Sans, Arial, sans-serif" font-size="{size:.1f}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{t}</text>', y + size * lh * (len(lines) - 1)

def pattern(x, y, W, H, k, op=".13"):
    """Dibujo de azulejo muy suave, recortado al panel."""
    cid = f"c{k}{int(x)}{int(y)}"
    step = min(W, H) / 5
    lines = "".join(f'<path d="M{x + i*step:.1f},{y} V{y+H}"/>' for i in range(1, int(W/step) + 1))
    lines += "".join(f'<path d="M{x},{y + i*step:.1f} H{x+W}"/>' for i in range(1, int(H/step) + 1))
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{W}" height="{H}"/></clipPath>'
            f'<g clip-path="url(#{cid})" stroke="#fff" stroke-width="{step*0.03:.2f}" opacity="{op}">{lines}</g>')

def front(x, y, W, H, p):
    """Cara frontal minimalista: color de la línea, logo grande, una frase y el nombre en una pastilla."""
    k, name, line, claim, *_ = p
    c1, c2 = LINES[line]
    m = min(W, H)
    cx, cy = x + W / 2, y + H / 2
    s = [f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="url(#g{k})"/>', pattern(x, y, W, H, k),
         f'<circle cx="{x + W*0.88:.1f}" cy="{y + H*0.12:.1f}" r="{m*0.42:.1f}" fill="#fff" opacity=".12"/>',
         f'<circle cx="{x + W*0.08:.1f}" cy="{y + H*0.95:.1f}" r="{m*0.3:.1f}" fill="#FFC845" opacity=".35"/>']
    lw = min(W * 0.72, H * 2.2)
    lh = lw * 200 / 739
    fs = min(W * 0.075, H * 0.075)
    total = lh + fs * 2.2
    top = cy - total / 2 - fs * 0.4
    s.append(logo(cx - lw / 2, top, lw, white=True))
    t, _ = txt(cx, top + lh + fs * 1.5, claim, fs, W * 0.86, "#FFF8EE", 800, "middle"); s.append(t)
    ps = min(W * 0.04, H * 0.045)
    pw = min(W * 0.8, len(name) * ps * 0.62 + ps * 2)
    py = y + H - ps * 3.2
    s += [f'<rect x="{cx - pw/2:.1f}" y="{py:.1f}" width="{pw:.1f}" height="{ps*2:.1f}" rx="{ps:.1f}" fill="{INK}"/>',
          f'<text x="{cx:.1f}" y="{py + ps*1.35:.1f}" font-family="DM Sans, Arial" font-size="{ps:.1f}" font-weight="800" fill="#fff" text-anchor="middle" letter-spacing="{ps*0.08:.2f}">{e(name.upper())}</text>']
    return "".join(s)

def side(x, y, D_, H, p):
    s = [f'<rect x="{x}" y="{y}" width="{D_}" height="{H}" fill="{INK}"/>']
    h = min(D_ * 0.55, H * 0.3)
    s.append(iso(x + D_ / 2 - h * 0.33, y + H / 2 - h / 2, h, "#FF6B2C"))
    return "".join(s)

def back(x, y, W, H, p):
    """Trasera: logo, 3 pasos con icono y una sola palabra, y el bloque legal pequeño (obligatorio)."""
    k, name, line, *_ = p
    c1, _ = LINES[line]
    m = min(W, H); pad = m * 0.08
    s = [f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="{CREAM}"/>']
    lw = min(W * 0.5, H * 1.2)
    s.append(logo(x + W/2 - lw/2, y + pad, lw))
    r = min(W / 9, H * 0.11)
    cy = y + H * 0.5
    for i, word in enumerate(["Limpia", "Pega", "24 h"]):
        cx = x + W * (0.2 + 0.3 * i)
        s += [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{[ORANGE, c1, "#FFC845"][i]}"/>',
              f'<text x="{cx:.1f}" y="{cy + r*0.36:.1f}" font-family="DM Sans, Arial" font-size="{r:.1f}" font-weight="900" fill="#fff" text-anchor="middle">{i+1}</text>',
              f'<text x="{cx:.1f}" y="{cy + r*1.9:.1f}" font-family="DM Sans, Arial" font-size="{r*0.55:.1f}" font-weight="800" fill="{INK}" text-anchor="middle">{word}</text>']
    fs = min(W * 0.028, H * 0.03)
    t, _ = txt(x + W/2, y + H - pad - fs * 1.4, "[TITULAR] · [DIRECCIÓN] · javiempresa2026@gmail.com · Fabricado en [PAÍS] · Lote [__]", fs, W * 0.9, INK, 500, "middle"); s.append(t)
    return "".join(s)

def lid(x, y, W, D_, top, p):
    """Tapa con lengüeta. Arriba: «¡Hola!». Abajo: sin texto."""
    ly = y + TUCK if top else y
    ty = y if top else y + D_
    s = [f'<path d="M{x+3},{ty + (TUCK if top else 0)} L{x+3},{ty + (5 if top else TUCK-5)} Q{x+3},{ty if top else ty+TUCK} {x+10},{ty if top else ty+TUCK} L{x+W-10},{ty if top else ty+TUCK} Q{x+W-3},{ty if top else ty+TUCK} {x+W-3},{ty + (5 if top else TUCK-5)} L{x+W-3},{ty + (TUCK if top else 0)} Z" fill="{CREAM}" stroke="#E0245E" stroke-width="0.4"/>',
         f'<rect x="{x}" y="{ly}" width="{W}" height="{D_}" fill="{INK}"/>']
    if top and D_ >= 20:
        fs = min(D_ * 0.35, W * 0.12)
        s.append(f'<text x="{x + W/2:.1f}" y="{ly + D_/2 + fs*0.35:.1f}" font-family="DM Sans, Arial" font-size="{fs:.1f}" font-weight="900" fill="#FFC845" text-anchor="middle">¡Hola! 👋</text>')
    return "".join(s)

def dust(x, y, D_, up):
    h = D_ * 0.75
    if up: d = f"M{x},{y} L{x+2},{y-h+4} Q{x+3},{y-h} {x+8},{y-h} L{x+D_-2},{y-h*0.6} L{x+D_},{y} Z"
    else: d = f"M{x},{y} L{x+2},{y+h-4} Q{x+3},{y+h} {x+8},{y+h} L{x+D_-2},{y+h*0.6} L{x+D_},{y} Z"
    return f'<path d="{d}" fill="{CREAM}" stroke="#E0245E" stroke-width="0.4"/>'

def caja(p):
    k, name, line, *_, (W, D_, H) = p
    c1, c2 = LINES[line]
    top = D_ + TUCK; TW = GLUE + 2 * D_ + 2 * W; TH = H + 2 * top
    x0 = GLUE; xs = [x0, x0 + D_, x0 + D_ + W, x0 + 2 * D_ + W]  # lado, frente, lado, trasera
    y0 = top
    parts = [f'<defs><linearGradient id="g{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs>',
             f'<path d="M0,{y0+6} L{GLUE},{y0} L{GLUE},{y0+H} L0,{y0+H-6} Z" fill="#ddd" stroke="#E0245E" stroke-width="0.4"/>',
             side(xs[0], y0, D_, H, p), front(xs[1], y0, W, H, p), side(xs[2], y0, D_, H, p), back(xs[3], y0, W, H, p),
             lid(xs[1], 0, W, D_, True, p), lid(xs[3], y0 + H, W, D_, False, p),
             dust(xs[0], y0, D_, True), dust(xs[2], y0, D_, True), dust(xs[0], y0 + H, D_, False), dust(xs[2], y0 + H, D_, False)]
    # contorno de corte (rojo) y hendidos (azul discontinuo)
    folds = [(xs[0], y0, xs[0], y0 + H), (xs[1], y0, xs[1], y0 + H), (xs[2], y0, xs[2], y0 + H), (xs[3], y0, xs[3], y0 + H),
             (xs[0], y0, TW, y0), (xs[0], y0 + H, TW, y0 + H), (xs[1], TUCK, xs[1] + W, TUCK), (xs[3], y0 + H + D_, xs[3] + W, y0 + H + D_)]
    parts += [f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#2F6DB5" stroke-width="0.35" stroke-dasharray="2 1.5"/>' for a, b, c, d in folds]
    parts.append(f'<rect x="{xs[0]}" y="{y0}" width="{2*D_+2*W}" height="{H}" fill="none" stroke="#E0245E" stroke-width="0.4"/>')
    leg = f'<text x="{TW}" y="{TH + 9}" font-family="DM Sans, Arial" font-size="5" fill="#555" text-anchor="end">jarandana · {e(name)} · caja {W}×{D_}×{H} mm (ORIENTATIVA) · rojo = corte · azul = hendido</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 {TW + 8} {TH + 18}" width="{(TW+8)*S}" height="{(TH+18)*S}"><rect x="-4" y="-4" width="{TW+8}" height="{TH+18}" fill="#fff"/>{"".join(parts)}{leg}</svg>'

def front_only(p):
    """Solo la cara frontal, para mockups y para enviar al proveedor como referencia."""
    k, *_, (W, D_, H) = p
    c1, c2 = LINES[p[2]]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*S}" height="{H*S}"><defs><linearGradient id="g{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs>{front(0, 0, W, H, p)}</svg>'

def pegatina():
    r = 40
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="{80*S*2}" height="{80*S*2}">
<circle cx="40" cy="40" r="39.5" fill="{ORANGE}"/><circle cx="40" cy="40" r="34" fill="none" stroke="#fff" stroke-width="0.8" stroke-dasharray="2 1.6"/>
{iso(31, 12, 30, "#FFFFFF")}
<text x="40" y="56" font-family="DM Sans, Arial" font-size="7.5" font-weight="900" fill="#fff" text-anchor="middle">jarandana</text>
<text x="40" y="64" font-family="DM Sans, Arial" font-size="4.2" font-weight="700" fill="#fff" text-anchor="middle">Tu casa, sin taladrar.</text></svg>'''

def tarjeta():
    W, H = 148, 105  # A6 apaisado
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*S*2}" height="{H*S*2}">
<defs><linearGradient id="gt" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF9A3D"/><stop offset="1" stop-color="#FF4D6D"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="url(#gt)"/>{pattern(0, 0, W, H, "t")}
<circle cx="{W-10}" cy="12" r="34" fill="#fff" opacity=".12"/>
{logo(W/2 - 45, 22, 90, white=True)}
<text x="{W/2}" y="72" font-family="DM Sans, Arial" font-size="13" font-weight="900" fill="#fff" text-anchor="middle">¡Gracias! 🧡</text>
<text x="{W/2}" y="86" font-family="DM Sans, Arial" font-size="6" font-weight="700" fill="#FFF3C4" text-anchor="middle">Tu casa, sin taladrar.</text></svg>'''

if __name__ == "__main__":
    out = os.path.join(D, "cajas"); os.makedirs(out, exist_ok=True)
    fr = os.path.join(D, "frontales"); os.makedirs(fr, exist_ok=True)
    cards = []
    for p in PRODUCTOS:
        open(os.path.join(out, p[0] + ".svg"), "w").write(caja(p))
        open(os.path.join(fr, p[0] + ".svg"), "w").write(front_only(p))
        cards.append(f'<figure><img src="cajas/{p[0]}.svg" alt="Troquel {e(p[1])}"><figcaption><b>{e(p[1])}</b> · {p[6][0]}×{p[6][1]}×{p[6][2]} mm (orientativo) · <a href="cajas/{p[0]}.svg">SVG troquel</a> · <a href="frontales/{p[0]}.svg">cara frontal</a></figcaption></figure>')
    open(os.path.join(D, "pegatina.svg"), "w").write(pegatina())
    open(os.path.join(D, "tarjeta-gracias.svg"), "w").write(tarjeta())
    fronts = "".join(f'<img class="f" src="frontales/{p[0]}.svg" alt="{e(p[1])}">' for p in PRODUCTOS)
    open(os.path.join(D, "index.html"), "w").write(f'''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Packaging jarandana</title>
<style>body{{font-family:DM Sans,Arial,sans-serif;background:#F5EFE4;color:#1E2B37;margin:0;padding:24px}}h1,h2{{margin:.2em 0}}.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end}}.f{{height:220px;box-shadow:0 10px 30px rgba(0,0,0,.18);border-radius:4px}}figure{{background:#fff;border-radius:14px;padding:14px;margin:0 0 18px}}figure img{{width:100%;height:auto}}figcaption{{font-size:14px;margin-top:8px}}.sm{{height:200px}}</style>
<h1>Packaging jarandana</h1><p>Colores por línea: <b style="color:#0FA3A3">Baño</b> turquesa · <b style="color:#FF6B2C">Cocina</b> naranja · <b style="color:#E0245E">Novedad</b> rosa. Medidas orientativas: confírmalas con cada proveedor.</p>
<h2>Caras frontales</h2><div class="row">{fronts}</div>
<h2>Pegatina de cierre y tarjeta de gracias</h2><div class="row"><img class="sm" src="pegatina.svg" alt="Pegatina"><img class="sm" src="tarjeta-gracias.svg" alt="Tarjeta"></div>
<h2>Troqueles (caja de solapas)</h2>{"".join(cards)}</html>''')
    print("ok", len(PRODUCTOS), "cajas")

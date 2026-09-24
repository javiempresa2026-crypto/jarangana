"""Genera las plantillas JSON del tema jarandana (portada, producto, cabecera, pie y ajustes)."""
import json, copy, os
D = os.path.dirname(os.path.abspath(__file__))
IMG = {
 "hero": "EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMyMjE3MDM4NTY2MDQwMl81OGQ0MjJiNDI3Yjd.png",
 "freg": "EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMyMjE3MDM4ODY1ODUxNF8yN2QxMzY5OWZlYWU.png",
 "mamp": "EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMyMjE3MDM5MTMwNDcyNV80ZGMwMWI3MTVjNDg.png",
 "logo": "jarandana-logo_e8f6b256-fc48-4ece-baa4-2071c63c853a.png",
 "logo_w": "jarandana-logo-blanco.png",
 "ban_bano": "EMXN1y8qTwoGdXBsb2FkEg55bGFiLXN0dW50LXNncBo1c3RhcmdhdGUvMTEyL2JhNjgyOWZmLTQxYTMtNDk3Yy04OWJjLTE2YTkyNzQ2YzZlNy5wbmc.png",
 "ban_nov": "EMXN1y8qUAoGdXBsb2FkEg55bGFiLXN0dW50LXNncBo2c3RhcmdhdGUvMTE0LzUwOTU4ODdiLTY0MzQtNGI2OS1iNDA4LWY5OWQyMGYyNDYwNS5qcGVn.jpg",
 "fav": "jarandana-favicon_a8793dc6-68eb-457d-a479-ac7dcfbd5a9e.png",
}
VID = {  # vídeos Kling subidos a Shopify Archivos
 "hero": "https://cdn.shopify.com/s/files/1/1085/1552/4953/files/jarandana-portada.mp4?v=1790201076",
 "mamp": "https://cdn.shopify.com/s/files/1/1085/1552/4953/files/jarandana-mampara.mp4?v=1790201321",
 "intro": "https://cdn.shopify.com/s/files/1/1085/1552/4953/files/jarandana-intro.mp4",
 "freg": "https://cdn.shopify.com/s/files/1/1085/1552/4953/files/jarandana-fregadero.mp4?v=1790201505",
}
si = lambda k: "shopify://shop_images/" + IMG[k]

def sec(type_, settings, blocks=()):
    b = {f"b{i+1}": {"type": t, "settings": s} for i, (t, s) in enumerate(blocks)}
    return {"type": type_, "settings": settings, "blocks": b, "block_order": list(b)}

plist_base = json.load(open(os.path.join(D, "plist.json")))
def plist(coll, bg="#F5EFE4", n=8):
    s = copy.deepcopy(plist_base)
    s["settings"].update({"collection": coll, "max_products": n, "background_color": bg})
    s["blocks"]["static-header"]["blocks"]["product_list_button_MWeP9V"]["settings"]["label"] = "Ver todo"
    s["blocks"]["static-product-card"]["settings"]["border_radius"] = 14
    s["blocks"]["static-product-card"]["blocks"]["product_card_gallery_677WP3"]["settings"].update({"image_ratio": "square", "border_radius": 14})
    return s

BENEFITS = [
 ("item", {"icon": "drill", "title": "Cero agujeros", "text": "Se fija con adhesivo sobre azulejo, cristal o metal. Ni taladro ni tacos."}),
 ("item", {"icon": "home", "title": "Ideal si vives de alquiler", "text": "Al mudarte, lo despegas con un secador y te lo llevas."}),
 ("item", {"icon": "drop", "title": "Hecho para la ducha", "text": "Aluminio, acero inoxidable y silicona: materiales que no temen al agua."}),
 ("item", {"icon": "shield", "title": "Si llega roto, lo cambiamos", "text": "Mándanos una foto y te enviamos otro o te devolvemos el dinero."}),
]
STEPS = [
 ("step", {"title": "Limpia", "text": "Pasa alcohol por el azulejo y sécalo bien. Sin grasa ni restos de jabón."}),
 ("step", {"title": "Pega y presiona", "text": "Coloca el soporte y presiona con fuerza durante 30 segundos."}),
 ("step", {"title": "Espera 24 horas", "text": "Deja que el adhesivo agarre antes de mojarlo o cargarlo. Es el paso más importante."}),
]
STEPS_NOTE = "Solo superficies lisas: azulejo, cristal o metal. No apto para gotelé, pintura, madera sin lacar ni juntas."
FAQ = [
 ("¿De verdad no hay que taladrar?", "<p>No. Nuestras baldas y ganchos se fijan con adhesivo sobre superficies lisas: azulejo, cristal o metal.</p>"),
 ("¿En qué superficies NO funcionan?", "<p>Gotelé, pintura, madera sin lacar, papel pintado y juntas de azulejo. Necesitan una superficie lisa y no porosa.</p>"),
 ("¿Y si me mudo?", "<p>Calienta el adhesivo con un secador unos segundos y despega despacio. Para volver a colocarlo usa nuestro <a href=\"/products/recambio-adhesivos\">Recambio de Adhesivos</a>.</p>"),
 ("¿Cuánto tarda el envío?", "<p>El plazo estimado es de 7 a 15 días laborables. Te enviamos el número de seguimiento por email. Más info en <a href=\"/pages/envios\">Envíos</a>.</p>"),
 ("¿Puedo devolverlo?", "<p>Sí: tienes 14 días desde que lo recibes. Si llega roto o con un defecto, mándanos una foto y te enviamos otro o te devolvemos el dinero. Más info en <a href=\"/pages/devoluciones\">Devoluciones</a>.</p>"),
]
faq_blocks = [("qa", {"q": q, "a": a}) for q, a in FAQ]

OFFERS = [
 ("offer", {"color": "orange", "tag": "Automático", "big": "-15 %", "title": "En 5 favoritos de la casa",
   "text": "<p>Balda, Kit Fregadero, Grifo 1080°, Alcachofa 5 chorros y Dispensador de pasta. Sin código.</p>",
   "btn_label": "Ver las ofertas", "btn_link": "shopify://collections/ofertas"}),
 ("offer", {"color": "teal", "tag": "Pack x2", "big": "Ahorra 5,90 €", "title": "2 Grifos 1080° por 19,90 €",
   "text": "<p>En vez de 25,80 € comprando 2 sueltos. Uno para la cocina y otro para el baño.</p>",
   "btn_label": "Elegir el pack", "btn_link": "shopify://products/grifo-giratorio-1080"}),
 ("offer", {"color": "pink", "tag": "Pack x2", "big": "Ahorra 4,90 €", "title": "2 Luces LED por 44,90 €",
   "text": "<p>En vez de 49,80 € sueltas. Se encienden solas al pasar: pasillo, armario o escalera.</p>",
   "btn_label": "Elegir el pack", "btn_link": "shopify://products/luz-led-sensor-movimiento"}),
 ("offer", {"color": "sun", "tag": "Primer pedido", "big": "-10 %", "title": "Bienvenida a jarandana",
   "text": "<p>En pedidos desde 25 €. Copia el código y pégalo al pagar.</p>", "code": "BIENVENIDA10", "btn_label": ""}),
]
WORDS = ["Sin taladro.", "Sin obras.", "Sin cal.", "Sin agujeros.", "Te lo llevas.", "Listo en 1 minuto."]
index = {"sections": {
 "intro": sec("jd-intro", {"video_url": VID["intro"] or VID["hero"], "poster": si("hero"), "seconds": 2,
   "pre": "Tu baño y tu cocina, por fin en orden",
   "sub": "Baldas, rasquetas y ganchos que se pegan al azulejo. Sin herramientas, sin obras y sin pedir permiso al casero.",
   "btn_label": "Comprar ahora", "btn_link": "shopify://collections/todo-jarandana", "btn2_label": "Cómo se instala"},
   [("word", {"word": w}) for w in WORDS]),
 "hero": sec("jd-hero", {"bg": "pop", "eyebrow": "Baño y cocina sin taladrar", "heading": "Tu casa, sin taladrar.",
   "text": "<p>Baldas, rasquetas y ganchos que se pegan al azulejo, aguantan la ducha y se vienen contigo cuando te mudas.</p>",
   "btn1_label": "Ver el Kit Ducha", "btn1_link": "shopify://products/kit-ducha-sin-cal",
   "btn2_label": "Ver todos los productos", "btn2_link": "shopify://collections/todo-jarandana",
   "image": si("hero"), "badge": "Sin agujeros · Sin obras"},
   [("chip", {"icon": "drill", "text": "Sin taladro"}), ("chip", {"icon": "truck", "text": "Envío con seguimiento"}),
    ("chip", {"icon": "return", "text": "14 días para devolver"}), ("chip", {"icon": "lock", "text": "Pago seguro"})]),
 "benefits": sec("jd-benefits", {"bg": "orange", "eyebrow": "Por qué jarandana", "heading": "Orden en casa, sin pedir permiso al casero"}, BENEFITS),
 "list_ducha": plist("ducha", "#F5EFE4"),
 "feat_rasqueta": sec("jd-feature", {"bg": "white", "reverse": False, "image": si("mamp"), "video_url": VID["mamp"], "eyebrow": "Adiós a las marcas de cal",
   "heading": "Mampara limpia en 20 segundos", "text": "<p>La cal aparece cuando el agua se seca sobre el cristal. Pasa la rasqueta al salir de la ducha y listo.</p>",
   "product": "rasqueta-mampara-silicona", "btn_label": "Ver la Rasqueta"},
   [("point", {"text": "Hoja de silicona que no raya el cristal"}), ("point", {"text": "Con soporte adhesivo para colgarla en la ducha"}), ("point", {"text": "Sin productos químicos"})]),
 "feat_fregadero": sec("jd-feature", {"bg": "sun", "reverse": True, "image": si("freg"), "video_url": VID["freg"], "eyebrow": "Cocina",
   "heading": "El fregadero, por fin en orden", "text": "<p>Dispensador de jabón de un toque y esponjero que deja escurrir el agua.</p>",
   "product": "kit-fregadero-dispensador-esponjero", "btn_label": "Ver el Kit Fregadero"},
   [("point", {"text": "Jabón con una sola mano"}), ("point", {"text": "La esponja se seca y no vive en un charco"}), ("point", {"text": "Ocupa muy poco espacio"})]),
 "steps": sec("jd-steps", {"bg": "teal", "eyebrow": "Cómo se instala", "heading": "Listo en 1 minuto. Sin herramientas.", "note": STEPS_NOTE}, STEPS),
 "list_todo": plist("todo-jarandana", "#FFFFFF", 12),
 "list_nov": plist("novedades", "#FFE9D6", 4),
 "reviews": sec("jd-reviews", {"bg": "pop", "filter_product": True}),
 "payments": sec("jd-payments", {"bg": "white", "heading": "Pago 100 % seguro y cifrado", "text": "Compra con total tranquilidad: el pago lo procesa Shopify y tus datos de tarjeta nunca pasan por nosotros."}),
 "offers": sec("jd-offers", {"bg": "pop", "eyebrow": "Ofertas especiales", "heading": "Ahorra hoy en baño y cocina",
   "text": "<p>Descuentos reales sobre nuestros precios de siempre. Se aplican solos en el carrito.</p>",
   "note": "Los descuentos no se suman entre sí: en el carrito se aplica el mejor para ti. Packs calculados sobre el precio de 1 unidad."}, OFFERS),
 "list_ofertas": plist("ofertas", "#FFFFFF", 5),
 "banner_nov": sec("jd-banner", {"bg": "orange", "image": si("ban_nov"), "align": "left", "eyebrow": "Novedades", "heading": "Ideas que te hacen la vida más fácil", "text": "<p>Grifo giratorio 1080°, luz que se enciende sola, ducha de 5 chorros y dispensador de pasta. Todo sin obras.</p>", "btn_label": "Descubrir novedades", "btn_link": "shopify://collections/novedades"}),
 "banner_bano": sec("jd-banner", {"bg": "teal", "image": si("ban_bano"), "align": "right", "eyebrow": "Baño sin agujeros", "heading": "Tu ducha, ordenada en 1 minuto", "text": "<p>Balda, esquinera, rasqueta y ganchos que se pegan al azulejo. Sin taladro, sin obras.</p>", "btn_label": "Ver todo para el baño", "btn_link": "shopify://collections/ducha"}),
 "faq": sec("jd-faq", {"bg": "white", "open_first": True, "link_label": "Ver todas las preguntas", "link": "shopify://pages/preguntas-frecuentes"}, faq_blocks),
 "contact": sec("jd-contact", {}),
}, "order": ["intro", "offers", "list_ofertas", "banner_nov", "list_nov", "hero", "benefits", "banner_bano", "list_ducha", "feat_rasqueta", "feat_fregadero", "steps", "list_todo", "reviews", "payments", "faq", "contact"]}

# --- producto: se parte del original de Horizon
prod = json.load(open(os.path.join(D, "product.orig.json")))
m = prod["sections"]["main"]
m["blocks"].pop("disclosures_g9mWze", None); m["block_order"] = []
m["settings"]["background_color"] = "#F5EFE4"
pd = m["blocks"]["product-details"]["blocks"]
pd["buy_buttons_eYQEYi"]["blocks"]["add-to-cart"]["settings"].update({"style_class": "button"})
pd["variant_picker_R3rGDr"]["settings"]["show_swatches"] = False
rec = prod["sections"]["product_recommendations_qggXJq"]
rec["blocks"]["text_cbcgyb"]["settings"]["text"] = "<h3>Combina con</h3>"
rec["settings"]["background_color"] = "#FFFFFF"
prod["sections"].update({
 "p_benefits": sec("jd-benefits", {"bg": "orange"}, [
   ("item", {"icon": "drill", "title": "Sin taladro", "text": "Adhesivo para azulejo, cristal o metal."}),
   ("item", {"icon": "truck", "title": "Envío con seguimiento", "text": "Entrega estimada en 7-15 días laborables."}),
   ("item", {"icon": "return", "title": "14 días para devolver", "text": "Sin dar explicaciones, si no está instalado."}),
   ("item", {"icon": "lock", "title": "Pago seguro", "text": "Tarjeta y métodos protegidos por Shopify."})]),
 "p_video": sec("jd-video", {"bg": "white", "eyebrow": "En casa", "heading": "Así queda, sin un solo agujero", "text": "<p>Se instala en un minuto y se quita con un secador cuando te mudas.</p>", "note": "Vídeo ilustrativo generado con IA."}),
 "p_steps": sec("jd-steps", {"bg": "teal", "eyebrow": "Cómo se instala", "heading": "3 pasos, 1 minuto", "note": STEPS_NOTE}, STEPS),
 "p_reviews": sec("jd-reviews", {"bg": "pop", "filter_product": True}),
 "p_pay": sec("jd-payments", {"bg": "white", "heading": "Pago 100 % seguro y cifrado", "text": "Envío con seguimiento · 14 días para devolver · Si llega roto, te enviamos otro."}),
 "p_offers": sec("jd-offers", {"bg": "pop", "eyebrow": "Ofertas especiales", "heading": "Ahorra en tu pedido", "note": "Los descuentos no se suman entre sí: en el carrito se aplica el mejor para ti."}, OFFERS),
 "p_faq": sec("jd-faq", {"bg": "cream", "open_first": False, "link_label": "Ver todas las preguntas", "link": "shopify://pages/preguntas-frecuentes"}, faq_blocks),
})
prod["order"] = ["main", "p_pay", "p_video", "p_benefits", "p_steps", "p_reviews", "p_offers", "p_faq", "product_recommendations_qggXJq"]

# --- cabecera
hg = json.load(open(os.path.join(D, "header-group.orig.json")))
ann = hg["sections"]["header_announcements_9jGBFp"]
ann["blocks"]["announcement_BxgCk9"]["settings"]["text"] = "Sin taladro, sin obras · Envío con seguimiento a península y Baleares"
ann["blocks"]["announcement_BxgCk9"]["settings"]["font_size"] = "0.8125rem"
ann["blocks"]["announcement_ofertas"] = copy.deepcopy(ann["blocks"]["announcement_BxgCk9"])
ann["blocks"]["announcement_ofertas"]["settings"]["text"] = "Ofertas especiales: -15 % en 5 favoritos, se aplica solo en el carrito"
ann["block_order"] = ["announcement_ofertas", "announcement_BxgCk9"]
ann["settings"].update({"background_color": "#1E2B37", "divider_width": 0, "padding-block-start": 10, "padding-block-end": 10})
hs = hg["sections"]["header_section"]["settings"]
hs.update({"show_country": False, "show_language": False, "background_color_top": "#F5EFE4"})

# --- pie
fg = json.load(open(os.path.join(D, "footer-group.orig.json")))
f = fg["sections"]["footer_m9NzUG"]
g = f["blocks"]["group_H6VpwJ"]["blocks"]
g["text_LWt8Pz"]["settings"]["text"] = "<h2>Únete a jarandana</h2>"
g["text_f9CFLH"]["settings"]["text"] = "<p>Trucos de orden y limpieza, y novedades. Sin spam: puedes darte de baja cuando quieras.</p>"
f["blocks"]["email_signup_crihX7"]["settings"]["label"] = "Suscribirme"
f["blocks"]["menu_shop"] = {"type": "menu", "settings": {"menu": "main-menu", "heading": "Tienda", "menu_spacing": 10, "heading_preset": "h5", "link_preset": "paragraph"}}
f["blocks"]["menu_help"] = {"type": "menu", "settings": {"menu": "footer", "heading": "Ayuda", "menu_spacing": 10, "heading_preset": "h5", "link_preset": "paragraph"}}
f["block_order"] = ["group_H6VpwJ", "menu_shop", "menu_help", "email_signup_crihX7"]
f["settings"].update({"background_color": "#EADFCB", "padding-block-start": 48, "padding-block-end": 36})
u = fg["sections"]["footer_utilities_jLGE8U"]
u["blocks"].pop("social_links_Ew63Kq", None)
u["block_order"] = ["footer_copyright_jweRK8", "footer_policy_list_VCdnpa"]
u["blocks"]["footer_copyright_jweRK8"]["settings"]["show_powered_by"] = False
u["settings"]["background_color"] = "#EADFCB"

# --- ajustes globales
st = json.load(open(os.path.join(D, "settings_data.json")))
st["current"].update({"palette_primary_button_background": "#FF6B2C", "palette_primary_button_border": "#FF6B2C", "badge_sale_background_color": "#FF4D6D", "logo": si("logo"), "logo_inverse": si("logo_w"), "favicon": si("fav"), "logo_height": 44, "logo_height_mobile": 34})

out = {"templates/index.json": index, "templates/product.json": prod, "sections/header-group.json": hg,
       "sections/footer-group.json": fg, "config/settings_data.json": st}
os.makedirs(os.path.join(D, "build"), exist_ok=True)
for k, v in out.items():
    p = os.path.join(D, "build", k); os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(v, open(p, "w"), ensure_ascii=False, indent=2)
    print(k, len(json.dumps(v, ensure_ascii=False)))

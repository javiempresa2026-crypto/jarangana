"""Plantillas secundarias de Horizon traducidas al español (404, carrito, colecciones, contacto)."""
import json, copy, os
D = os.path.dirname(os.path.abspath(__file__))
Z = {"padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}
BG = "{{ settings.color_palette.background }}"
def txt(text, preset, align="left", width="100%", **kw):
    s = {"text": text, "width": width, "max_width": "normal", "alignment": align, "type_preset": preset, "font": "var(--font-body--family)",
         "line_height": "normal", "letter_spacing": "normal", "case": "none", "wrap": "pretty", "background": False,
         "background_color": "#00000026", "corner_radius": 0, **Z}
    s.update(kw); return s
plist_base = json.load(open(os.path.join(D, "plist.json")))
def plist(title, label=None, coll="todo-jarandana", n=4):
    s = copy.deepcopy(plist_base)
    s["settings"].update({"collection": coll, "max_products": n, "background_color": BG})
    h = s["blocks"]["static-header"]["blocks"]
    h["product_list_text_YFtzcL"]["settings"]["text"] = f"<h3>{title}</h3>"
    if label: h["product_list_button_MWeP9V"]["settings"]["label"] = label
    else:
        del h["product_list_button_MWeP9V"]; s["blocks"]["static-header"]["block_order"] = ["product_list_text_YFtzcL"]
    return s

t404 = {"sections": {
 "main": {"type": "main-404", "blocks": {
   "t1": {"type": "text", "settings": txt("<h1>Esta página no existe</h1>", "h3", "center"), "blocks": {}},
   "t2": {"type": "text", "settings": txt("<p>Puede que el enlace esté mal escrito o que la página se haya movido.</p>", "rte", "center", **{"padding-block-end": 16}), "blocks": {}},
   "b1": {"type": "button", "settings": {"label": "Ver todos los productos", "link": "shopify://collections/todo-jarandana", "open_in_new_tab": False, "style_class": "button", "width": "fit-content", "custom_width": 100, "width_mobile": "fit-content", "custom_width_mobile": 100}, "blocks": {}}},
   "block_order": ["t1", "t2", "b1"],
   "settings": {"content_direction": "column", "section_width": "page-width", "section_height": "small", "horizontal_alignment_flex_direction_column": "center", "vertical_alignment_flex_direction_column": "center", "gap": 20, "background_color": BG, "padding-block-start": 100, "padding-block-end": 100}},
 "list": plist("Descubre jarandana")},
 "order": ["main", "list"]}

cart = {"sections": {
 "cart-section": {"type": "main-cart", "blocks": {
   "cart-page-title": {"type": "_cart-title", "static": True, "settings": {"title": "Tu carrito", "show_count": True, "type_preset": "h4", "alignment": "left", **Z}, "blocks": {}},
   "cart-page-items": {"type": "_cart-products", "static": True, "settings": {"gap": 24, "image_ratio": "square", "dividers": True, "vendor": False, **Z}, "blocks": {}},
   "cart-page-summary": {"type": "_cart-summary", "static": True, "settings": {"extend_summary": True, "background_color": "#EADFCB", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 14}, "blocks": {}}},
   "settings": {"section_width": "page-width", "background_color": BG, "padding-block-start": 24, "padding-block-end": 0}},
 "list": plist("Completa tu pedido", "Ver todo")},
 "order": ["cart-section", "list"]}

lc = {"sections": {"collection_list_Wfgh3m": {"type": "main-collection-list", "blocks": {
   "group_4FtiAg": {"type": "group", "settings": {"content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start", "vertical_alignment": "center", "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start", "vertical_alignment_flex_direction_column": "center", "gap": 12, "width": "fit-content", "custom_width": 100, "width_mobile": "fit-content", "custom_width_mobile": 100, "height": "fit", "custom_height": 100, "background_media": "none", "video_position": "cover", "background_image_position": "cover", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0, "toggle_overlay": False, "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top", "open_in_new_tab": False, "padding-block-start": 0, "padding-block-end": 48, "padding-inline-start": 0, "padding-inline-end": 0},
     "blocks": {"text_fRMQMR": {"type": "text", "settings": txt("<h1>Colecciones</h1>", "h2", **{"padding-block-end": 16}), "blocks": {}}}, "block_order": ["text_fRMQMR"]},
   "static-collection-card": {"type": "_collection-card", "static": True, "settings": {"placement": "below_image", "horizontal_alignment": "flex-start", "vertical_alignment": "flex-start", "collection_card_gap": 8, "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 14},
     "blocks": {"collection_title_7YgBPU": {"type": "collection-title", "settings": {**txt("", "rte", width="fit-content", font_size="1rem")}, "blocks": {}},
                "collection-card-image": {"type": "_collection-card-image", "static": True, "settings": {"image_ratio": "square", "toggle_overlay": False, "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 14}, "blocks": {}}},
     "block_order": ["collection_title_7YgBPU"]}},
   "block_order": ["group_4FtiAg"],
   "settings": {"layout_type": "grid", "carousel_on_mobile": False, "columns": 3, "mobile_columns": "2", "columns_gap": 12, "bento_gap": 8, "rows_gap": 24, "max_collections": 4, "icons_style": "arrow", "icons_shape": "none", "section_width": "page-width", "gap": 12, "background_color": BG, "padding-block-start": 48, "padding-block-end": 48}}},
 "order": ["collection_list_Wfgh3m"]}
del lc["sections"]["collection_list_Wfgh3m"]["blocks"]["static-collection-card"]["blocks"]["collection_title_7YgBPU"]["settings"]["text"]

contact = {"sections": {
 "main": {"type": "jd-pagehero", "settings": {"bg": "sun", "emoji": "💬", "sticker": "Respondemos en 24 h", "heading": "¿Hablamos? [Escríbenos]", "eyebrow": "Contacto", "text": "<p>¿Dudas antes de comprar o sobre tu pedido? Rellena el formulario y te contestamos en 24 horas laborables. Si ya has comprado, pon tu número de pedido.</p>"},
   "blocks": {"c1": {"type": "chip", "settings": {"icon": "mail", "text": "Respuesta en 24 h"}}, "c2": {"type": "chip", "settings": {"icon": "return", "text": "14 días para devolver"}}, "c3": {"type": "chip", "settings": {"icon": "shield", "text": "Si llega roto, otro nuevo"}}}, "block_order": ["c1", "c2", "c3"]},
 "form": {"type": "section", "blocks": {"contact_form_UwiCkQ": {"type": "contact-form", "settings": {"width": "custom", "custom_width": 50, "width_mobile": "custom", "custom_width_mobile": 100, "input_style": "default", **Z},
     "blocks": {"submit-button": {"type": "contact-form-submit-button", "static": True, "settings": {"label": "Enviar mensaje", "style_class": "button", "width": "fit-content", "custom_width": 100, "width_mobile": "fit-content", "custom_width_mobile": 100}, "blocks": {}}}, "block_order": []}},
   "block_order": ["contact_form_UwiCkQ"],
   "settings": {"content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start", "vertical_alignment": "center", "align_baseline": False, "horizontal_alignment_flex_direction_column": "center", "vertical_alignment_flex_direction_column": "center", "gap": 32, "section_width": "page-width", "section_height_custom": 50, "background_media": "none", "background_color": "#FFF8EE", "video_position": "cover", "background_image_position": "cover", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0, "toggle_overlay": False, "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top", "padding-block-start": 40, "padding-block-end": 56}},
 "contact": {"type": "jd-contact", "settings": {"eyebrow": "Otras formas de contactar", "heading": "Estamos aquí para ayudarte", "text": "<p>Escríbenos con tu número de pedido si ya has comprado. Si aún no, cuéntanos qué quieres colgar y dónde.</p>"}, "blocks": {}, "block_order": []}},
 "order": ["main", "form", "contact"]}

out = {"templates/404.json": t404, "templates/cart.json": cart, "templates/list-collections.json": lc, "templates/page.contact.json": contact}
payload = {"themeId": "gid://shopify/OnlineStoreTheme/207150252377", "files": []}
for k, v in out.items():
    p = os.path.join(D, "build", k); os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(v, open(p, "w"), ensure_ascii=False, indent=2)
    payload["files"].append({"filename": k, "body": {"type": "TEXT", "value": json.dumps(v, ensure_ascii=True)}})
print(json.dumps(payload, ensure_ascii=True))

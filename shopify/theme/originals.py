"""Plantillas originales de Horizon (tema duplicado) que build.py modifica."""
import json
Z = {"padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}
def txt(text, preset, width="100%", **kw):
    s = {"text": text, "width": width, "max_width": "normal", "alignment": "left", "type_preset": preset, "font": "var(--font-body--family)",
         "font_size": "1rem", "line_height": "normal", "letter_spacing": "normal", "case": "none", "wrap": "pretty", "text_color": "",
         "background": False, "background_color": "#00000026", "corner_radius": 0, **Z}
    s.update(kw); return s
def price(preset, **kw):
    s = {"show_sale_price_first": True, "show_installments": False, "show_tax_info": False, "type_preset": preset, "width": "100%", "alignment": "left",
         "font": "var(--font-body--family)", "font_size": "1rem", "line_height": "normal", "letter_spacing": "normal", "case": "none", "text_color": "", **Z}
    s.update(kw); return s
BOX = {"border": "none", "border_width": 1, "border_opacity": 100, "border_color": "", "border_radius": 0}
FG, BG, C2 = "{{ settings.color_palette.foreground }}", "{{ settings.color_palette.background }}", "{{ settings.color_palette.color2 }}"

product = {"sections": {
 "main": {"type": "product-information", "blocks": {
   "disclosures_g9mWze": {"type": "disclosures", "name": "t:names.disclosures", "settings": {"heading": "Disclosures", "heading_preset": "h5", "open_by_default": False, "icon": "caret", "disclosure_heading_preset": "h6", "text_color": "", "dividers": True, "divider_color": C2, **Z}, "blocks": {}},
   "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {"media_presentation": "grid", "media_columns": "two", "image_gap": 4, "large_first_image": False, "slideshow_controls_style": "counter", "slideshow_mobile_controls_style": "dots", "thumbnail_position": "right", "thumbnail_width": 44, "thumbnail_radius": 0, "aspect_ratio": "adapt", "constrain_to_viewport": True, "media_fit": "contain", "media_radius": 0, "extend_media": False, "zoom": True, "video_loop": False, "hide_variants": True, **Z}, "blocks": {}},
   "product-details": {"type": "_product-details", "static": True, "settings": {"width": "fill", "custom_width": 100, "width_mobile": "fill", "custom_width_mobile": 100, "height": "fit", "details_position": "flex-start", "gap": 28, "sticky_details_desktop": True, "background_media": "none", "background_color": "", "video_position": "cover", "background_image_position": "cover", **BOX, "padding-block-start": 24, "padding-block-end": 24, "padding-inline-start": 0, "padding-inline-end": 0},
     "blocks": {
       "group_icgrde": {"type": "group", "name": "t:names.header", "settings": {"content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start", "vertical_alignment": "center", "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start", "vertical_alignment_flex_direction_column": "center", "gap": 12, "width": "fill", "custom_width": 100, "width_mobile": "fill", "custom_width_mobile": 100, "height": "fit", "custom_height": 100, "background_media": "none", "background_color": "", "video_position": "cover", "background_image_position": "cover", "toggle_overlay": False, "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top", **BOX, "open_in_new_tab": False, "placeholder": "", **Z},
         "blocks": {
           "text_xrnftG": {"type": "text", "name": "t:names.product_title", "settings": txt("<h1>{{ closest.product.title }}</h1>", "h3"), "blocks": {}},
           "price_tVjtKg": {"type": "price", "settings": price("paragraph", **{"padding-block-start": 4}), "blocks": {}}},
         "block_order": ["text_xrnftG", "price_tVjtKg"]},
       "divider_VJhene": {"type": "_divider", "name": "t:names.divider", "settings": {"thickness": 1, "corner_radius": "square", "divider_color": C2, "width_percent": 100, "padding-block-start": 0, "padding-block-end": 0}, "blocks": {}},
       "variant_picker_R3rGDr": {"type": "variant-picker", "settings": {"variant_style": "buttons", "show_swatches": False, "option_label_text_color": "", "variant_style_class": "default", "custom_variant_background": BG, "custom_variant_text": FG, "custom_variant_border": FG, "selected_variant_style_class": "default", "custom_selected_variant_background": FG, "custom_selected_variant_text": BG, "custom_selected_variant_border": FG, "alignment": "left", **Z}, "blocks": {}},
       "buy_buttons_eYQEYi": {"type": "buy-buttons", "settings": {"stacking": True, "text_color": "", "show_pickup_availability": False, "gift_card_form": True, "recipient_button_style": "default", "recipient_button_background": BG, "recipient_button_text": FG, "recipient_button_border": FG, "selected_recipient_button_style": "default", "selected_recipient_button_background": FG, "selected_recipient_button_text": BG, "selected_recipient_button_border": FG, "input_style": "default", "input_background_color": BG, "input_text_color": FG, "input_border_color": FG, "border_width": 1, "border_radius": 0, **Z},
         "blocks": {
           "quantity": {"type": "quantity", "static": True, "settings": {"input_style": "default", "input_background_color": BG, "input_text_color": FG, "input_border_color": FG, "border_width": 1, "border_radius": 0}, "blocks": {}},
           "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {"style_class": "button", "custom_button_background": FG, "custom_button_text": BG, "custom_button_border": BG}, "blocks": {}},
           "accelerated-checkout": {"type": "accelerated-checkout", "static": True, "settings": {}, "blocks": {}}},
         "block_order": []},
       "text_aEtTtq": {"type": "text", "name": "t:names.product_description", "settings": txt("{{ closest.product.description }}", "rte"), "blocks": {}}},
     "block_order": ["group_icgrde", "divider_VJhene", "variant_picker_R3rGDr", "buy_buttons_eYQEYi", "text_aEtTtq"]}},
   "block_order": ["disclosures_g9mWze"],
   "settings": {"content_width": "content-center-aligned", "desktop_media_position": "left", "equal_columns": False, "limit_details_width": False, "gap": 48, "enable_sticky_add_to_cart": True, "background_color": BG, "padding-block-start": 0, "padding-block-end": 0}},
 "product_recommendations_qggXJq": {"type": "product-recommendations", "blocks": {
   "text_cbcgyb": {"type": "text", "name": "t:names.header", "settings": txt("<h3>You may also like </h3>", "h4", width="fit-content"), "blocks": {}},
   "static-product-card": {"type": "_product-card", "name": "t:names.product_card", "static": True, "settings": {"product_card_gap": 8, "background_color": "", **BOX, "padding-block-start": 0, "padding-block-end": 8, "padding-inline-start": 0, "padding-inline-end": 0},
     "blocks": {
       "product_card_gallery_DNizbJ": {"type": "_product-card-gallery", "name": "t:names.product_card_media", "settings": {"image_ratio": "adapt", **BOX, **Z}, "blocks": {}},
       "product_title_M7MJkb": {"type": "product-title", "name": "t:names.product_title", "settings": txt("", "rte", **{"padding-block-start": 4}), "blocks": {}},
       "price_gLWgA6": {"type": "price", "settings": price("h6"), "blocks": {}}},
     "block_order": ["product_card_gallery_DNizbJ", "product_title_M7MJkb", "price_gLWgA6"]}},
   "block_order": ["text_cbcgyb"], "name": "t:names.product_recommendations",
   "settings": {"product": "{{ closest.product }}", "recommendation_type": "related", "layout_type": "grid", "carousel_on_mobile": False, "max_products": 4, "columns": 4, "mobile_columns": "2", "columns_gap": 12, "rows_gap": 24, "icons_style": "arrow", "icons_shape": "none", "section_width": "page-width", "gap": 28, "background_color": BG, "padding-block-start": 48, "padding-block-end": 48}}},
 "order": ["main", "product_recommendations_qggXJq"]}
# product-title no lleva "text" en el original
del product["sections"]["product_recommendations_qggXJq"]["blocks"]["static-product-card"]["blocks"]["product_title_M7MJkb"]["settings"]["text"]

header = {"type": "header", "name": "t:names.header", "sections": {
 "header_announcements_9jGBFp": {"type": "header-announcements", "blocks": {"announcement_BxgCk9": {"type": "_announcement", "settings": {"text": "Welcome to our store", "font": "var(--font-subheading--family)", "font_size": "0.75rem", "letter_spacing": "normal", "case": "none"}, "blocks": {}}},
   "block_order": ["announcement_BxgCk9"], "name": "t:names.announcement_bar", "settings": {"speed": 5, "section_width": "page-width", "background_color": BG, "divider_width": 1, "divider_color": C2, "padding-block-start": 15, "padding-block-end": 15}},
 "header_section": {"type": "header", "blocks": {
   "header-logo": {"type": "_header-logo", "static": True, "settings": {"hide_logo_on_home_page": False, "padding-block-start": 0, "padding-block-end": 0}, "blocks": {}},
   "header-menu": {"type": "_header-menu", "static": True, "settings": {"menu": "main-menu", "type_font_primary_size": "0.875rem", "menu_font_style": "inverse", "type_font_primary_link": "body", "type_case_primary_link": "none", "menu_style": "featured_products", "featured_products_aspect_ratio": "4 / 5", "featured_collections_aspect_ratio": "16 / 9", "image_border_radius": 0, "navigation_bar": False, "drawer_accordion": False, "drawer_accordion_expand_first": False, "drawer_dividers": False}, "blocks": {}}},
   "settings": {"logo_position": "left", "menu_position": "left", "menu_row": "top", "show_search": True, "search_position": "right", "search_row": "top", "show_country": True, "country_selector_style": False, "show_language": True, "localization_font": "heading", "localization_font_size": "0.875rem", "localization_position": "right", "localization_row": "top", "section_width": "page-width", "section_height": "standard", "enable_sticky_header": "always", "divider_width": 0, "divider_size": "page-width", "border_width": 0, "background_color_top": BG, "enable_transparent_header_home": False, "enable_transparent_header_product": False, "enable_transparent_header_collection": False}}},
 "order": ["header_announcements_9jGBFp", "header_section"]}

def ftxt(text, preset):
    s = txt(text, preset); s.pop("text_color"); return s
footer = {"type": "footer", "name": "t:names.footer", "sections": {
 "footer_m9NzUG": {"type": "footer", "blocks": {
   "group_H6VpwJ": {"type": "group", "settings": {"content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start", "vertical_alignment": "center", "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start", "vertical_alignment_flex_direction_column": "center", "gap": 6, "width": "fill", "custom_width": 100, "width_mobile": "fill", "custom_width_mobile": 100, "height": "fit", "custom_height": 100, "background_media": "none", "video_position": "cover", "background_image_position": "cover", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0, "toggle_overlay": False, "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top", "open_in_new_tab": False, **Z},
     "blocks": {"text_LWt8Pz": {"type": "text", "settings": ftxt("<h2>Join our email list</h2>", "h4"), "blocks": {}},
                "text_f9CFLH": {"type": "text", "settings": ftxt("<p>Get exclusive deals and early access to new products.</p>", "rte"), "blocks": {}}},
     "block_order": ["text_LWt8Pz", "text_f9CFLH"]},
   "email_signup_crihX7": {"type": "email-signup", "settings": {"width": "fill", "custom_width": 100, "heading_preset": "h3", "border_style": "all", "input_style": "custom", "border_width": 1, "border_radius": 100, "input_background_color": BG, "input_text_color": "{{ settings.color_palette.color1 }}", "input_border_color": C2, "input_type_preset": "paragraph", "style_class": "button-unstyled", "display_type": "arrow", "label": "Sign up", "integrated_button": True, "button_type_preset": "paragraph", **Z}, "blocks": {}}},
   "block_order": ["group_H6VpwJ", "email_signup_crihX7"], "name": "t:names.footer", "settings": {"section_width": "page-width", "gap": 20, "background_color": BG, "padding-block-start": 30, "padding-block-end": 30}},
 "footer_utilities_jLGE8U": {"type": "footer-utilities", "blocks": {
   "footer_copyright_jweRK8": {"type": "footer-copyright", "settings": {"show_powered_by": True, "font_size": "0.75rem", "case": "none"}, "blocks": {}},
   "footer_policy_list_VCdnpa": {"type": "footer-policy-list", "settings": {"font_size": "0.75rem", "case": "none"}, "blocks": {}},
   "social_links_Ew63Kq": {"type": "social-links", "settings": {}, "blocks": {}}},
   "block_order": ["footer_copyright_jweRK8", "footer_policy_list_VCdnpa", "social_links_Ew63Kq"], "name": "t:names.utilities",
   "settings": {"section_width": "page-width", "gap": 24, "divider_thickness": 1, "divider_color": C2, "background_color": BG, "padding-block-start": 20, "padding-block-end": 48}}},
 "order": ["footer_m9NzUG", "footer_utilities_jLGE8U"]}

for n, d in [("product.orig.json", product), ("header-group.orig.json", header), ("footer-group.orig.json", footer)]:
    json.dump(d, open(n, "w"), ensure_ascii=False, indent=2)

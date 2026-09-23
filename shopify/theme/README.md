# Tema jarandana (sobre Horizon)

Personalización del tema **"jarandana"** (copia de Horizon) de jarandana.myshopify.com. Se sube con `themeFilesUpsert` de la Admin API.

- `sections/jd-*.liquid`: secciones propias, adaptadas a móvil y editables desde el editor de temas.
  - `jd-hero`: portada.
  - `jd-benefits`: ventajas.
  - `jd-steps`: cómo se instala.
  - `jd-feature`: producto destacado.
  - `jd-reviews`: reseñas.
  - `jd-faq`: preguntas frecuentes.
  - `jd-contact`: contacto.
- `assets/jarandana.css`: estilos de marca (crema `#F5EFE4`, tinta `#1E2B37`, naranja `#E4702E`).
- `snippets/jd-icon.liquid`: iconos SVG.
- `build.py`: genera `build/` (portada, ficha de producto, cabecera, pie y ajustes con el logo). Parte de `originals.py` (las plantillas originales de Horizon) y de `plist.json`.

## Reseñas
Las reseñas son **reales**:
1. El cliente envía el formulario "Escribir una reseña" y te llega por email.
2. Tú la creas en **Contenido → Metaobjetos → Reseña**, con nombre, ciudad, valoración 1-5, texto, producto, fecha y "Compra verificada".
3. Solo se muestran las que están en estado **Activo**.

No publiques reseñas inventadas: la Directiva Ómnibus las prohíbe.

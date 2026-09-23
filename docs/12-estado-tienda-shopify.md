# 12 · Estado de la tienda Shopify (23-09-2026)

Tienda: **jarandana.myshopify.com** (EUR, plan Basic).

## Hecho
- **8 productos ACTIVOS** y publicados en Tienda online y Shop: Balda, Rasqueta, Ganchos, Kit Fregadero, Esquinera Doble, Bayetas, Recambio de adhesivos y **Kit Ducha Sin Cal** (bundle a 44,90 €, en Negro mate, Blanco y Gris).
- **Colecciones:** Ducha, Fregadero, Recambios y Todo jarandana (automática, por proveedor = jarandana).
- **Páginas:** Nosotros, Preguntas frecuentes, Cómo se instala, Contacto (con formulario), Devoluciones y Envíos.
- **Menús:**
  - Principal: Inicio, Ducha, Fregadero, Todo, Cómo se instala y Nosotros.
  - Pie: FAQ, Cómo se instala, Envíos, Devoluciones, Contacto, Recambios y Buscar.
- **Descuento** `BIENVENIDA10`: 10 % a partir de 25 €.
- **Imágenes de portada** generadas con Kling (baño con la Balda, mampara y fregadero), subidas a Archivos.
- **3 vídeos Kling** (portada, mampara y fregadero) subidos a Archivos de Shopify y puestos en la portada.
- **Tema en español** (textos del tema copiados de `es.json` sobre `en.default.json`, porque el idioma principal de la tienda es inglés) y plantillas de 404, carrito, colecciones y contacto traducidas.
- **SEO**: título y descripción para Google en los 8 productos y las 4 colecciones; imágenes en las colecciones.
- **Logo y favicon** subidos y puestos en el tema.
- **Sistema de reseñas reales** (metaobjeto "Reseña" + formulario). Ver [`shopify/theme/README.md`](../shopify/theme/README.md).
- **Tema "jarandana"** (copia de Horizon, **sin publicar**), rediseñado con secciones propias adaptadas a móvil:
  - Colores de marca: fondo crema `#F5EFE4`, texto `#1E2B37` y botones naranjas `#E4702E`.
  - Portada: cabecera con logo → portada con imagen y ventajas → 4 motivos → productos de Ducha → Rasqueta → Kit Fregadero → cómo se instala → todos los productos → reseñas → preguntas frecuentes → contacto.
  - Ficha de producto: ventajas, instalación, reseñas del producto, preguntas y "Combina con".
  - Cabecera y pie en español: barra de aviso, menús Tienda y Ayuda, y suscripción al boletín.
- **Kit Ducha:** ya no promete "envío gratis".

## Pendiente (lo haces tú en el admin)
0. **Idioma**: Ajustes → Idiomas → cambia el idioma predeterminado a **Español** (el checkout y los emails salen en inglés hasta que lo hagas).
1. **Envíos:** ve a Ajustes → Envíos, pon **3,95 €** y **gratis desde 35 €**, y desactiva las zonas UE e Internacional hasta lanzar allí.
2. **Tema:** ve a Tienda online → Temas → "jarandana" → **Vista previa**, revísalo y pulsa **Publicar**. La API no permite publicar temas. Si quieres, cambia la imagen del banner principal por el vídeo de Kling en Personalizar.
3. **Nombre de la tienda:** cambia "My Store" por **jarandana** en Ajustes → Detalles de la tienda.
4. **Políticas legales:** créalas en Ajustes → Políticas desde las plantillas de Shopify y añade tu NIF y tu dirección.
5. **Pagos:** activa Shopify Payments.
6. **Proveedores:** conecta **AutoDS** (o DSers) y enlaza cada producto con su ID de AliExpress (ver [11](11-productos-seleccionados-autods.md)).
7. **Apertura:** quita la contraseña de la tienda y elige un plan.
8. **Seguridad:** **revoca los tokens `shpat_`** que compartiste en el chat (Apps → Desarrollar apps).
9. **Imágenes de IA:** revísalas y cámbialas por fotos reales en cuanto lleguen las muestras.

# 24 · Revisión de UX de jarandana (método "design-critique" de Anthropic)

Revisión hecha sobre el código del tema, los datos de Shopify y las maquetas. La tienda tiene contraseña, así que falta una pasada en vivo por móvil: con la contraseña la hago y añado capturas.

## Primera impresión (2 segundos)
Marca alegre y reconocible: colores, azulejo, "sin taladrar". **Pero al entrar no se ve primero el producto ni la propuesta:** la portada empieza con textos, la cinta y las ofertas, y el bloque principal (hero) es la **sección 7 de 19**.

## Problemas por prioridad
| # | Problema | Gravedad | Recomendación |
|---|---|---|---|
| 1 | **Portada demasiado larga (19 secciones) y el hero en la posición 7.** En móvil hay que bajar mucho antes de ver qué vendes | 🔴 | Hero primero ("Tu casa, sin taladrar" + botón "Ver los más vendidos"). Luego: más vendidos → ofertas → cómo se instala → garantías → FAQ. Dejar unas 9 secciones y quitar la cinta duplicada |
| 2 | **0 reseñas reales.** La sección de opiniones y la página "Opiniones" salen vacías, y eso resta confianza | 🔴 | Ocultar la sección de reseñas hasta tener 3-5 reales (muestras gratis a probadores, indicándolo). Mientras, reforzar con garantías: 14 días, 3 años y "si llega roto, otro nuevo" |
| 3 | **Fotos del proveedor con textos o marcas ajenas** (dispensador con logo "oenon"/"MENGNI", bayetas "NO-7 THICKENED", textos en inglés) | 🔴 | ✅ Ya he corregido la foto principal de la esquinera, el fregadero y la luz. Falta sustituir las del dispensador y las bayetas por fotos limpias o propias |
| 4 | **Contraste insuficiente:** texto blanco sobre naranja (2,8:1), rosa (3,1:1) y turquesa (3,1:1). WCAG pide 4,5:1 para texto normal | 🟡 | Blanco solo en titulares grandes. En texto pequeño y botones, usar tinta #1E2B37 sobre naranja (5,1:1) o naranja oscuro #C95C1D |
| 5 | **Dominio jarandana.myshopify.com** | 🟡 | Comprar jarandana.es (~10 €/año). Da confianza y los anuncios convierten mejor |
| 6 | **Faltan datos técnicos:** carga máxima, medidas y material. La FAQ dice "lo indicamos en cada ficha" y no está | 🟡 | Tabla "Ficha técnica" en cada producto con los datos del proveedor |
| 7 | **Plazo de 7-15 días** | 🟡 | ✅ Ya se muestra la fecha estimada en la ficha. Añadir "Puede llegar en varios paquetes" en el carrito |
| 8 | **Tema v9 sin publicar:** el carrito nuevo y la página "Próximamente" no se ven | 🟡 | Publicarlo |
| 9 | **Pagos sin activar y NIF sin poner** | 🔴 para vender | Shopify Payments y alta de autónomo |
| 10 | Menú con 8 opciones | 🟢 | En móvil está bien (cajón con botones). En ordenador, agrupar "Nosotros" y "Cómo se instala" en "Ayuda" |

## Lo que funciona bien ✅
- Caja de compra con fecha de entrega, envío gratis y oferta
- Barra de compra fija en el móvil
- Carrito con barra de envío gratis y código de bienvenida
- Páginas legales completas, aviso de cookies correcto y enlaces del pie claros
- Identidad visual coherente en toda la web

## ✅ Aplicado en el tema v10 («jarandana v10 (publicar este)», sin publicar)
| # | Cambio |
|---|---|
| 1 | Portada con **9 secciones y el hero primero**: hero → cinta → «Nuestros favoritos» (8) → ofertas → baño → rasqueta → cómo se instala → opiniones → FAQ |
| 2 | La sección de opiniones **se oculta sola** mientras no haya reseñas reales |
| 3 | Foto principal limpia en el **dispensador** y las **bayetas** (recortes de la foto real, sin textos ajenos) |
| 4 | Colores más oscuros en naranja, turquesa y rosa, y en los botones de compra: **contraste AA** con texto blanco |
| 6 | Desplegable **«📋 Ficha técnica»** en 10 productos (medidas, material y peso del proveedor). Fregadero y dispensador no tienen datos fiables, así que no lo muestran |
| 7 | Aviso en el carrito: «Si pides varios productos, pueden llegar en paquetes separados». FAQ de peso reescrita con honestidad |

**Qué tienes que hacer tú:** Tienda online → Temas → «jarandana v10 (publicar este)» → **Vista previa** → si te gusta, **Publicar**.
Pendiente tuyo: dominio (5), pagos y NIF (9).

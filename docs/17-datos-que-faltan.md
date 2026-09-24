# 17 · Datos y ajustes que te faltan para vender

Ordenado por prioridad. ✅ = hecho por mí · 🟠 = solo lo puedes hacer tú.

## A. Imprescindible antes de abrir
| # | Qué | Dónde | Por qué |
|---|---|---|---|
| 1 | 🟠 **Tu nombre o empresa, NIF y dirección** | Tienda online → Páginas: Aviso legal, Privacidad, Condiciones de venta, Cookies y Devoluciones. Cambia `[TITULAR]`, `[NIF]` y `[DIRECCIÓN]` | Obligatorio por la LSSI y el RGPD |
| 2 | 🟠 **Políticas de Shopify** | Ajustes → Políticas. Copia los textos de `shopify/legal/politicas.json` | Son las que salen en el pago. Ahora la de privacidad está en inglés y a nombre de «My Store» |
| 3 | 🟠 **Nombre de la tienda: jarandana** | Ajustes → Detalles de la tienda | Sale en correos, facturas y pestaña del navegador |
| 4 | 🟠 **Idioma principal: español** | Ajustes → Idiomas | La tienda está en inglés por defecto: botones del carrito, pago y correos |
| 5 | 🟠 **Tarifas de envío** | Ajustes → Envíos y entregas → España: **3,95 €** y **gratis desde 35 €**. Quita UE e Internacional | Sin tarifas, el pago no deja terminar la compra fuera de las zonas activas |
| 6 | 🟠 **Pagos** | Ajustes → Pagos → Shopify Payments (necesita DNI/NIF, IBAN y teléfono) + PayPal | Sin pagos activos nadie puede comprar |
| 7 | 🟠 **Alta fiscal** | Hacienda (modelo 036/037) y Seguridad Social (autónomo) o tu empresa. Consulta a un gestor el IVA de importación (IOSS/OSS) | Vender de forma habitual exige estar dado de alta |
| 8 | 🟠 **Quitar la contraseña** | Tienda online → Preferencias | Hasta entonces nadie puede entrar a la tienda |
| 9 | 🟠 **Revocar los tokens `shpat_`** | Apps → Desarrollar apps | Los compartiste en el chat |

## B. Datos de producto que tienes que pedir a los proveedores
| Dato | Para qué | Dónde ponerlo |
|---|---|---|
| **Carga máxima** de balda, esquinera y ganchos | La FAQ dice que se indica en cada ficha: hay que ponerlo | Descripción de cada producto |
| **Medidas y materiales** reales | Ficha de producto y packaging | Descripción y `packaging/generar_packaging.py` |
| **Plazo real de entrega a España** | Ahora prometemos 7-15 días laborables. Si es más, hay que cambiarlo en Envíos, FAQ y la caja de compra | `snippets/jd-buybox.liquid` y páginas |
| **País de fabricación y responsable en la UE** | Etiquetado (Reglamento de seguridad de productos, GPSR) | Packaging |
| **Fotos o vídeos reales sin marca de agua** | Sustituir las imágenes creadas con IA | Productos y Archivos |

Mensaje para pedírselo: `docs/14-packaging-y-mensajes-proveedores.md`.

## C. Muy recomendable
| Qué | Dónde |
|---|---|
| 🟠 **Dominio propio** `jarandana.es` o `.com` (~10 €/año) | Ajustes → Dominios → Comprar |
| 🟠 **Email con tu dominio** (hola@jarandana.es) y ponerlo como remitente | Ajustes → Notificaciones → Remitente |
| 🟠 **Correos en español con tu logo y los bloques de reseña** | `docs/16-correos-y-resenas.md` |
| 🟠 **Redes sociales** (Instagram y TikTok @jarandana). Pásame los enlaces y los pongo en el pie | — |
| 🟠 **Teléfono o WhatsApp de atención** (opcional). Pásamelo y añado un botón flotante de WhatsApp | — |
| 🟠 **AutoDS o DSers** conectado para que los pedidos se tramiten solos | Apps |
| 🟠 **Google y Meta:** canal de Google y Facebook & Instagram, píxel de Meta y Google Merchant Center | Apps → canales de venta |
| 🟠 **Primeras reseñas reales** (probadores con muestra, indicándolo) | `docs/16-correos-y-resenas.md` |
| 🟠 **Correo de carrito abandonado** | Marketing → Automatizaciones → «Recuperar carrito abandonado» |

## D. Lo que ya está hecho ✅
- Diseño completo:
  - Portada, fichas, colecciones, páginas interiores, carrito, 404 y buscador, adaptado a móvil, tablet y ordenador.
  - Menú de botones y barra fija de compra en móvil.
  - Caja de compra con fecha estimada de entrega y oferta.
- 12 productos con fotos y vídeos, colecciones, ofertas reales (−15 % automático, packs y BIENVENIDA10) y margen de alrededor del 30 %.
- Páginas legales (con 3 huecos por rellenar), aviso de cookies con aceptar/rechazar y formulario de desistimiento.
- Sistema de reseñas reales con página «Opiniones», fotos y aviso de muestra gratis.
- Packaging con tu logo para cada producto, y mensajes para los proveedores.

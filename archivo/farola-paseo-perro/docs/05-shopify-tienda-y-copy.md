# 05 · Tienda Shopify: estructura, home, fichas y copy

## 1. Configuración base

| Elemento | Decisión |
|---|---|
| Plan | **Basic**: 32 €/mes (mensual) o 24 €/mes (anual); promoción habitual 1 €/mes los 3 primeros meses ([Finom](https://finom.co/es-es/blog/shopify-precios/), [Impulsa Ecommerce](https://impulsaecommerce.com/shopify-3-meses-por-1-euro/)) — confirma en shopify.es |
| Pagos | Shopify Payments (2,1 % + 0,30 € en Basic) + Bizum si tu pasarela lo permite (muy usado en España) — NO VERIFICADO disponibilidad en Shopify Payments |
| Tema | **Dawn** (gratuito, rápido) o **Sense/Refresh** (gratuitos). No comprar tema al principio |
| Idiomas | Español (lanzamiento). Italiano con **Shopify Translate & Adapt** (gratuito) en fase de expansión |
| Mercados | España (península + Baleares). Canarias: desactivar al inicio (IGIC/aduanas) |
| Envío | 3,95 € · **gratis desde 30 €** · plazo mostrado = el real del proveedor (no prometer 24 h si no es cierto) |
| Legal (obligatorio) | Aviso legal, privacidad (RGPD), cookies (banner), condiciones de venta, **desistimiento 14 días** (formulario modelo), política de envíos, **información GPSR en cada ficha** (fabricante/persona responsable UE + advertencias) |

## 2. Mapa de la tienda (máx. 7 productos)

```
HOME
├── TIENDA (todo)                 /collections/all
│   ├── Limpieza del paseo        /collections/limpieza      → Botella Chorro, Dispensador, Bolsas, Portabolsa
│   ├── Llevarlo todo             /collections/llevar        → Bandolera, Bolsa de premios
│   └── Agua y verano             /collections/agua          → Botella-Bebedero (desde primavera)
├── KITS (bundles)                /collections/kits          → Duo, Kit Esencial, Pack Premium, Bundle Completo
├── ¿ES OBLIGATORIO EN MI CIUDAD? /pages/normativa-ciudades (página SEO/contenido con fuentes)
├── NOSOTROS                      /pages/nosotros
├── FAQ                           /pages/preguntas-frecuentes
├── CONTACTO                      /pages/contacto
└── SEGUIR MI PEDIDO              /pages/seguimiento (app de tracking)
```
Menú principal: **Kits · Tienda · ¿Es obligatorio en mi ciudad? · Nosotros** · (icono) Seguir pedido.

## 3. HOME — sección por sección

| # | Sección | Copy | Imagen | Vídeo | CTA | Producto | Objetivo |
|---|---|---|---|---|---|---|---|
| 0 | Barra de anuncio | "Envío gratis desde 30 € · Cambios y devoluciones 14 días" | — | — | — | — | Reducir fricción |
| 1 | **Hero** | **H1: Paseos limpios. Manos libres.** Sub: "Botella limpia-pis, bolsas y premios que se enganchan entre sí. Todo el paseo, en una mano." | Dueña en acera al atardecer con el Kit enganchado a la correa | Loop 6-8 s (vídeo Kling #11): chorro sobre el pis junto a una farola → dispensador → premio | **Ver el Kit Paseo** (color Luz) · secundario "Ver todo" | Kit Paseo Esencial | Entender en 3 s qué vendemos |
| 2 | Barra de confianza | "🚚 Envío con seguimiento · ↩︎ 14 días para devolver · 🔒 Pago seguro · 💬 Te respondemos en 24 h laborables" | Iconos de línea | — | — | — | Confianza |
| 3 | **El problema** | H2: "Sacar al perro no debería ser un malabarismo." Texto: "Correa, bolsas, la botella para el pis, la bolsa usada, los premios, el móvil, las llaves… y el vecino mirando. Lo hemos resuelto en un solo sistema." | Collage: manos llenas vs mano libre | GIF 3 s antes/después | — | — | Identificación |
| 4 | **Cómo funciona (3 pasos)** | 1. **Engancha** la Botella Chorro a la correa. 2. **Clica** el Dispensador en la botella. 3. **Paseo hecho**: un chorrito, una bolsa, y a casa. | 3 fotos en la calle | — | "Montar mi kit" | Kit Esencial | Mostrar el "sistema" |
| 5 | **Kits** (tarjetas) | Duo (21,90 €) · **Kit Esencial (32,90 €) — "El más elegido"** (solo cuando sea verdad; al inicio "Nuestro favorito") · Pack Premium (64,90 €) · Bundle Completo (79,90 €). Mostrar "Por separado: 37,60 €" | Foto de cada kit sobre arena | — | "Elegir kit" | Todos los packs | Subir AOV |
| 6 | **¿Es obligatorio en tu ciudad?** | "En ciudades como Valencia, Alicante, Valladolid, Gijón o Bilbao limpiar el pis del perro es obligatorio y hay multas. Consulta tu ciudad." | Mapa ilustrado | — | "Consultar mi ciudad" | — | Urgencia **real** + SEO |
| 7 | **Producto estrella** | Botella Chorro: "Chorro dirigido, cero goteo, se engancha en 1 segundo." 4 colores | Fotos de color | Demo 5 s | "Elegir color" | P1 | Entrada barata |
| 8 | **UGC / reseñas** | "Lo que dicen en el parque" — solo reseñas reales (Judge.me). Antes de tener reseñas: sección oculta | Fotos de clientes | 3 vídeos UGC | — | — | Prueba social |
| 9 | **Bolsas que no fallan** | "Grandes, gruesas y opacas. Recarga cuando quieras, sin suscripción obligatoria." (**sin "eco"/"biodegradable"**) | Foto bolsa resistiendo peso | Prueba de resistencia 4 s | "Recargar bolsas" | P3 | Recompra |
| 10 | Nosotros (bloque corto) | "Nacimos en una acera de [tu ciudad], con un perro, una botella de agua de 50 cl y demasiadas cosas en las manos." | Foto fundador + perro | — | "Nuestra historia" | — | Marca real |
| 11 | FAQ (4 preguntas) | Ver §6 | — | — | "Ver todas" | — | Objeciones |
| 12 | Newsletter | "Consejos de paseo y avisos de normativa en tu ciudad. Sin spam." | — | — | "Apuntarme" | — | Lista de email |
| 13 | Footer | Logo · menú · legal · "Información de seguridad de producto (GPSR)" · métodos de pago | — | — | — | — | Cumplimiento |

## 4. Plantilla de ficha de producto + copy completo (ejemplo: **Kit Paseo Esencial**)

**Estructura (de arriba abajo)**
1. Galería (1ª imagen = kit enganchado a la correa en la calle; 2ª = contenido del kit; 3ª = vídeo demo; 4ª = colores; 5ª = medidas)
2. Título + estrellas (cuando existan)
3. Hook + beneficio principal
4. Precio + "Por separado: 37,60 €"
5. Selector de color + **quantity/bundle selector**
6. Oferta (envío gratis)
7. Añadir al carrito + Comprar ya
8. Mini-garantía + envío
9. Vídeo UGC → Demostración → Beneficios → Cómo funciona → Qué incluye → Reseñas → FAQ → Garantía → Envío → Cross-sell → Upsell → Bundle
10. **Sticky add-to-cart** en móvil (barra fija inferior con precio + botón)

**Copy**

> **Título:** Kit Paseo Esencial — Botella limpia-pis + Dispensador + 150 bolsas + Portabolsa
>
> **Hook:** El paseo entero, en una mano.
>
> **Beneficio principal:** Limpia el pis en un segundo, saca una bolsa sin pelearte con el rollo y lleva la bolsa usada colgada de la correa — no de tus dedos.
>
> **Precio:** **32,90 €** · *Por separado: 37,60 €* · Envío gratis
>
> **Color:** ◯ Arena ◯ Salvia ◯ Terracota ◯ Noche *(todo el kit en el mismo color)*
>
> **Cantidad:**
> ◉ 1 kit — 32,90 €
> ○ 2 kits (dos perros o para regalar) — 59,90 € *(ahorras 5,90 €)*
>
> **Oferta:** 🚚 Envío gratis en este kit · ↩︎ 14 días para devolverlo
>
> **[ Añadir al carrito ]** **[ Comprar ya ]**
>
> *Recíbelo en X–Y días laborables (plazo real del proveedor). Seguimiento incluido.*

**Vídeo UGC** (autoplay sin sonido, subtítulos): "Llevo 2 años con la botella del ayuntamiento goteando en el bolsillo. Esto es otra cosa."

**Demostración (3 GIF):** chorro sobre el pis · bolsa sale con una mano · bolsa usada enganchada a la correa.

**Beneficios**
- **Chorro dirigido, cero goteo.** El tapón solo suelta agua cuando aprietas. Nada de pantalones mojados.
- **Todo se engancha.** Botella a la correa, dispensador a la botella, bolsa usada al portabolsa. Un solo gesto.
- **Bolsas que no te dejan tirado.** Grandes, gruesas y opacas. 150 incluidas.
- **Pensado para la calle española.** 450-500 ml: suficiente para varios pises. Úsala con agua (o agua y un poco de vinagre, como recomiendan muchos ayuntamientos).
- **Bonito de verdad.** Colores que combinan con tu correa, no verde fosforito.

**Cómo funciona**
1. Llena la botella en casa (10 segundos).
2. Engánchala a la correa con el mosquetón y clica el dispensador.
3. Pis → chorrito. Caca → bolsa → portabolsa → papelera.

**Qué incluye:** 1 Botella Chorro · 1 Dispensador Clic (con 2 rollos) · 8 rollos de recarga (120 bolsas) · 1 Portabolsa Sin Manos.

**Reseñas:** (Judge.me; solo reseñas reales verificadas. Pedir reseña con foto a los 10 días de la entrega.)

**FAQ de ficha**
- *¿Es obligatorio limpiar el pis en mi ciudad?* En muchas sí (Valencia, Alicante, Valladolid, Gijón, Bilbao…). Mira nuestra página de normativa, con enlaces a la fuente.
- *¿Qué le pongo dentro?* Agua. Muchos ayuntamientos recomiendan agua con algo de vinagre. No uses lejía.
- *¿Sirve cualquier rollo en el dispensador?* Sí, rollos estándar.
- *¿Las bolsas son biodegradables?* Son bolsas convencionales, gruesas y resistentes. No decimos que sean "eco" porque no tenemos una certificación que lo demuestre. *(Si en el futuro se tiene EN 13432 del producto, se cambia.)*
- *¿Cuánto tarda?* X–Y días laborables con seguimiento.

**Garantía:** "Si algo llega roto o defectuoso, te lo reponemos. Y si no te convence, tienes 14 días para devolverlo."

**Envío:** "Envío con seguimiento a península y Baleares. 3,95 € · gratis desde 30 €."

**Cross-sell (bloque "Se engancha con…"):** Bolsa de Premios Imán (12,90 €) · Bolsas 32 rollos (19,90 €).

**Upsell (en ficha):** "¿Paseas con premios, móvil y llaves? → **Pack Premium** con Bandolera: 64,90 € (por separado 87,50 €)."

**Bundle (tabla comparativa al final):** Duo · Esencial · Premium · Completo con check de qué incluye cada uno.

**Bloque GPSR (plegable al final):** Fabricante: [razón social y dirección del fabricante]. Persona responsable en la UE: [tu empresa / 3PL / representante]. Advertencias: "No es un juguete. Mantener fuera del alcance de niños pequeños (piezas pequeñas). No apto para líquidos calientes ni productos químicos."

### Copy corto de las otras fichas

| Producto | Título | Hook | Beneficio principal |
|---|---|---|---|
| P1 | Botella Chorro — limpia-pis anti-goteo 500 ml | "Un chorrito y el vecino ni se entera." | Chorro dirigido, no gotea, se engancha a la correa en 1 s |
| P2 | Dispensador Clic — resistente a la lluvia | "La bolsa sale a la primera. Llueva o no." | Tapa estanca, salida sin atascos, se clica a la botella |
| P3 | Bolsas Farola XL — 16 o 32 rollos | "Grandes, gruesas y opacas. Punto." | No se rompen, no transparentan, caben en cualquier dispensador |
| P4 | Bolsa de Premios Imán | "Se abre con un dedo. Se cierra sola." | Cierre magnético, silicona lavable, clip a cinturón |
| P5 | Bandolera Paseo | "Todo el paseo, cruzado al hombro." | Funda de botella, salida de bolsas, bolsillo de premios, móvil y llaves |
| P6 | Portabolsa Sin Manos | "La bolsa usada viaja en la correa, no en tu mano." | Sujeta la bolsa cerrada hasta la papelera |
| P7 | Botella-Bebedero 2 en 1 | "Agua para él, sin cuencos extra." | Cuenco abatible, sin derrames, 350/550 ml |

## 5. Páginas

**KITS (colección):** encabezado "Elige tu paseo" + tabla comparativa + nota "Los kits cuestan menos que las piezas por separado. Siempre."

**NOSOTROS** (plantilla — rellénala con tu historia real, nunca inventada):
> "FAROLA nació en [ciudad], en [año], paseando a [nombre del perro]. Cada paseo era un malabarismo: la correa, las bolsas, la botella del ayuntamiento que goteaba en el bolsillo… Queríamos pasear como buenos vecinos sin parecer un carrito de la compra. Así que diseñamos un sistema: piezas que se enganchan entre sí y que da gusto llevar. Somos una marca pequeña, contestamos nosotros mismos los mensajes y solo vendemos lo que usamos cada día."

**FAQ (página completa):** envíos (plazos reales, seguimiento), devoluciones (14 días, cómo, quién paga el retorno), cambios de color, compatibilidad de rollos, qué poner en la botella, limpieza (lavar con agua y jabón; no lavavajillas si el proveedor no lo certifica), normativa por ciudad, pago (métodos), factura, contacto, **por qué no decimos "biodegradable"**.

**CONTACTO:** formulario + email + horario ("Lunes a viernes, 9-18 h, respondemos en 24 h laborables") + datos legales de la empresa. WhatsApp Business opcional.

**SEGUIR MI PEDIDO:** página con app de tracking (p. ej. "Parcel Panel" o "Track123", ambas con plan gratuito — **NO VERIFICADO**, compruébalo en la Shopify App Store).

**¿ES OBLIGATORIO EN MI CIUDAD?:** tabla por ciudad con fuente oficial enlazada y fecha de revisión. **Solo ciudades con fuente**. Es la página SEO más valiosa.

## 6. Apps (mínimas)

| Necesidad | App | Coste |
|---|---|---|
| Bundles | **Shopify Bundles** (oficial) | Gratis — confirmar |
| Quantity breaks / upsell en carrito | Opción gratuita de la App Store (buscar "volume discount" con plan free) | Gratis/freemium — NO VERIFICADO |
| Reseñas | **Judge.me** | Plan gratuito — confirmar |
| Email | **Shopify Email** (incluye envíos gratis mensuales) o Klaviyo free | Gratis al inicio — confirmar |
| Dropshipping | **CJdropshipping app** | Gratis |
| Tracking | Parcel Panel / Track123 | Plan free — NO VERIFICADO |
| Cookies/RGPD | Banner de privacidad nativo de Shopify | Gratis |

➡️ Siguiente: [06 · Kling: 30 vídeos](06-kling-30-videos.md)

# 07 · Meta Ads — estructura inicial y tests A/B

## 1. Antes de gastar 1 €
- Business Manager + página FB + cuenta IG profesional + **píxel y API de conversiones** (integración nativa de Shopify "Facebook & Instagram").
- Dominio verificado en Meta. Evento de optimización: **Compra**.
- Catálogo de Shopify sincronizado (para retargeting con catálogo más adelante).
- Mínimo **3 vídeos UGC reales o de marca listos** (V1-V10) y la tienda revisada en móvil.
- ⚠️ Categoría de anuncio: normal (no es especial). No usar lenguaje que "atribuya características personales" ("¿Tienes perro y eres mal vecino?") → Meta lo rechaza; hablar del producto y de la situación.

## 2. Presupuesto y estructura [HIPÓTESIS de partida]

| Fase | Días | Campaña | Presupuesto diario | Objetivo |
|---|---|---|---|---|
| **Test de ángulos** | 1-7 | CBO/ABO "TEST-ÁNGULOS" · Ventas · Advantage+ audiencia · España (ciudades con ordenanza + resto) | **20-30 €/día** (≈ 5 conjuntos × 5 €) | Encontrar 1-2 ángulos con CTR > 1 % y coste por añadir al carrito razonable |
| **Test de creativos** | 8-14 | "TEST-CREATIVOS" con el ángulo ganador | 20-30 €/día | 3-5 variaciones de hook/creativo |
| **Test de oferta** | 15-21 | "TEST-OFERTA" | 20-30 €/día | Kit vs Botella vs Premium como landing |
| **Escalado** | 22-30 | "ESCALA" (Advantage+ Shopping si hay ≥ 15-25 compras) + "RETARGETING" | +20 % cada 48-72 h si CPA < CPA objetivo | Rentabilidad |

**Reglas de corte** [HIPÓTESIS, ajustar con tus datos]
- Anuncio con gasto ≥ 2× CPA objetivo (≈ 25-30 €) y **0 añadidos al carrito** → apagar.
- CTR (enlace) < 0,7 % tras 1.000 impresiones → cambiar hook.
- CPA ≤ 15 € (equilibrio del Kit, ver [02](02-catalogo-variantes-oferta.md)) → mantener y escalar.

## 3. Audiencias
| Audiencia | Definición |
|---|---|
| A1 Amplia España | 22-60, España, Advantage+ (sin intereses) — **la principal** |
| A2 Ciudades con ordenanza | Ubicación: Valencia, Alicante, Valladolid, Gijón, Bilbao, León, Huesca, Málaga (radio 15-25 km) — para el ángulo normativa |
| A3 Intereses | Perros, adopción de mascotas, Kiwoko, Tiendanimal, Zooplus (solo como test contra A1) |
| A4 Regalo | 25-55, Advantage+, con creativo de regalo (nov-dic) |
| R1 Retargeting | Visitas 30 días, añadidos al carrito 14 días (excluir compradores) |
| R2 Recompra | Compradores 45-120 días → Bolsas 32 rollos |

## 4. Anuncios (fase test de ángulos) — 1 anuncio por ángulo

| ID | Vídeo | Producto/landing | Oferta | Audiencia | Primary text | Headline | CTA |
|---|---|---|---|---|---|---|---|
| **AD-01** Normativa | V1 | Kit Esencial | Envío gratis | A1 + A2 | "En ciudades como Valencia, Alicante, Valladolid o Gijón limpiar el pis del perro es obligatorio (y hay multas). 💧 La Botella Chorro suelta agua solo cuando aprietas y va enganchada a la correa. En la web tienes las fuentes de cada ciudad." | "Un chorrito y listo" | Comprar |
| **AD-02** Goteo | V2 | Botella (con upsell a Kit) | Envío gratis desde 30 € | A1 | "Si la botella que te dio el ayuntamiento te moja el bolsillo, no estás solo/a. La nuestra tiene tapón anti-goteo y mosquetón. 4 colores." | "La botella que no gotea" | Comprar |
| **AD-03** Manos llenas | V3 | Kit Esencial | Envío gratis | A1 | "Correa, bolsas, botella, bolsa usada, móvil, llaves… 🤹 Lo hemos juntado todo en la correa. Kit Paseo Esencial: botella limpia-pis + dispensador + 150 bolsas + portabolsa." | "Todo el paseo, en una mano" | Comprar |
| **AD-04** Vecinos | V4 | Botella | Envío gratis desde 30 € | A1 | "Tu vecina del bajo te lo agradecerá. 😉 Un chorrito de agua después del pis y la esquina queda como estaba." | "Sé el vecino favorito" | Más información |
| **AD-05** Estética | V5 | Pack Premium | Envío gratis | A1 (mujeres 25-45 como señal, no restricción) | "Botella, bolsas, premios con imán, móvil y llaves. Todo en una bandolera que sí te pondrías. 🐾" | "Qué llevo en mi bandolera de paseo" | Comprar |

Fase creativos (con el ángulo ganador) → AD-06…AD-10 = V6-V10 + variaciones de hook (texto en pantalla distinto, primeros 2 s distintos).

## 5. Matriz de tests A/B (una variable cada vez)

| Test | Variante A | Variante B | Variable fija | Métrica de decisión |
|---|---|---|---|---|
| **HOOK** | "¿Sabías que te pueden multar…?" | "Mi vecina del bajo antes no me saludaba" | Mismo vídeo a partir del s3, mismo copy, misma landing | Tasa de reproducción de 3 s + CTR |
| **ÁNGULO** | Normativa (AD-01) | Manos llenas (AD-03) | Misma landing (Kit), misma oferta | CPA / coste por añadir al carrito |
| **CREATIVO** | UGC personaje (V3) | Demo stop-motion (V19) | Mismo ángulo y copy | CTR + CPA |
| **COPY** | Largo (con lista del kit) | Corto ("Todo el paseo, en una mano. Envío gratis.") | Mismo vídeo | CTR + CPA |
| **OFERTA** | Landing Kit Esencial 32,90 € envío gratis | Landing Botella 12,90 € + barra "envío gratis desde 30 €" | Mismo vídeo | **Beneficio por visita** (no solo CPA): AOV × CR − coste |

Duración mínima de cada test: hasta ~50 clics por variante o 3-4 días; no decidir con < 1.000 impresiones.

## 6. Copys de retargeting y recompra
- **R1 (carrito abandonado, anuncio):** "Tu kit sigue aquí. Envío gratis y 14 días para devolverlo." — Headline: "Termina tu kit" — CTA: Comprar.
- **R2 (recompra bolsas):** "¿Se acaban las bolsas? Pack 32 rollos: bolsas XL para ~8 meses de paseos*" (*cálculo a 2 bolsas/día). — Headline: "Recarga en 1 clic".

## 7. Lo que NO haremos
- Precios tachados inventados, contadores de tiempo falsos, "últimas unidades" sin ser verdad.
- "Biodegradable/eco" sin certificado.
- Testimonios IA presentados como clientes reales.
- Afirmar multas o ciudades sin fuente.

➡️ Siguiente: [08 · TikTok orgánico](08-tiktok-organico.md)

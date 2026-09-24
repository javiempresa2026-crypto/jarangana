# 20 · Vídeos de anuncio y campañas (Meta, TikTok, Pinterest)

## Los 5 vídeos (`ads/out/`)
Formato vertical 1080×1920 (9:16) de 15 s, con fotos reales del producto. Cada uno tiene gancho, 4 escenas con subtítulos, precio y cierre con logo, envío gratis y BIENVENIDA10.

| Vídeo | Gancho | Para quién |
|---|---|---|
| `jarandana-grifo.mp4` | «Tu grifo puede hacer ESTO 👀» | Curiosidad: el más «viral» |
| `jarandana-luz.mp4` | «Se acabó buscar a oscuras 🔦» | Armarios, cocina, pasillo |
| `jarandana-rasqueta.mp4` | «El truco para una mampara sin cal ✨» | Limpieza (TikTok #cleantok) |
| `jarandana-kit-ducha.mp4` | «Mi casero: «ni un agujero» 🙅» | Gente de alquiler (tu público principal) |
| `jarandana-fregadero.mp4` | «Friegas con una mano 🧽» | Cocina |

Van **sin música a propósito**. Al subirlos, elige un **sonido en tendencia** desde la propia app (TikTok, Reels). La música con derechos que pongas en el archivo te la pueden silenciar, y el sonido en tendencia ayuda mucho al alcance.

Para regenerarlos o hacer más: edita `ADS` en `ads/render.py` y ejecuta `python3 ads/render.py`.

> Lo que más se viraliza en esta categoría son los **vídeos reales grabados con el móvil**: tu mano instalando la balda o el grifo, el «antes y después» de la mampara o la luz encendiéndose al pasar. Cuando te llegue el primer pedido de muestra, graba 10 clips de 3-5 s y te monto los vídeos con ellos.

## 1. Conectar Shopify con Meta y TikTok (una vez, gratis)
1. **Facebook e Instagram:** Shopify → Apps → busca **«Facebook & Instagram»** (de Meta) → Instalar.
   - Conecta tu **Página de Facebook** (créala: «jarandana») y tu **Instagram de empresa** (@jarandana).
   - Crea la **cuenta publicitaria** y el **píxel/Conversions API** con el nivel de datos **«Máximo»**.
   - Activa el **catálogo**: tus 12 productos se sincronizan solos y puedes etiquetarlos en las publicaciones (Instagram Shopping).
2. **TikTok:** Shopify → Apps → **«TikTok»** → cuenta de TikTok for Business + píxel + catálogo.
3. **Google** (opcional): app **«Google & YouTube»**, para Shopping gratis y YouTube Shorts.
4. **Pinterest** (opcional): app **«Pinterest»**. Para hogar y baño funciona muy bien de forma orgánica.

El aviso de cookies de la web ya respeta el consentimiento: los píxeles solo miden si el cliente acepta.

## 2. Dónde subir cada vídeo (orgánico, gratis)
| Plataforma | Cómo | Frecuencia |
|---|---|---|
| **TikTok** | Sonido en tendencia + texto corto. Hashtags: #hogar #baño #limpieza #cleantok #alquiler #trucosdecasa #sintaladro | 1 al día |
| **Instagram Reels** | Mismo vídeo; etiqueta el producto (catálogo) | 4-5 por semana |
| **Facebook Reels** | Se comparte desde Instagram | automático |
| **YouTube Shorts** | Mismo vídeo; título con la palabra clave («balda ducha sin taladrar») | 3 por semana |
| **Pinterest** | Pin de vídeo con enlace al producto; tablero «Baño pequeño sin obras» | 3-5 por semana |

**Textos para publicar (cópialos):**
- Grifo: «¿Sabías que existe esto? 🤯 Se pone en 1 minuto y gira 1080°. #trucosdecasa #cocina #baño»
- Luz: «La mejor compra para el armario 🔦 Se enciende sola al pasar. #hogar #organizacion»
- Rasqueta: «10 segundos al día y adiós cal en la mampara ✨ #cleantok #limpieza»
- Kit ducha: «Vivir de alquiler y tener la ducha ordenada SIN agujeros 🙅 #alquiler #baño #sintaladro»
- Fregadero: «El cambio más tonto que más uso en la cocina 🧽 #cocina #hogar»

## 3. Primera campaña en Meta Ads (Facebook e Instagram)
Empieza cuando tengas **pagos activos, contraseña quitada y alta fiscal** (doc 17).

**Estructura de prueba (7 días, unos 10 €/día):**
- **Campaña:** objetivo **Ventas** → «Advantage+ campaña de ventas».
- **País:** España · **Edad:** 25-55 · **Público:** Advantage+ (automático, sin intereses). Con vídeos claros, Meta encuentra al público.
- **Ubicaciones:** Advantage+ (Reels, Stories, Feed).
- **Anuncios:** los 5 vídeos en la misma campaña. Meta reparte el dinero hacia el que mejor funcione.
- **Texto principal:** «Baño y cocina ordenados sin taladrar. Envío GRATIS desde 35 € · -10 % en tu primer pedido con BIENVENIDA10.»
- **Titular:** el nombre del producto + precio. **Botón:** «Comprar».
- **Enlace:** directo a la ficha del producto de cada vídeo (no a la portada).

**Cómo leer los resultados, después de 3-4 días:**
| Métrica | Buena | Si va mal |
|---|---|---|
| CTR (clics / impresiones) | > 1,5 % | Cambia el gancho de los 2 primeros segundos |
| CPC | < 0,60 € | Prueba otro vídeo |
| Coste por compra | < 12-15 € | El margen por pedido ronda 5-15 €: si es mayor, pausa ese anuncio |

- Apaga los anuncios que a las 48 h tengan CTR < 0,8 %. Sube el presupuesto un 20 % cada 2-3 días al que venda.
- **Retargeting** (cuando tengas ~1.000 visitas): público de «visitaron la web y no compraron», con el vídeo del kit ducha y el código BIENVENIDA10. 3-5 €/día.

**Importante:** no pongas mucho dinero hasta ver ventas. Con 70 € en una semana ya sabes qué producto tira.

## 4. TikTok Ads (cuando algún vídeo funcione orgánico)
- **Spark Ads:** promociona el vídeo orgánico que más visitas tenga, porque conserva likes y comentarios. Presupuesto mínimo de 20 €/día por grupo.
- Objetivo: Ventas en la web (con el píxel de la app de TikTok).

## 5. Colaboraciones (UGC), muchas veces lo que mejor funciona
- Busca en TikTok o Instagram creadores de hogar y limpieza de 5.000-50.000 seguidores en España.
- Ofrece **producto gratis** a cambio de un vídeo, o 50-100 € por vídeo con derechos para usarlo en anuncios.
- En el vídeo tienen que indicar **#publicidad** o **#colaboración** (obligatorio en España).
- Mensaje: «¡Hola! Soy de jarandana, accesorios de baño y cocina sin taladrar. Nos encanta tu contenido de hogar. ¿Te apetece probar nuestra balda de ducha y, si te gusta, hacer un vídeo? Te la enviamos gratis. 🧡»

## 6. Reglas para no tener problemas
- No prometas lo que el producto no hace: ni «aguanta 20 kg», ni «quita la cal», ni «llega en 3 días».
- Las fotos de los vídeos son del proveedor. Para anuncios lo ideal son tus propias fotos y vídeos; en cuanto tengas el producto, sustitúyelas.
- Las reseñas o testimonios de los anuncios tienen que ser reales.

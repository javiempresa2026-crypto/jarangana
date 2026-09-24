# 21 · Contenido orgánico para Instagram y TikTok

## Vídeos ya hechos (`ads/out/`)
| Archivo | Tipo | Voz | Dónde |
|---|---|---|---|
| `organico-3-inventos.mp4` | «3 inventos para tu casa de alquiler» | Sí (voz en off + subtítulos) | TikTok, Reels, Shorts |
| `organico-casero.mp4` | «POV: tu casero dice ni un agujero» | Sí | TikTok, Reels |
| `jarandana-campana.mp4` | Vídeo largo de campaña (~37 s) con botón COMPRAR AHORA | No (añade música en Meta) | Anuncio Meta / TikTok |
| `jarandana-grifo-ia.mp4`, `-luz-ia`, `-rasqueta-ia` | Anuncio con clip en movimiento | No | Anuncio o Reel |
| `jarandana-grifo.mp4`… (5) | Anuncio con fotos | No | Anuncio o Reel |

**La voz en off** es sintética: Piper, voz de España «davefx», con licencia CC0 que permite uso comercial. Se genera sin coste con `python3 ads/organico.py`. Para cambiar el texto, edita `VIDEOS` en `ads/organico.py`.
- Si prefieres una voz más natural, pon la **voz de TikTok** («Texto a voz» en el editor) o graba **tu propia voz**: es lo que mejor funciona.
- Si subes el vídeo con voz, **baja la música** del sonido en tendencia al 10-20 %.

## Qué publicar (fórmulas que funcionan en hogar y limpieza)
1. **«3 cosas que…»:** 3 inventos para el baño, para la cocina o para pisos de alquiler.
2. **POV:** «POV: tu casero dice ni un agujero», «POV: te mudas y te lo llevas todo».
3. **Antes y después:** mampara con cal y mampara limpia, armario a oscuras y con luz.
4. **Satisfactorio (ASMR):** la rasqueta en el cristal, el grifo cambiando de chorro, el clic del dispensador. Sin voz, solo sonido real.
5. **Tutorial de 15 s:** «Cómo poner una balda sin taladrar»: limpia, pega, presiona y espera 24 h.
6. **Mito o verdad:** «¿Aguantan las baldas adhesivas?», con lo que es cierto: superficie lisa y esperar 24 h.
7. **Respuesta a comentarios:** responde con vídeo a las preguntas. Es el formato que más alcance da en TikTok.
8. **Unboxing:** abrir tu caja con el packaging de jarandana.

## Calendario de 4 semanas (1 vídeo al día en TikTok, 4-5 en Instagram)
| Semana | L | M | X | J | V | S | D |
|---|---|---|---|---|---|---|---|
| 1 | 3 inventos | Grifo (clip) | POV casero | Rasqueta ASMR | Luz (clip) | Tutorial balda | Oferta semana |
| 2 | Antes/después mampara | Fregadero | Mito o verdad | Grifo 2 chorros | 3 cosas cocina | Unboxing | Respuesta a comentario |
| 3 | POV mudanza | Luz armario | Kit ducha | Rasqueta ASMR | Dispensador pasta | Tutorial esquinera | Oferta semana |
| 4 | Los 3 más vendidos | Respuesta | Antes/después baño | Grifo | Luz pasillo | Tutorial ganchos | Resumen del mes |

**Hora:** 13:00-14:00 o 20:00-22:00 (hora de España).
**Hashtags base:** #hogar #trucosdecasa #baño #cocina #limpieza #cleantok #alquiler #sintaladro #organizacion #pisodealquiler

## Herramientas para automatizar (y cuáles puedo usar yo)
| Para qué | Herramienta | ¿Lo puedo hacer yo desde aquí? |
|---|---|---|
| Voz en off | Piper (instalado) | ✅ Ya lo hago |
| Voz en off más natural | **ElevenLabs** (de pago, con uso comercial) | ✅ Si me das una clave de API como «secreto» del entorno |
| Clips con IA | **Kling** (ya conectado) | ✅ Unos 50 créditos por clip de 5 s |
| Montaje de los vídeos | Python + ffmpeg (instalado) | ✅ Ya lo hago |
| Plantillas y miniaturas | **Canva** (conector de Claude) | ✅ Si conectas Canva en claude.ai → Conectores |
| Campañas de TikTok Ads | **TikTok for Business** (conector de Claude) | ✅ Si lo conectas, puedo crear y analizar campañas |
| Resultados de Meta Ads | **Windsor.ai** o **Supermetrics** (conectores) | ✅ Leer métricas y recomendarte cambios |
| Programar publicaciones de Instagram y Facebook | **Meta Business Suite** (gratis) | ❌ Lo subes tú: 5 min a la semana, programas los 7 vídeos |
| Programar en TikTok | TikTok Studio (web, gratis, programa hasta 10 días) | ❌ Lo subes tú |

**Rutina semanal:**
1. Cada lunes te preparo los 7 vídeos de la semana con voz y los textos para publicar.
2. Tú los programas en Meta Business Suite y TikTok Studio en unos 10 minutos.

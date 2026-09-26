# 25 · Pack de contenido «de creador» (vídeos al ritmo, portadas y carrusel)

## Vídeos (`ads/out/pro/`, 9:16, 11-12 s, con sonido)
Edición como la de los creadores que más visitas tienen:
- **Cortes al ritmo** de una base propia a 118 bpm, sin derechos de terceros: nadie te lo silencia.
- **Zoom de impacto** en cada corte y **destello** en el momento clave.
- **Texto nativo** (recuadro blanco) que entra con rebote y un «pop».
- Efectos de **whoosh**, **golpe grave** y **ding** en la tarjeta final.
- Color retocado y **tarjeta final** animada con precio, «enlace en el perfil» y BIENVENIDA10.

| Vídeo | Gancho (primer segundo) | Texto para publicar |
|---|---|---|
| `grifo-1080.mp4` | «tu grifo puede hacer ESTO 👀» | ¿Sabías que existía esto? 🤯 Gira 1080° y cambia a modo ducha. Se enrosca en 1 minuto. #trucosdecasa #cocina #baño #gadgets |
| `luz-sensor.mp4` | «POV: 7 de la mañana, sin despertar a nadie 🤫» | La compra más tonta que más uso 💡 Se enciende sola al abrir. Imán + adhesivo, cero agujeros. #organizacion #armario #hogar |
| `mampara-10s.mp4` | «el truco de 10 segundos ✨» | El secreto no es frotar más: es quitar el agua antes de que se seque 💧 #cleantok #limpieza #mampara |
| `ducha-sin-agujeros.mp4` | «mi casero: «ni un agujero» 🙅» | Vivir de alquiler y tener la ducha ordenada SIN taladrar 🙌 ¿Quién más tiene casero así? 👇 #pisodealquiler #sintaladro #baño |
| `top3-menos-25.mp4` | «3 cosas de menos de 25 €…» | ¿Con cuál te quedas: 1, 2 o 3? 👇 Los 3 sin taladrar. #inventos #hogar #pisodealquiler |

**Cómo subirlos para que rindan:**
1. Sube el vídeo **con su sonido**. Si quieres usar un sonido en tendencia, ponlo al 10-15 % para que se oigan los efectos.
2. Elige la **portada** de `ads/out/pro/portadas/`: TikTok → «Editar portada» → «Subir». En Reels: «Portada» → «Añadir desde el carrete».
3. Publica entre 13:00-14:00 o 20:00-22:00 y contesta todos los comentarios en la primera hora.
4. Si uno pasa de 1.000 visualizaciones en orgánico, **promociónalo** (Spark Ads en TikTok o «Promocionar» en Instagram) con 5-10 €/día.

## Portadas (`ads/out/pro/portadas/*.jpg`, 1080×1920)
El título va en la franja central, que es lo que se ve en la cuadrícula del perfil (3:4). Así el perfil queda ordenado y «de marca».

## Carrusel educativo (`ads/out/posts/10-errores-*.jpg`, 5 imágenes)
«3 errores que hacen que tu balda adhesiva se caiga». Es el formato que más **guardados y compartidos** consigue, y eso es lo que más empuja el alcance en Instagram.

**Texto:**
> 3 errores que hacen que tu balda adhesiva se caiga 😱 (el 3 lo hace casi todo el mundo)
>
> ❌ Pegarla en gotelé, pintura o madera sin lacar → ✅ solo azulejo, cristal o metal
> ❌ No limpiar antes → ✅ alcohol y secar bien
> ❌ Cargarla el mismo día → ✅ presiona 30 s y espera 24 h
>
> 📌 Guárdalo para cuando te llegue y mándaselo a quien se acaba de mudar.
>
> #trucosdecasa #pisodealquiler #sintaladro #organizacion #hogar #baño #tutorial

**Primer comentario tuyo:** «¿Cuál de los 3 errores habías cometido? 👀»

## Para regenerar o hacer más
- `python3 ads/pro.py [nombre]`: edita `VIDEOS` en `ads/pro.py` (plano, pulsos, texto, efecto y marcas `flash`/`boom`).
- `python3 ads/carrusel_errores.py`
- `python3 ads/sfx.py`: vuelve a crear los efectos y la base.

# 16 · Correos automáticos y reseñas

## 1. Correos que ya salen solos (Shopify)
En cuanto alguien compra, Shopify envía **automáticamente** estos correos al email que el cliente pone al pagar:

| Correo | Cuándo sale |
|---|---|
| **Confirmación de pedido** | Al pagar |
| **Confirmación de envío** (con nº de seguimiento) | Cuando marcas el pedido como enviado o lo hace AutoDS/DSers |
| **En reparto** y **Entregado** | Cuando la empresa de transporte lo actualiza (si el seguimiento lo permite) |
| **Pedido cancelado** y **Reembolso** | Si cancelas o reembolsas |

No tienes que activar nada. Solo revisa estas 4 cosas para que salgan bonitos y en español:

1. **Idioma:** Ajustes → Idiomas → pon **Español** como idioma principal. Los correos salen en el idioma principal de la tienda, que ahora mismo es el inglés.
2. **Marca:** Ajustes → Notificaciones → Notificaciones para clientes → **Personalizar plantillas de correo** → sube el **logo** y pon el color **#FF6B2C**.
3. **Nombre del remitente:** Ajustes → Detalles de la tienda → cambia «My Store» por **jarandana**. Es lo que ve el cliente en su bandeja de entrada.
4. **Avisos a ti de cada pedido:** Ajustes → Notificaciones → **Notificaciones del personal** → añade `jarandanainfo@gmail.com` → «Nuevo pedido».

## 2. Bloques para pegar en los correos
Ruta: **Ajustes → Notificaciones → Notificaciones para clientes → (elige el correo) → Editar código**. Pega cada bloque **justo encima** de la línea que empieza por `{% if order_status_url %}` o, si no la encuentras, antes del bloque de «Resumen del pedido». Pulsa **Guardar** y después **Enviar correo de prueba** para verlo.

### a) Confirmación de pedido: «Qué pasa ahora»
```html
<table style="width:100%;margin:16px 0;border-collapse:separate;border-spacing:0;background:#FFF8EE;border-radius:14px;border-left:5px solid #FF6B2C">
  <tr><td style="padding:16px 18px;font-family:Arial,sans-serif;color:#1E2B37;font-size:15px;line-height:1.5">
    <strong style="font-size:17px">¡Gracias por confiar en jarandana! 🧡</strong><br>
    📦 Preparamos tu pedido y te avisamos por email cuando salga, con su número de seguimiento.<br>
    🚚 Plazo estimado: <strong>7 a 15 días laborables</strong>. Puede llegar en varios paquetes.<br>
    🛠️ Mientras tanto, echa un vistazo a <a href="{{ shop.url }}/pages/como-se-instala" style="color:#E4502E;font-weight:bold">cómo se instala en 1 minuto</a>.
  </td></tr>
</table>
```

### b) Confirmación de envío: consejo de instalación
```html
<table style="width:100%;margin:16px 0;border-collapse:separate;border-spacing:0;background:#E6FAF7;border-radius:14px;border-left:5px solid #19C2B0">
  <tr><td style="padding:16px 18px;font-family:Arial,sans-serif;color:#1E2B37;font-size:15px;line-height:1.5">
    <strong style="font-size:17px">Tu pedido va de camino 🚚</strong><br>
    El truco para que agarre bien: <strong>limpia con alcohol, presiona 30 segundos y espera 24 horas</strong> antes de mojarlo o cargarlo.
    <a href="{{ shop.url }}/pages/como-se-instala" style="color:#0E7490;font-weight:bold">Ver la guía</a>
  </td></tr>
</table>
```

### c) Pedido entregado: pedir la reseña ⭐
Pégalo en **«Pedido entregado»** (Delivered). Si tu transportista no marca las entregas, pégalo también al final de «Confirmación de envío».
```html
<table style="width:100%;margin:16px 0;border-collapse:separate;border-spacing:0;background:#FFF3C4;border-radius:14px">
  <tr><td style="padding:18px;font-family:Arial,sans-serif;color:#1E2B37;font-size:15px;line-height:1.5;text-align:center">
    <div style="font-size:26px">⭐⭐⭐⭐⭐</div>
    <strong style="font-size:18px">¿Qué tal te ha ido?</strong><br>
    Cuando lo tengas instalado, cuéntanos cómo ha quedado. Tu opinión (buena o mala) ayuda a otras personas y a nosotros a mejorar.<br>
    {% for line in line_items %}• {{ line.title }}<br>{% endfor %}
    <a href="{{ shop.url }}/pages/opiniones#escribir-resena" style="display:inline-block;margin-top:12px;background:#FF6B2C;color:#ffffff;text-decoration:none;font-weight:bold;padding:12px 26px;border-radius:999px">Dejar mi reseña</a>
    <br><span style="font-size:12px;color:#555">📸 ¿Tienes una foto? Respóndenos a este correo y la añadimos.</span>
  </td></tr>
</table>
```

## 3. Cómo funcionan las reseñas en la web
- **Dónde se escriben:**
  - La página **⭐ Opiniones** (`/pages/opiniones`), que está en el menú y en el pie, con el formulario abierto.
  - El botón «Escribir una reseña» de cada ficha de producto.
  - Enlaces directos:
    - `/pages/opiniones#escribir-resena` abre el formulario.
    - `/pages/opiniones?producto=balda-ducha-sin-taladrar` lo abre con el producto ya elegido.
- **Qué pasa al enviarla:** te llega por email a `jarandanainfo@gmail.com` con el nombre, la ciudad, el producto, las estrellas y el texto. El cliente ve el mensaje «¡Gracias! La publicaremos tras revisarla».
- **Cómo se publica:** Contenido → **Metaobjetos → Reseña → Añadir**. Rellena:
  - Nombre, ciudad, valoración, texto, producto y fecha.
  - **Compra verificada:** márcala si está en tus pedidos.
  - **Foto del cliente:** opcional.
  - **Producto de muestra gratis:** márcalo si se lo regalaste para probarlo. La web mostrará «🎁 Recibió el producto gratis para probarlo».

  Aparece al momento en la portada, en la ficha del producto y en Opiniones, con la media de estrellas.

## 4. ¿Y las reseñas «ficticias» para empezar? No
Publicar reseñas inventadas es **ilegal** en España y en la UE. Lo prohíben la Directiva Ómnibus y el art. 20 de la Ley de Consumidores, con multas de consumo que pueden ser de miles de euros. Además, Meta, TikTok y Google Shopping pueden bloquearte los anuncios si detectan reseñas falsas.

**Cómo conseguir las primeras reseñas de forma legal y rápida:**
1. **Probadores:** regala o vende a precio de coste 5-10 productos a amigos, familia o vecinos. Que escriban su opinión real y márcala como **«Producto de muestra gratis»**. Es legal porque se indica.
2. **Tus primeros clientes:** el bloque de «Pedido entregado» (apartado 2c) les pide la reseña automáticamente.
3. **Fotos y vídeos propios:** cuando te lleguen las muestras, graba la instalación real. Convence más que 10 reseñas.
4. **Mientras no haya reseñas,** la web muestra «Todavía no hay reseñas publicadas: ¡estrena el muro!» en lugar de un hueco vacío.

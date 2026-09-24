# 15 · Cambios de la noche (24-09-2026) y lo que te toca a ti

## 1. Publica el tema nuevo
Ve a **Tienda online → Temas** y publica **«jarandana v6 (publicar este)»**. El que tienes publicado («jarandana FINAL») no se puede editar por la API mientras esté publicado, así que todos los cambios están en la copia v6.

## 2. Qué hay nuevo en la web
| Parte | Cambio |
|---|---|
| **Menú** | Botones tipo pastilla con emoji. 🔥 Ofertas (degradado naranja-rosa que late), ✨ Novedades (amarillo), 🚿 Baño, 🍽️ Cocina, Todo, 🛠️ Cómo se instala y Nosotros. En móvil hay una **barra de botones deslizable** bajo el logo. Se quita «Inicio», que ya es el logo. |
| **Cómo se instala** | Rediseñado: 3 tarjetas con **foto real de cada paso** (creadas con IA), número de color, tiempo (1 min · 30 s · 24 h), flechas entre pasos, recuadros **«Sí funciona en / No funciona en»** y 2 botones. |
| **Página «Cómo se instala»** | Tiene plantilla propia: banner, pasos, vídeo, preguntas rápidas, ofertas y contacto. |
| **Cinta animada** | 2 cintas que se desplazan con las ventajas y las ofertas, una en negro y otra en naranja. |
| **Aviso de cookies** | Botones **Aceptar todas**, **Rechazar** y **Configurar**, con el mismo tamaño para aceptar y rechazar, como pide la AEPD. Guarda la elección y se lo comunica a Shopify, que así no activa la analítica ni la publicidad sin permiso. Se reabre desde «🍪 Configurar cookies» en el pie. |
| **Botón ↑** | Aparece al bajar para volver arriba. |
| **Pie de página** | Nuevo menú **Legal**: Aviso legal, Condiciones de venta, Privacidad, Cookies, Devoluciones y Configurar cookies. |

## 3. Textos legales (páginas publicadas)
- `/pages/aviso-legal` (LSSI)
- `/pages/politica-de-privacidad` (RGPD). Incluye que la dirección se comparte con proveedores fuera de la UE para poder entregar el pedido.
- `/pages/condiciones-de-venta`: precios con IVA, pago, envío, desistimiento, **garantía legal de 3 años** y reclamaciones.
- `/pages/politica-de-cookies`
- `/pages/devoluciones`: **corregida**. Antes decía que los productos instalados no se podían devolver, y eso no es legal. Ahora explica que se puede descontar la pérdida de valor (art. 108 TRLGDCU). También incluye el **modelo de formulario de desistimiento**, que es obligatorio.
- `/pages/envios`: añadido el apartado de incidencias y el plazo de 30 días.

### ⚠️ Rellena estos huecos (en Tienda online → Páginas)
En **Aviso legal, Privacidad, Condiciones de venta, Cookies y Devoluciones** hay 3 huecos:
- `[TITULAR]`: tu nombre y apellidos, o la razón social si es empresa.
- `[NIF]`
- `[DIRECCIÓN]`: calle y número. La ciudad ya está puesta: 18600 Motril (Granada).

### ⚠️ Políticas de Shopify (Ajustes → Políticas)
La API no me deja escribir ahí (falta el permiso `write_legal_policies`). Las políticas de esa pantalla son las que se enlazan en el **pago**. Copia los textos de [`shopify/legal/politicas.json`](../shopify/legal/politicas.json) en cada una, o pulsa «Crear desde plantilla» y cambia el idioma a español:
- Reembolso = `REFUND_POLICY`
- Privacidad = `PRIVACY_POLICY`
- Términos del servicio = `TERMS_OF_SERVICE`
- Envío = `SHIPPING_POLICY`
- Información de contacto = `CONTACT_INFORMATION`
- Aviso legal = `LEGAL_NOTICE`

Ahora mismo la de privacidad está en inglés y a nombre de «My Store».

> Estos textos son una plantilla completa para una tienda online en España. Pide a un gestor o abogado que les dé un vistazo antes de vender en serio.

## 4. Lo que sigue pendiente (solo lo puedes hacer tú en el admin)
1. **Publicar** el tema v6.
2. **Nombre de la tienda:** cambia «My Store» por **jarandana** en Ajustes → Detalles de la tienda. Sale en correos, facturas y en la política de privacidad automática.
3. **Idioma:** pon **español** como idioma principal en Ajustes → Idiomas.
4. **Envíos:** pon 3,95 € y gratis desde 35 € en Ajustes → Envíos. La web y las FAQ ya lo dicen.
5. **Pagos:** activa Shopify Payments (tarjeta, Apple Pay, Google Pay) y PayPal en Ajustes → Pagos.
6. **Cookies de Shopify:** en Ajustes → Privacidad del cliente, deja **desactivado** el banner de Shopify o, si lo prefieres, actívalo; nuestro aviso se oculta solo si detecta el de Shopify.
7. **Contraseña:** quítala cuando quieras abrir la tienda.
8. **Seguridad:** revoca los tokens `shpat_` que compartiste en el chat.
9. **Permisos para que haga más cosas yo:**
   - **Gmail:** dale permiso de enviar en claude.ai → Conectores, y así escribo a los proveedores.
   - **Políticas de Shopify:** con el permiso `write_legal_policies` las relleno yo.

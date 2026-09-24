# 18 · Enlazar los productos con DSers (10-15 minutos, una sola vez)

Los **12 productos ya están en tu tienda** y se pueden comprar. Lo que falta es decirle a DSers **qué artículo de AliExpress corresponde a cada producto**. Ese enlace se hace dentro de DSers. No tiene API y no puedo hacerlo desde aquí. Cuando esté hecho, los pedidos se tramitan con un clic.

## 1. Ajustes de DSers (una vez)
1. **Cuenta de AliExpress:** DSers → Ajustes (Setting) → **Account → Link to AliExpress**. Inicia sesión con tu cuenta de AliExpress, que es la que pagará los pedidos.
2. **Envío por defecto:** Setting → **Shipping** → país **Spain** → método **«AliExpress Standard Shipping»** o **«AliExpress Selection Standard»**. Son los de 7-15 días con seguimiento.
3. **Nota al proveedor:** Setting → **Other → Message to supplier**:
   `Dropshipping order. Please do NOT include invoices, prices or promotional material. Thank you!`
4. **Seguimiento automático:** Setting → **Tracking → Sync tracking number to Shopify: ON**, y activa que Shopify avise al cliente.
5. **AutoDS:** déjalo instalado pero **sin Auto-order**, o desinstálalo. Si no, podría comprar el pedido otra vez.

## 2. Enlazar cada producto (Mapping)
DSers → **Products → My Products**. Si no ves tus productos, pulsa **«Import from Shopify»** o **«Sync Shopify products»**. En cada producto pulsa el icono de **Mapping → Basic Mapping**, pega el enlace de AliExpress y elige, para cada variante de tu tienda, la variante del proveedor que corresponde. Después pulsa **Save**.

| Producto de tu tienda | Enlace de AliExpress (proveedor) | Cómo enlazar las variantes |
|---|---|---|
| Balda (Negro mate, Blanco, Gris) | https://www.aliexpress.com/item/1005007286601018.html | Mismo color |
| Rasqueta | https://www.aliexpress.com/item/1005006352958855.html | Variante **con soporte** |
| Ganchos (2 o 4) | https://www.aliexpress.com/item/3256808858857869.html | 2 ganchos = 2 pcs · 4 ganchos = 4 pcs |
| Kit Fregadero (Negro, Blanco) | https://www.aliexpress.com/item/1005006997228432.html | Mismo color |
| Esquinera Doble (Blanco, Negro, Plata) | https://www.aliexpress.com/item/1005008539345371.html | Mismo color, **2 alturas** |
| Bayetas (8) | https://www.aliexpress.com/item/1005005911753573.html | 8 pcs · 30×30 |
| Recambio de adhesivos | https://www.aliexpress.com/item/1005004896437481.html | 3 m |
| Grifo 1080° (1 o 2) | https://www.aliexpress.com/item/3256806984740623.html | 1 unidad = 1 pc. **2 unidades: usa «Bundle Mapping»** con cantidad 2 del mismo artículo |
| Luz LED (1 o 2) | https://www.aliexpress.com/item/1005009195805856.html | «White Light 1PC». **2 luces: Bundle Mapping ×2** |
| Alcachofa (Plata, Negro) | https://www.aliexpress.com/item/1005009452514317.html | Mismo color |
| Dispensador de pasta (Negro, Gris) | https://www.aliexpress.com/item/1005008311587065.html | Mismo color |
| **Kit Ducha** (Negro mate, Blanco, Gris) | Balda + Rasqueta + Ganchos | **Bundle Mapping** con 3 artículos: balda del mismo color + rasqueta con soporte + ganchos 2 pcs. Llegará en 3 paquetes (ya se avisa en la web) |

Antes de guardar, **comprueba el precio**. Si el precio del proveedor ha subido mucho respecto a la tabla del doc 13, avísame y recalculo el margen.

## 3. Cuando entra un pedido
1. Shopify te avisa por email y el pedido aparece en DSers → **Orders → Awaiting order**.
2. Pulsa **«Place order to AliExpress»**. DSers rellena la dirección del cliente y la variante.
3. **Paga** en AliExpress. Puedes dejar la tarjeta guardada para pagar varios pedidos a la vez.
4. Cuando el proveedor envía, el número de seguimiento pasa solo a Shopify y el cliente recibe el correo «Tu pedido va de camino».

## 4. Si prefieres que sea 100 % automático
AutoDS con plan de pago y **Auto-order** hace el paso 3 por ti. Cuesta una cuota mensual y necesitas saldo en AutoDS. Con los primeros pedidos, DSers gratis es suficiente.

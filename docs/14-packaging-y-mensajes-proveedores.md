# 14 · Packaging jarandana y mensajes a los proveedores

## 1. Qué hay en [`packaging/`](../packaging/)
| Archivo | Para qué |
|---|---|
| [`packaging-jarandana.pdf`](../packaging/packaging-jarandana.pdf) | Todo en un PDF: caras frontales, pegatina, tarjeta y troqueles. **Es lo que mandas al proveedor.** |
| `cajas/<producto>.svg` | Troquel plano de cada caja, vectorial para imprenta (**rojo = corte**, **azul = hendido**). |
| `frontales/<producto>.svg` | Solo la cara frontal, para enseñar el diseño rápido. |
| `png/` | Lo mismo en PNG, para mandar por el chat de AliExpress o por WhatsApp. |
| `pegatina.svg` y `tarjeta-gracias.svg` | Pegatina redonda de 8 cm para cerrar la bolsa o caja, y tarjeta A6 de gracias. |
| `generar_packaging.py` | Script que genera todo. Cambia textos o medidas en `PRODUCTOS` y ejecuta `python3 packaging/generar_packaging.py`. |

**Diseño:**
- Crema y tinta de la marca, con un color por línea: **Baño** turquesa, **Cocina** naranja y **Novedad** rosa.
- La cara frontal lleva el logo, el nombre, la frase, 3 ventajas y el sello "SIN TALADRAR".
- La trasera lleva los 3 pasos de instalación, el aviso de superficies y el contenido de la caja.
- La tapa dice "¡Hola! Tu casa te lo va a agradecer".

⚠️ **Antes de imprenta:**
1. **Medidas:** son **orientativas**. Pide al proveedor la medida de su caja o del producto y cámbiala en `PRODUCTOS` (ancho × fondo × alto en mm).
2. **Bloque legal de la trasera:** rellénalo con **tu nombre o empresa, tu dirección, tu email, el país de fabricación y el lote**. El Reglamento UE de Seguridad General de Productos (GPSR) exige un responsable en la UE en el envase.
3. **Imprenta:** ajusta el sangrado (3 mm) con la imprenta o el proveedor. Casi todos te pasan su propio troquel y colocan encima tu diseño.

## 2. Qué es realista con dropshipping
| Opción | Coste y mínimo habitual | Cuándo |
|---|---|---|
| **Pegatina + tarjeta de gracias** metidas por el proveedor | Barato; muchos lo hacen desde pocos pedidos | **Ahora**, desde el primer pedido |
| **Caja personalizada por producto** | Suele pedirse un mínimo de 300-1.000 cajas por modelo | Cuando un producto venda de forma constante |
| **Agente o almacén** (CJdropshipping y similares) que guarda tus cajas y empaqueta | Tú compras las cajas; ellos las montan en cada pedido | Cuando tengas 2 o 3 productos que se venden solos |

Los mínimos son rangos típicos del sector: **confírmalos con cada proveedor**, que es justo lo que pregunta el mensaje.

## 3. Mensaje para cada proveedor (chat de AliExpress → "Mensaje" en la ficha)
Las tiendas de AliExpress **no tienen email público**: solo se les puede escribir por el chat. Yo no tengo acceso a ese chat y tu Gmail conectado no me deja enviar ni crear borradores (falta el permiso). Copia y pega este mensaje cambiando **[PRODUCTO]** e **[ID]** y adjunta los PNG de `packaging/png/`.

```
Hello! I run jarandana, a home brand in Spain, and I want to sell your item [ID] ([PRODUCTO]) regularly.
1. Do you offer dropshipping (you ship each order directly to my customer in Spain)?
2. Can you ship with NO invoice, price or promotional material inside the parcel?
3. Can you add my branded sticker and a small thank-you card to each parcel? (I will send the files)
4. Can you pack the product in my own custom box? What is the MOQ and price per box? I attach my design.
5. Real delivery time to Spain? Do you have an EU warehouse?
6. Unit price for 20 / 50 / 100 orders per month?
7. Can you send me one sample first?
Thank you!
```

| Producto | Proveedor | Escribir aquí |
|---|---|---|
| Balda | Trustworthy Home Furnishing Store | [1005007286601018](https://www.aliexpress.com/item/1005007286601018.html) |
| Rasqueta | Shop1102896187 Store | [1005006352958855](https://www.aliexpress.com/item/1005006352958855.html) |
| Ganchos y Kit Fregadero | Stone's Store | [3256808858857869](https://www.aliexpress.com/item/3256808858857869.html) · [1005006997228432](https://www.aliexpress.com/item/1005006997228432.html) |
| Esquinera Doble | Sunpid Home Store | [1005008539345371](https://www.aliexpress.com/item/1005008539345371.html) |
| Bayetas | NO-7 Best Store | [1005005911753573](https://www.aliexpress.com/item/1005005911753573.html) |
| Recambio adhesivos | Global Shell 18 Store | [1005004896437481](https://www.aliexpress.com/item/1005004896437481.html) |
| Grifo 1080° | Stone's Store | [3256806984740623](https://www.aliexpress.com/item/3256806984740623.html) |
| Luz LED | Willed Store | [1005009195805856](https://www.aliexpress.com/item/1005009195805856.html) |
| Alcachofa | Bathware Specialty Store | [1005009452514317](https://www.aliexpress.com/item/1005009452514317.html) |
| Dispensador | MENGNI Official Store | [1005008311587065](https://www.aliexpress.com/item/1005008311587065.html) |

Stone's Store tiene 3 de tus productos: **pregunta en un solo mensaje** por los tres y por un precio conjunto.

### Email para Shenzhen Kean Silicone (info@keansilicone.com, alternativa para el Kit Fregadero)
Asunto: `Dropshipping + custom packaging inquiry – silicone sink kit – Spain`
```
Hello Kean Silicone team,
I run jarandana, a new home brand in Spain (bathroom and kitchen accessories that install without drilling). I'm interested in a silicone kitchen sink kit: push-type soap dispenser with sponge holder.
1. Do you offer dropshipping to Spain, or only bulk orders? If bulk, what is the MOQ?
2. Can you pack each unit in my own custom branded box (artwork and dieline ready), or add my sticker and thank-you card?
3. MOQ and price for custom printed boxes, and unit price at 100 / 300 / 500 pcs?
4. Can you ship without invoices or promotional material inside?
5. Real delivery time to Spain, and any EU warehouse?
6. Samples: cost and shipping time?
7. Documentation to sell in the EU (food-contact / material certificates)?
Best regards,
jarandana (Spain)
```

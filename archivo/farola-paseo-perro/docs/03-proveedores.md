# 03 · Proveedores, validación, mensajes y negociación

> **Reglas de este documento**
> - Nada inventado. Si un dato no apareció en una fuente pública, pone **NO VERIFICADO** + enlace oficial para comprobarlo.
> - Contactos (emails/teléfonos) **solo** si aparecen publicados por la empresa o en un directorio empresarial; se indica la fuente. Aun así, **confírmalos en la web oficial antes de escribir** (los datos cambian).
> - Clasificación: **PROVEEDOR VERIFICADO** (empresa identificable con datos registrales/certificaciones publicadas) · **FABRICANTE** · **MARKETPLACE** · **PLATAFORMA DE SOURCING/DROPSHIPPING**.
> - Limitación: desde este entorno no se pudieron abrir las fichas de producto de CJ, AliExpress, Alibaba ni BigBuy (bloqueo de red). **Precios por producto = NO VERIFICADO** salvo donde se indica.

---

## 0. Mapa de proveedores y estrategia

| Prioridad del brief | Opción | Para qué la usamos | Tipo |
|---|---|---|---|
| 1. España | **BigBuy** (Valencia) | Backup/benchmark genérico; su catálogo es de marcas de terceros → no permite nuestra marca | Plataforma dropshipping (mayorista) |
| 1. España | **Freedog Import SL** (Berga, BCN) · **Arquivet SL** (Les Franqueses del Vallès, BCN) · **Mascoteca** | Mayoristas de marcas propias (Clean Street, Pipi Clean…). Sirven como **plan B de stock rápido** y para comparar calidad, **no para marca propia** | Proveedor verificado (mayorista/fabricante nacional) |
| 2. Europa | **Syncee**, **Spocket** | Buscar proveedores UE de dispensadores/bolsas para envío 2-5 días | Plataforma de sourcing |
| 3. China con almacén UE | **CJdropshipping** (almacén en Alemania; permite stock privado en UE; packaging personalizado desde 1 ud) | **Proveedor principal de lanzamiento** (test) | Plataforma de dropshipping/sourcing |
| 4. China | **Fabricantes vía Alibaba/web** (Kean Silicone, Chongjia, Aimazing, Orizon…) | **Marca propia (private label)** cuando haya ventas: logo en producto, colores propios, caja | Fabricante |
| — | AliExpress vía DSers | Solo para **pedir muestras rápidas** y comparar; no como proveedor principal | Marketplace |

**Recomendación de arquitectura**
1. **Fase test (mes 1-2):** CJdropshipping como agente (sourcing de los 7 productos, packaging con logo desde 1 ud, envío desde almacén UE cuando haya stock, o desde China). Pedir que CJ **cotice los productos a sus fábricas** (su servicio de sourcing) y a la vez pedir presupuesto directo a los fabricantes de abajo.
2. **Fase validación (≥ 30-50 pedidos/semana):** pedido de stock de 200-500 uds de los 3 principales a un fabricante (Kean/Chongjia/Aimazing) con logo, enviado al **almacén UE de CJ** o a un 3PL español. Plazos de 2-4 días a España.
3. **Nunca** elegir por precio más bajo sin muestra.

---

## 1. Tablas por producto

### P1 — Botella Chorro (limpia-pis)

| Campo | Opción A | Opción B | Opción C | Opción D (plan B España) |
|---|---|---|---|---|
| PROVEEDOR | **Shenzhen Kean Silicone Product Co., Ltd.** | **CJdropshipping** | Yiwu Miaoshu (vía Alibaba) | **Freedog Import SL** (botella Clean Street) |
| TIPO | FABRICANTE · PROVEEDOR VERIFICADO (auditado BSCI, Sedex, ISO 9001 según su web) | PLATAFORMA DROPSHIPPING/SOURCING | FABRICANTE/TRADING (Alibaba) — sin verificar | PROVEEDOR VERIFICADO (mayorista de marca propia) |
| ENLACE | [keansilicone.com](https://www.keansilicone.com/) · [contacto](https://www.keansilicone.com/contact.html) · [botella mascota](https://keantravel.com/products/portable-pet-water-bottle) | [Buscar en CJ](https://cjdropshipping.com/search/dog%20pee%20bottle.html) | [Alibaba – proveedores botella mascota](https://www.alibaba.com/supplier/alibaba-pet-water-bottle-dual-dispenser-supplier-price.html) | [freedog.es](https://freedog.es/es/accesorios) · [Clean Street en Miscota](https://www.miscota.es/perros/freedog/cleanstreet) |
| PRECIO | NO VERIFICADO | NO VERIFICADO | **1,50 $/ud** (botella PP "eco-PP", según página de Alibaba) | NO VERIFICADO (precio mayorista) |
| MOQ | NO VERIFICADO | 1 ud (dropshipping) | **200 uds** (según Alibaba) | NO VERIFICADO |
| VARIANTES/COLORES | Silicona en colores Pantone a medida (fabricante de silicona) — confirmar | Según listing | NO VERIFICADO | Rojo y otros (listing Amazon muestra "Red") |
| ALMACÉN | China (Shenzhen) | China + UE (Alemania) | China | España |
| PAÍS ENVÍO | China | China o Alemania | China | España |
| TIEMPO ENVÍO | NO VERIFICADO (marítimo/aéreo a negociar) | 3-7 días desde almacén alemán en DE ([blog CJ](https://cjdropshipping.com/blogs/dropshipping-knowledge/Dropshipping-in-Germany)); 7-15 días desde China (declarado por CJ) — **a España: NO VERIFICADO** | NO VERIFICADO | NO VERIFICADO (nacional) |
| COSTE ENVÍO | NO VERIFICADO | NO VERIFICADO (calculadora en CJ) | NO VERIFICADO | NO VERIFICADO |
| BRANDING | Sí (OEM/ODM, logo) — confirmar MOQ de logo | Sí: logo/packaging/insert desde 1 ud; stickers desde 0,30 $, cajas rígidas 2 $+ ([CJ](https://cjdropship.com/custom-packaging-service-3/), [review](https://cjdropshipping.com/customPackaging)) | Posible (Alibaba) — NO VERIFICADO | **No** (es su marca) |
| PACKAGING PERSONALIZADO | Sí (fabricante) — MOQ NO VERIFICADO | Sí | NO VERIFICADO | No |
| MUESTRA | NO VERIFICADO — pedir | Sí (pedido de 1 ud) | NO VERIFICADO | Comprar en Miscota/Amazon |
| CONTACTO/EMAIL | **info@keansilicone.com** · op001@keansilicone.com (publicados; fuente: [contacto Kean](https://www.keansilicone.com/contact.html)) | Agente asignado tras registrarse | Vía chat Alibaba | **info@freedog.es** (fuente: [Empresite](https://empresite.eleconomista.es/FREEDOG-IMPORT.html)) |
| TELÉFONO/WHATSAPP | +86 189 2640 3849 · +86 755 8969 6258 (publicados). WhatsApp: NO VERIFICADO | — | — | 938 220 780 |
| OBSERVACIONES | Fundada 08-02-2006; Longgang, Shenzhen. Fabrica botellas de perro, dispensadores y "silicone dog poop carrier" → **puede hacer P1, P2 y P6** en el mismo pedido y mismos colores | Proveedor de arranque. Trustpilot ~4,9 con ~13.000 reseñas, pero con quejas de roturas de stock, reembolsos y calidad variable ([Trustpilot](https://www.trustpilot.com/review/cjdropshipping.com)) | Precio de referencia útil; **proveedor sin validar** | Solo para comparar calidad o stock urgente |

### P2 — Dispensador Clic

| Campo | Opción A | Opción B | Opción C |
|---|---|---|---|
| PROVEEDOR | **Yancheng Chongjia Technology Co., Ltd. (Chongjia Pet)** | **Shenzhen Kean Silicone** | **CJdropshipping** |
| TIPO | FABRICANTE (bolsas + dispensadores) | FABRICANTE | PLATAFORMA |
| ENLACE | [chongjiapet.com](https://www.chongjiapet.com/) · [contacto](https://www.chongjiapet.com/contact-us/) · [Made-in-China](https://ycchongjia.en.made-in-china.com/company-Yancheng-Chongjia-Technology-Co-Ltd-.html) | [Dispensador silicona](https://www.keansilicone.com/silicone_pet_product/Dog_poop_bag_dispenser_2549.html) | [Buscar en CJ](https://cjdropshipping.com/search/silicone%20poop%20bag%20dispenser.html) |
| PRECIO | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |
| MOQ | NO VERIFICADO | NO VERIFICADO | 1 ud |
| VARIANTES/COLORES | NO VERIFICADO | Colores a medida (silicona) — confirmar | Según listing |
| ALMACÉN | China (Jianhu, Yancheng, Jiangsu; oficina en Shanghái) | China | China/UE |
| TIEMPO/COSTE ENVÍO | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |
| BRANDING / PACKAGING | Sí, OEM/ODM "full customization" (según su web) | Sí ("Custom Dog Poop Bag Dispenser") | Sí |
| MUESTRA | NO VERIFICADO | NO VERIFICADO | Sí |
| CONTACTO | **info@chongjiapet.com** · +86 147 2111 9769 (publicados en su web) | info@keansilicone.com | Agente |
| OBSERVACIONES | Desde 2009, especializada en bolsas, dispensadores y rollos → **mismo proveedor para P2 + P3** (ahorra envío y asegura compatibilidad de rollo) | Mismo color que P1 y P6 si se fabrican juntos | — |

### P3 — Bolsas Farola XL

| Campo | Opción A | Opción B | Opción C (solo si se quiere versión certificada compostable) |
|---|---|---|---|
| PROVEEDOR | **Chongjia Pet** | **CJdropshipping** | **ORIZON** / Weifang Golden Grain Bio Material / ShinHigh |
| TIPO | FABRICANTE | PLATAFORMA | FABRICANTES |
| ENLACE | [Premium Dog Poop Bags OEM](https://www.chongjiapet.com/premium-dog-poop-bags-kraft-box-270-counts-oem-odm-available-product/) | [Buscar](https://cjdropshipping.com/search/dog%20poop%20bags.html) | [orizonbags.com](https://orizonbags.com/private-label-compostable-dog-poop-bags/) · [Golden Grain](https://53c43e0bcbce31e3.en.made-in-china.com/product-group/VqIfLBavgPRi/Compostable-Dog-Poop-Bags-catalog-1.html) · [biopakwell.com](https://biopakwell.com/pet-waste-bags/) |
| PRECIO | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |
| MOQ | NO VERIFICADO | 1 | **ORIZON: desde 10.000 packs; Golden Grain: 10.000 rollos** (según sus páginas) |
| CERTIFICACIONES | Declara EN 13432, ASTM D6400, OK Compost en su web → **pedir certificado a nombre del producto concreto** | NO VERIFICADO | ORIZON y Golden Grain declaran EN 13432 (TÜV) |
| ALMACÉN / ENVÍO | China / NO VERIFICADO | China/UE / NO VERIFICADO | China / NO VERIFICADO |
| BRANDING | Sí (caja kraft, impresión) | Sí (packaging) | Sí (impresión personalizada) |
| CONTACTO | info@chongjiapet.com | Agente | ORIZON: **info@orizonbio.com** (publicado); Golden Grain y ShinHigh: vía web — NO VERIFICADO |
| OBSERVACIONES | Recomendado. Lanzar **bolsa convencional opaca y gruesa sin claims ambientales** | Para test | MOQ alto → solo fase 3. **Sin certificado a nombre del producto no se puede decir "compostable"** ([Directiva 2024/825](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32024L0825)) |

### P4 — Bolsa de Premios Imán

| Campo | Opción A | Opción B | Opción C |
|---|---|---|---|
| PROVEEDOR | **CJdropshipping** | **Shenzhen Kean Silicone** | AliExpress (vía DSers) |
| TIPO | PLATAFORMA | FABRICANTE | MARKETPLACE |
| ENLACE | [Buscar](https://cjdropshipping.com/search/silicone%20dog%20treat%20pouch.html) | [keansilicone.com](https://www.keansilicone.com/) | [AliExpress](https://www.aliexpress.com/w/wholesale-silicone-treat-pouch-for-dog.html) |
| PRECIO | NO VERIFICADO | NO VERIFICADO (confirmar que lo fabrican) | NO VERIFICADO. Referencia retail EE. UU.: 8,71 $ en Walmart ([Walmart](https://www.walmart.com/ip/2201180571)) |
| MOQ | 1 | NO VERIFICADO | 1 |
| RESTO (almacén, envío, branding, muestra, contacto) | Ver P1 | Ver P1 | Envío desde China; sin branding; muestra = pedido normal |
| OBSERVACIONES | — | Si lo fabrican, unificar color con P1/P2/P6 | Solo para muestras comparativas |

### P5 — Bandolera Paseo

| Campo | Opción A | Opción B | Opción C |
|---|---|---|---|
| PROVEEDOR | **Aimazing (Guangzhou) Co., Ltd.** | **CJdropshipping** | Spocket / Syncee (proveedores UE) |
| TIPO | FABRICANTE (OEM/ODM bolsos y artículos para mascota) | PLATAFORMA | PLATAFORMA DE SOURCING |
| ENLACE | [doghandbag.com](https://doghandbag.com/) · [contacto](https://aimazingbag.com/contact/) · [about](https://aimazingbag.com/about/) | [Buscar](https://cjdropshipping.com/search/dog%20walking%20bag.html) | [Syncee pet](https://syncee.com/page/sell-wholesale-pet-supplies/) · [Spocket pet](https://www.spocket.co/dropship/pets) |
| PRECIO / MOQ | NO VERIFICADO | NO VERIFICADO / 1 | NO VERIFICADO |
| ALMACÉN | China (Shiling, Guangzhou) | China/UE | UE (según proveedor) |
| BRANDING | Sí (OEM: logo, tejido, colores) | Parcial (etiqueta/packaging) | Normalmente no |
| MUESTRA | NO VERIFICADO — pedir muestra de desarrollo | Sí | Según proveedor |
| CONTACTO | Formulario web (dicen responder en 1 h); email y WhatsApp: **NO VERIFICADO** | Agente | Plataforma |
| OBSERVACIONES | 200+ trabajadores y 26+ años según su web. Ideal para una bandolera **diseñada por nosotros** (funda de botella + salida de bolsas) | Test con modelo genérico | Buscar "dog walking bag" con stock UE |

### P6 — Portabolsa Sin Manos

| Campo | Opción A | Opción B |
|---|---|---|
| PROVEEDOR | **Shenzhen Kean Silicone** ("Silicone dog poop carrier") | **CJdropshipping** |
| ENLACE | [Silicone dog poop carrier](https://www.keansilicone.com/dog-water-bottle/Silicone_dog_poop_carrier_2544.html) | [Buscar](https://cjdropshipping.com/search/dog%20poop%20bag%20holder%20carrier.html) |
| PRECIO / MOQ | NO VERIFICADO | NO VERIFICADO / 1 |
| RESTO | Ver P1 | Ver P1 |
| OBSERVACIONES | Mismo fabricante que P1/P2 → colores idénticos | — |

### P7 — Botella-Bebedero 2 en 1

| Campo | Opción A | Opción B | Opción C |
|---|---|---|---|
| PROVEEDOR | **Shenzhen Kean Silicone** (Portable Pet Water Bottle) | **CJdropshipping** | Chengdu Daruhui (acero inox 3 en 1, grabado) |
| ENLACE | [keantravel.com](https://keantravel.com/products/portable-pet-water-bottle) | [Buscar](https://cjdropshipping.com/search/dog%20water%20bottle.html) | [Alibaba](https://www.alibaba.com/supplier/alibaba-pet-water-bottle-dual-dispenser-supplier-price.html) |
| PRECIO / MOQ | NO VERIFICADO | NO VERIFICADO / 1 | NO VERIFICADO |
| OBSERVACIONES | Material en contacto con agua de bebida → **pedir declaración de conformidad para contacto con alimentos (Reglamento (CE) 1935/2004)** y test LFGB | — | Versión premium futura |

### Proveedores España/UE de referencia (plan B y benchmark)

| Proveedor | Tipo | Datos publicados | Uso |
|---|---|---|---|
| **BigBuy** (Valencia) | Plataforma dropshipping/mayorista | Fundada 2010; Trustpilot 4,1 (8.000+ reseñas) con quejas de roturas de stock; packs de 69-120 €/mes + alta 90 € según reseñas ([Minea](https://www.minea.com/dropshipping-provider/best-dropshipping-suppliers/bigbuy-reviews), [Trustpilot](https://www.trustpilot.com/review/bigbuy.eu)). Categoría mascotas: [bigbuy.eu/es/mascotas](https://www.bigbuy.eu/es/mascotas.html) | **No recomendado** para esta marca (cuota mensual + productos de terceros) |
| **Arquivet SL** | Fabricante/distribuidor (desde 1991) | C/ Mas Pujol 41, Pol. Ind. Congost, 08520 Les Franqueses del Vallès; tel. 938 402 066; **ventas@arquivet.com**; CIF B59180125 ([Interempresas](https://www.interempresas.net/Mascotas/FeriaVirtual/Contacto-Arquivet-S-L-220430.html), [eInforma](https://www.einforma.com/informacion-empresa/arquivet)) | Benchmark / stock urgente |
| **Freedog Import SL** | Mayorista (Berga) | tel. 938 220 780; info@freedog.es ([Empresite](https://empresite.eleconomista.es/FREEDOG-IMPORT.html)) | Benchmark |
| **Mascoteca** | Distribuidor con dropshipping (9.000 referencias) | Condiciones: NO VERIFICADO → [formulario](https://mascoteca.es/distribuidor-dropshipping-productos-mascotas/) | Plan B |

---

## 2. Validación de proveedores (checklist antes de elegir el principal)

| Comprobación | Kean Silicone | Chongjia | Aimazing | CJdropshipping |
|---|---|---|---|---|
| Reviews | Buscar en Alibaba/Made-in-China su puntuación → **NO VERIFICADO** | NO VERIFICADO | NO VERIFICADO | Trustpilot ~4,9/13k, con quejas reales de stock/calidad/reembolsos |
| Antigüedad | 2006 (su web) | 2009 (su web) | 26+ años (su web) | Operando desde 2014 aprox. — NO VERIFICADO |
| Información empresarial | Razón social, dirección y certificaciones BSCI/Sedex/ISO 9001 publicadas | Razón social y planta en Jianhu publicadas | Razón social, planta en Shiling publicadas | Empresa conocida |
| Política de devoluciones/defectos | Preguntar (mensaje §3) | Preguntar | Preguntar | Política publicada en su web — leer antes de pagar |
| Warehouse | China | China | China | China + UE (Alemania) |
| Procesamiento | Preguntar | Preguntar | Preguntar | 1-3 días típicos — NO VERIFICADO |
| Tracking | Preguntar | Preguntar | Preguntar | Sí |
| Integración Shopify | No (fabricante) → vía CJ o 3PL | No | No | **Sí (app CJ para Shopify)** |
| Branding | Sí | Sí | Sí | Sí (desde 1 ud) |
| Señales de alerta | Verificar que el email del chat coincide con el dominio oficial; no pagar a cuentas personales | Idem | Idem | Stock que desaparece → tener proveedor B |

**Banderas rojas en cualquier proveedor:** pide pago por Western Union o a cuenta personal; no acepta muestra; no da nombre de empresa que coincida con la licencia; certificado "EN 13432" sin número o de otra empresa; fotos de producto robadas de Amazon.

---

## 3. Mensaje a proveedores

### 3.1 En inglés (fabricantes chinos y CJ)

```
Subject: Private label inquiry – dog walking accessories (EU brand, Spain) – [Product name]

Hello [Name],

I'm [Your name], founder of FAROLA, a new dog-walking accessories brand based in Spain,
selling online to Spain and Italy (EU). We are selecting a long-term manufacturing partner
for the following item(s):

  – [Product: e.g. silicone dog pee-cleaning bottle 450-500 ml with carabiner and leak-proof nozzle]
  – [Product 2 …]

Could you please share:
 1. Unit price for dropshipping (1 unit/order) and volume prices for 200 / 500 / 1,000 / 3,000 units.
 2. MOQ per colour and MOQ for logo printing / custom Pantone colours.
 3. Production lead time and order processing time for in-stock items.
 4. Shipping time and cost per unit to Spain (door-to-door) and to Italy / other EU countries,
    and whether you have (or work with) a warehouse in the EU.
 5. Tracking: carrier used and whether tracking works end-to-end in Spain.
 6. Packaging options: polybag, printed box, kraft box, insert card – costs and MOQs.
 7. Private label: logo on product (debossed / printed), custom colours, custom packaging.
 8. Samples: cost, shipping cost and time; is the sample cost refunded on the first order?
 9. Defective products: what is your policy (replacement, refund, credit)? Acceptable defect rate?
10. Returns policy for customers in the EU.
11. Can you integrate with Shopify or with an agent (e.g. CJdropshipping) for automatic order processing?
12. Documents for the EU market: material specs, REACH / LFGB or food-contact declaration
    (for water bottles), test reports, and your willingness to support GPSR requirements
    (manufacturer name/address on product or packaging).
13. For bags only: certificates (EN 13432 / OK Compost) issued for THIS specific product,
    with certificate number.

Our plan: start with samples this month, then a first stock order of 200-500 units per SKU,
growing monthly. We value quality and reliability over the lowest price.

Thank you,
[Name] – FAROLA
[email] · [web] · [WhatsApp]
```

### 3.2 En español (proveedores españoles)

```
Asunto: Solicitud de condiciones de distribución / dropshipping – tienda online de accesorios de paseo

Hola, equipo de [Empresa]:

Soy [Nombre], de FAROLA, tienda online especializada en accesorios de paseo para perros
(España e Italia). Nos interesa trabajar con [producto/s]. ¿Podrían indicarnos?

1. Precio de distribuidor y precio por volumen (50/100/250 uds) y si ofrecen dropshipping.
2. Pedido mínimo, plazo de preparación y plazo/coste de envío a península, Baleares y Canarias.
3. Envío a otros países de la UE (Italia/Portugal).
4. Número de seguimiento y transportista.
5. ¿Es posible envío en caja neutra o con inserto de nuestra marca?
6. Muestras disponibles y coste.
7. Política de producto defectuoso y de devoluciones.
8. Integración con Shopify o envío de catálogo/stock por CSV/API.

Muchas gracias,
[Nombre] · FAROLA · [teléfono] · [email]
```

---

## 4. Qué negociar (por orden de importancia)

1. **Calidad de muestra = calidad de producción.** Pide que guarden una "golden sample" firmada; cualquier desviación → reposición.
2. **Tasa de defectos y reposición**: objetivo ≤ 2 % y reposición gratuita en el siguiente envío (o crédito).
3. **Coste de muestra reembolsable** en el primer pedido.
4. **MOQ por color**: pide 100-200 por color en el primer pedido (en silicona suelen tener stock de colores estándar).
5. **Logo sin coste de molde** en el primer pedido (debossed/impreso) o molde amortizado en 2-3 pedidos.
6. **Precio escalado cerrado** para 200/500/1.000/3.000 uds durante 6 meses.
7. **Plazo de producción por escrito** (penalización o descuento si se retrasa).
8. **Documentación UE** (GPSR: nombre y dirección del fabricante en el producto o embalaje; REACH; contacto alimentario en la botella-bebedero).
9. **Packaging**: que el fabricante meta el inserto de marca y la caja (ahorra manipulación en 3PL).
10. **Pago**: 30 % anticipo / 70 % antes del envío, vía Alibaba Trade Assurance cuando se use Alibaba.

➡️ Siguiente: [04 · Marca y logo](04-marca-logo.md)

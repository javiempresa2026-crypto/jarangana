"""4 productos nuevos (23-09-2026). Datos del proveedor sacados de AutoDS (AliExpress, región US: revisar precio/envío a España)."""
import json
FREG, DUCHA = "gid://shopify/Collection/715459920217", "gid://shopify/Collection/715459887449"
INSTALA = "<p><em>Si llega roto o con un defecto, mándanos una foto y te enviamos otro o te devolvemos el dinero. Tienes 14 días para devolverlo.</em></p><p><strong>Envío:</strong> plazo estimado 7-15 días laborables, con seguimiento.</p>"

def img(urls, alt): return [{"originalSource": u, "contentType": "IMAGE", "alt": alt} for u in urls]
def var(opt, name, price, sku): return {"optionValues": [{"optionName": opt, "name": name}], "price": price, "sku": sku,
                                        "inventoryItem": {"tracked": False, "requiresShipping": True}}
P = []
P.append({"title": "Grifo Jarandana 1080° — Cabezal giratorio con 2 chorros", "handle": "grifo-giratorio-1080",
 "productType": "Cocina", "vendor": "jarandana", "status": "ACTIVE", "collections": [FREG],
 "tags": ["cocina", "baño", "sin-taladrar", "novedad", "proveedor:aliexpress-3256806984740623"],
 "seo": {"title": "Grifo giratorio 1080° con 2 chorros para cocina y baño | jarandana",
         "description": "Cabezal que se enrosca en tu grifo y gira 1080°. Dos modos: chorro suave o spray a presión. Sin obras ni herramientas. Rosca de 22/24 mm."},
 "descriptionHtml": "<p><strong>Tu grifo de siempre, con superpoderes.</strong></p><p>Se enrosca en lugar del aireador de tu grifo y lo convierte en un brazo articulado que <strong>gira 1080°</strong>: apunta el agua donde la necesitas para aclarar la sartén, lavarte la cara o limpiar el fregadero, sin salpicar.</p><h3>Por qué te va a gustar</h3><ul><li><strong>2 modos</strong>: chorro suave aireado o spray a presión, con un giro.</li><li><strong>Gira en todas direcciones</strong>: llega a todas las esquinas del fregadero.</li><li><strong>Se instala en 1 minuto</strong>: desenroscas el aireador y enroscas este. Sin herramientas ni obras.</li><li>Incluye un pequeño filtro de malla en la entrada.</li></ul><h3>Compatibilidad (importante)</h3><p>Rosca de <strong>22 mm (interior) / 24 mm (exterior)</strong>, la más común en grifos de cocina y lavabo. <strong>Mide tu grifo antes de comprar</strong>: no sirve para grifos extraíbles, de ducha o sin rosca en la boca.</p><h3>Datos</h3><ul><li>Material: plástico ABS, color negro.</li><li>Contenido: 1 cabezal giratorio.</li></ul>" + INSTALA,
 "productOptions": [{"name": "Pack", "values": [{"name": "1 unidad"}, {"name": "2 unidades"}]}],
 "variants": [var("Pack", "1 unidad", "12.90", "JAR-GRIFO-1"), var("Pack", "2 unidades", "19.90", "JAR-GRIFO-2")],
 "files": img(["https://ae01.alicdn.com/kf/S9303ab64042046108efe403b615b2fc4C.jpg", "https://ae01.alicdn.com/kf/Sf473b5a5642d4bda9b379f7115e7e67bn.jpg",
   "https://ae01.alicdn.com/kf/Sae5dc4530c8b4ef1a062d113f99ca05fV.jpg", "https://ae01.alicdn.com/kf/S96bc377c1b29432c806ddf5c53bd69c9o.jpg",
   "https://ae01.alicdn.com/kf/Sd04911e70a874df6aaf981a4630da79eu.jpg", "https://ae01.alicdn.com/kf/Sd6fbb94f4c4845d09812abf1c262ea8bO.jpg"], "Grifo giratorio 1080° jarandana")})

P.append({"title": "Luz LED Jarandana con sensor de movimiento — Recargable y magnética", "handle": "luz-led-sensor-movimiento",
 "productType": "Cocina", "vendor": "jarandana", "status": "ACTIVE", "collections": [FREG],
 "tags": ["cocina", "armario", "sin-taladrar", "novedad", "proveedor:aliexpress-1005009195805856"],
 "seo": {"title": "Luz LED con sensor de movimiento recargable sin cables | jarandana",
         "description": "Barra LED de 25 cm que se enciende sola al pasar. Recargable por USB-C, magnética y sin taladrar. 3 tonos de luz y 5 intensidades. Para cocina y armarios."},
 "descriptionHtml": "<p><strong>Abres el armario y se hace la luz. Sin cables, sin electricista.</strong></p><p>Barra LED de 25 cm con <strong>sensor de movimiento</strong>: en modo automático se enciende sola cuando pasas por delante a oscuras y se apaga a los 20 segundos. Perfecta bajo los muebles de cocina, dentro del armario, en el pasillo o junto a la cama.</p><h3>Por qué te va a gustar</h3><ul><li><strong>Sin taladrar</strong>: se pega una chapa adhesiva y la luz se queda imantada. La quitas para cargarla en un segundo.</li><li><strong>Recargable por USB-C</strong> (batería de 1800 mAh con indicador de carga). Cable incluido.</li><li><strong>3 tonos de luz</strong> (cálida 3000K, neutra 4500K, fría 6000K) y <strong>5 intensidades</strong>.</li><li>Modo automático con sensor o encendido fijo.</li></ul><h3>Datos del fabricante</h3><ul><li>Medidas: 25 × 3,3 × 1,9 cm.</li><li>Autonomía: unas 40 h al 10 % y 5 h al 100 %.</li><li>Incluye: luz, chapa magnética adhesiva, cable USB-C y manual.</li></ul><p><em>El sensor solo funciona a oscuras. No pongas dos luces muy juntas: pueden interferir entre sí.</em></p>" + INSTALA,
 "productOptions": [{"name": "Pack", "values": [{"name": "1 luz"}, {"name": "2 luces"}]}],
 "variants": [var("Pack", "1 luz", "24.90", "JAR-LUZ-1"), var("Pack", "2 luces", "44.90", "JAR-LUZ-2")],
 "files": img(["https://ae01.alicdn.com/kf/S5e9550e8a1004a6dbad17799cdb621cc3.jpg", "https://ae01.alicdn.com/kf/S286f945f5da1473d9a904fa38b783b09E.jpg",
   "https://ae01.alicdn.com/kf/Se4dd1f13b25d4a8faa26f21e04daa1968.jpg", "https://ae01.alicdn.com/kf/S2d68f730f78e403691d2e839fb5355a3b.jpg",
   "https://ae01.alicdn.com/kf/Sdb432612749b4cd6bf9442f66fb39f13t.jpg", "https://ae01.alicdn.com/kf/S7738a26a232e4a4ea7c56b0fd7485946Q.jpg"], "Luz LED con sensor de movimiento jarandana")})

P.append({"title": "Alcachofa de ducha Jarandana — 5 chorros con filtro", "handle": "alcachofa-ducha-5-chorros",
 "productType": "Baño", "vendor": "jarandana", "status": "ACTIVE", "collections": [DUCHA],
 "tags": ["ducha", "baño", "novedad", "proveedor:aliexpress-1005009452514317"],
 "seo": {"title": "Alcachofa de ducha de 5 chorros con filtro | jarandana",
         "description": "Cambia tu ducha en 2 minutos: alcachofa de mano con 5 tipos de chorro y cartucho de filtro. Se enrosca a tu flexo, sin obras. En plata o negro."},
 "descriptionHtml": "<p><strong>La ducha de hotel, en tu baño de alquiler.</strong></p><p>Alcachofa de mano con <strong>5 tipos de chorro</strong>: lluvia, masaje, spray… cambias de uno a otro con un botón. Se enrosca a tu flexo en dos minutos, sin herramientas ni obras, y cuando te mudas te la llevas.</p><h3>Por qué te va a gustar</h3><ul><li><strong>5 modos de chorro</strong> con un solo botón.</li><li><strong>Cartucho de filtro</strong> en el mango para retener impurezas del agua (según el fabricante). Recambiable.</li><li>Diseño de ahorro de agua, según el fabricante.</li><li>Se instala a mano: desenroscas la vieja y enroscas esta.</li></ul><h3>Compatibilidad</h3><p>Conexión estándar para flexos de ducha. Revisa que tu flexo tenga rosca estándar de 1/2\" (la habitual en España). Incluye solo la alcachofa (sin flexo ni soporte).</p><p><em>No es un descalcificador: para las marcas de cal en la mampara usa nuestra <a href=\"/products/rasqueta-mampara-silicona\">Rasqueta</a>.</em></p>" + INSTALA,
 "productOptions": [{"name": "Color", "values": [{"name": "Plata"}, {"name": "Negro"}]}],
 "variants": [var("Color", "Plata", "19.90", "JAR-ALCA-PLATA"), var("Color", "Negro", "19.90", "JAR-ALCA-NEGRO")],
 "files": img(["https://ae01.alicdn.com/kf/Sf8416213b76542b1acf2a492011c2cd2a.jpg", "https://ae01.alicdn.com/kf/S2f2d69a4b0e64b97b9e3ed392f981f83t.jpg",
   "https://ae01.alicdn.com/kf/S72e4bfd078de4da9adf06403eef1d06ca.jpg", "https://ae01.alicdn.com/kf/S85cd677b4c5d4b5dbdc0760d73b8f55fE.jpg",
   "https://ae01.alicdn.com/kf/Sf967a1010db642edb8c9c36412fd4c6eE.jpg", "https://ae01.alicdn.com/kf/S4f1031bd6311473081d9c390ac3cf7b6n.jpg"], "Alcachofa de ducha de 5 chorros jarandana")})

P.append({"title": "Dispensador de pasta de dientes Jarandana — Con portacepillos, sin taladrar", "handle": "dispensador-pasta-dientes",
 "productType": "Baño", "vendor": "jarandana", "status": "ACTIVE", "collections": [DUCHA],
 "tags": ["baño", "lavabo", "sin-taladrar", "novedad", "proveedor:aliexpress-1005008311587065"],
 "seo": {"title": "Dispensador de pasta de dientes con portacepillos sin taladrar | jarandana",
         "description": "Apoya el cepillo, empuja y sale la pasta justa. Dispensador de pared con portacepillos que se pega al azulejo, sin taladro. Lavabo recogido y sin tubos aplastados."},
 "descriptionHtml": "<p><strong>Empujas el cepillo y sale la pasta justa. Así de fácil.</strong></p><p>Dispensador de pasta de dientes de pared con <strong>portacepillos integrado</strong>. Colocas el tubo boca abajo, apoyas el cepillo, empujas y sale la cantidad justa. Adiós al tubo aplastado y a la encimera pringada.</p><h3>Por qué te va a gustar</h3><ul><li><strong>Sin taladrar</strong>: se pega al azulejo con adhesivo.</li><li><strong>Portacepillos</strong> para que los cepillos no toquen la encimera.</li><li>Funciona sin pilas: es mecánico.</li><li>Lavabo recogido en un minuto.</li></ul><h3>Cómo se instala</h3><ol><li>Limpia el azulejo con alcohol y sécalo.</li><li>Pega el soporte y presiona 30 segundos.</li><li><strong>Espera 24 h</strong> antes de colgar peso.</li></ol><p><em>Solo superficies lisas: azulejo, cristal o metal.</em></p>" + INSTALA,
 "productOptions": [{"name": "Color", "values": [{"name": "Negro"}, {"name": "Gris"}]}],
 "variants": [var("Color", "Negro", "14.90", "JAR-DISP-NEGRO"), var("Color", "Gris", "14.90", "JAR-DISP-GRIS")],
 "files": img(["https://ae01.alicdn.com/kf/S209e77d659f04317b48adc75b404f840f.jpg", "https://ae01.alicdn.com/kf/S7b6bf35d3c6c43c4a0cead3487f36d417.jpg",
   "https://ae01.alicdn.com/kf/S591bbd45da8a47908ced1a3ca3aae32ch.jpg", "https://ae01.alicdn.com/kf/Sf2d614577a754708a48948ce4001229cq.jpg",
   "https://ae01.alicdn.com/kf/Sccf2801551f84a49bde4a72fec62ce84R.jpg", "https://ae01.alicdn.com/kf/Sc295aea279594370a49b44e003015476w.jpg"], "Dispensador de pasta de dientes jarandana")})

if __name__ == "__main__":
    import sys
    i = int(sys.argv[1])
    print(json.dumps({"input": P[i]}, ensure_ascii=True))

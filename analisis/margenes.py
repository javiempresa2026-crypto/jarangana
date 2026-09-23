"""Margen neto por pedido de 1 unidad (dropshipping desde AliExpress, cliente en España).
Supuestos (cámbialos aquí):
- IVA 21 % incluido en el PVP (IOSS: se ingresa el IVA de la venta).
- Envío cobrado al cliente: 3,95 € si el pedido < 35 €, gratis desde 35 €.
- Comisión de pago Shopify Payments: 2,1 % + 0,30 € sobre el total cobrado. CONFIRMAR con tu plan.
- Tipo de cambio 0,92 €/$ (CONFIRMAR el día que compres).
- 0,50 € por pedido de imprevistos (devoluciones, reenvíos, diferencia de cambio).
- No incluye publicidad: el 30 % es lo que queda para pagar anuncios y beneficio.
"""
EUR_USD = 0.92
FEE_PCT, FEE_FIX, BUFFER = 0.021, 0.30, 0.50
FREE_FROM, SHIP = 35.0, 3.95

def margen(pvp, coste_usd, envio_usd):
    envio = 0 if pvp >= FREE_FROM else SHIP
    cobrado = pvp + envio
    neto = cobrado / 1.21
    comision = cobrado * FEE_PCT + FEE_FIX
    coste = (coste_usd + envio_usd) * EUR_USD + BUFFER
    beneficio = neto - comision - coste
    return beneficio, beneficio / neto

def precio_para(objetivo, coste_usd, envio_usd):
    p = 1.0
    while margen(p, coste_usd, envio_usd)[1] < objetivo: p += 0.05
    # redondeo comercial a ,90
    import math
    return math.ceil(p - 0.9) + 0.9

if __name__ == "__main__":
    actuales = [  # nombre, PVP actual, coste $, envío proveedor $
        ("Balda", 24.90, 11.12, 0), ("Rasqueta", 12.90, 8.61, 1.99), ("Ganchos x2", 9.90, 4.99, 1.99),
        ("Ganchos x4", 16.90, 8.28, 1.99), ("Kit Fregadero", 19.90, 6.19, 1.99), ("Esquinera Doble", 39.90, 20.42, 0),
        ("Bayetas x8", 12.90, 7.05, 1.99), ("Recambio adhesivos", 7.90, 5.00, 2.00), ("Kit Ducha", 44.90, 11.12 + 8.61 + 4.99, 1.99 * 2)]
    print(f"{'Producto':22} {'PVP':>7} {'Benef.':>7} {'Margen':>7}  PVP para 30 %")
    for n, p, c, e in actuales:
        b, m = margen(p, c, e)
        print(f"{n:22} {p:7.2f} {b:7.2f} {m:7.0%}  {precio_para(0.30, c, e):.2f}")

def resumen_ventas(ventas):
    if not isinstance(ventas, list):
        raise TypeError("El parámetro 'ventas' debe ser una lista")

    total_ventas = sum(v["total"] for v in ventas)
    promedio = total_ventas / len(ventas) if ventas else 0
    max_venta = max(ventas, key=lambda v: v["total"], default={"total": 0})

    return {
        "total_ventas": round(total_ventas, 2),
        "promedio_venta": round(promedio, 2),
        "venta_mayor": max_venta
    }


ventas = [
    {"id": 1, "total": 120.5},
    {"id": 2, "total": 80.2},
    {"id": 3, "total": 200.0},
]

print(resumen_ventas(ventas))

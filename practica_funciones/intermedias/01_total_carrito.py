def calcular_total_carrito(productos, descuento=0, envio=0):
    if not isinstance(productos, list):
        raise TypeError("El carrito debe ser una lista de prodcutos")

    total = 0
    for p in productos:
        if not isinstance(p, dict):
            raise TypeError("Cada producto debe ser un diccionario")
        if "precio" not in p or "cantidad" not in p:
            raise ValueError("Cada producto debe tener 'precio' y 'cantidad'")

        total += p["precio"] * p["cantidad"]

    # Aplicar descuento (en %)
    total -= total * (descuento / 100)

    # Agregar costo de envio
    total += envio
    return round(total, 2)


carrito = [
    {"nombre": "Camisa", "precio": 20.5, "cantidad": 2},
    {"nombre": "Pantalón", "precio": 35, "cantidad": 1}
]


print(calcular_total_carrito(carrito, descuento=10, envio=5))

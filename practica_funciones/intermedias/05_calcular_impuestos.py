def calcular_impuesto(producto):
    if not isinstance(producto, dict):
        raise TypeError("El producto debe ser un diccionario")

    tipo = producto.get("tipo")
    precio = producto.get("precio", 0)

    if tipo == "ropa":
        impuesto = 0.08
    elif tipo == "tecnologia":
        impuesto = 0.15
    else:
        impuesto = 0.05

    return round(precio * (1 + impuesto), 2)


print(calcular_impuesto({"tipo": "ropa", "precio": 100}))        # 108.0
print(calcular_impuesto({"tipo": "tecnologia", "precio": 100}))  # 115.0

"""Calcular el precio total de un pedido"""


def calcular_total(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["cantidad"]
    return total


# Ejemplo de uso
productos = [
    {"nombre": "Camisa", "precio": 20, "cantidad": 2},
    {"nombre": "Pantalón", "precio": 35, "cantidad": 1}
]

print(calcular_total(productos))  # 75

# Aplicar descuento al total


def aplicar_descuento(total, porcentaje):
    return total - (total * porcentaje / 100)


print(aplicar_descuento(20000, 10))  # 90.0

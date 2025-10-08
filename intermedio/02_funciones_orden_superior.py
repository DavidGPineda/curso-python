"""Funciones de orden superior"""
# Recibir otra función como argumento, o

# Devolver una función como resultado.

# Ejemplo 1 — Recibir otra función

from functools import reduce


def saludar(nombre):
    return f"Hola", {nombre}


def procesar(funcion, valor):
    return funcion(valor)


print(procesar(saludar, "Elliot"))

# Ejemplo 2 Devolver una función


def crear_miltiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar


por_dos = crear_miltiplicador(2)
print(por_dos(5))

products = [
    {"nombre": "Camisa", "precio": 25},
    {"nombre": "Pantalon", "precio": 40},
    {"nombre": "Zapatos", "precio": 60},
]

# map
con_iva = list(map(lambda p: {**p, "precio": p["precio"] * 1.21}, products))

print(con_iva)
# Todos los productos ahora incluyen el IVA.

# Filter
caros = list(filter(lambda p: p["precio"] > 30, products))
print(caros)

# sorted
ordenados = sorted(products, key=lambda p: p["precio"])
print(ordenados)

# reduce de functools sumar precios totales

total = reduce(lambda acc, p: acc + p["precio"], products, 0)
print("Total:", total)

# otra explicacion de reduce
latters = ["H", "E", "L", "L", "O"]

total = reduce(lambda x, y: x + y, latters)
print(total)

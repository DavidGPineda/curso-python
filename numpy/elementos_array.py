import numpy as np


matriz = np.arange(1, 13).reshape(3, 4)
print(matriz)

# ✅ Acceder a elementos en un array 2D
# print("Elemento fila 0, columna: 2:", matriz[0, 2])
# print("Elemento fila 2, columna 3:", matriz[2, 3])

# ✅ Acceder a filas completas
# print("Primera fila:", matriz[0])
# print("Segunda fila:", matriz[1])
# print("Tercera fila:", matriz[2])

# ✅ Acceder a columnas completas
# print("Primera columna:", matriz[:, 0])
# print("Segunda columna:", matriz[:, 1])
# print("Última columna:", matriz[:, -1])

# ✅ Slicing (cortar partes de una matriz)
# print("Submatriz 2x2:")
# print(matriz[0:2, 1:3])

# 🧠 Mini Reto 5
matriz = np.arange(1, 13).reshape(3, 4)

print("matriz")
print(matriz)

print("Valor 10:")
print(matriz[2, 1])

print("Segunda columna:")
print(matriz[:, 1])

print("submatriz:")
print(matriz[1:3, 1:3])

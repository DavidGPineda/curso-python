import numpy as np

matriz = np.arange(1, 13).reshape(3, 4)
print(matriz)

# ✅ Suma, máximo, mínimo, promedio
print("Suma total:", matriz.sum())
print("Valor máximo:", matriz.max())
print("Valor mínimo:", matriz.min())
print("Promedio:", matriz.mean())

# ✅ Operaciones por filas o columnas
# axis=0	Operar por columna
# axis=1	Operar por fila
# print("Suma por columnas:", matriz.sum(axis=0))
# print("Suma por filas:", matriz.sum(axis=1))


# ✅ Otras operaciones útiles
print("Minimo de cada columna:", matriz.min(axis=0))
print("Maximo de cada fila:", matriz.max(axis=1))
print("Promedio por columnas:", matriz.mean(axis=0))
print("Desviacion estandar:", matriz.std())

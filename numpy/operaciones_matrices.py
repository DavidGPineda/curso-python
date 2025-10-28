# import numpy as np

# matriz = np.arange(1, 13).reshape(3, 4)
# print(matriz)

# ✅ Suma, máximo, mínimo, promedio
# print("Suma total:", matriz.sum())
# print("Valor máximo:", matriz.max())
# print("Valor mínimo:", matriz.min())
# print("Promedio:", matriz.mean())
# print("Varianza:", matriz.var())
# print("Percentil 50:", np.percentile(matriz, 50))


# ✅ Operaciones por filas o columnas
# axis=0	Operar por columna
# axis=1	Operar por fila
# print("Suma por columnas:", matriz.sum(axis=0))
# print("Suma por filas:", matriz.sum(axis=1))


# ✅ Otras operaciones útiles
# print("Minimo de cada columna:", matriz.min(axis=0))
# print("Maximo de cada fila:", matriz.max(axis=1))
# print("Promedio por columnas:", matriz.mean(axis=0))
# print("Desviacion estandar:", matriz.std())

# 🧠 Mini Reto 6
# matriz = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90],
# ])

# print("Suma por filas:", matriz.sum(axis=1))
# print("Suma por columnas:", matriz.sum(axis=0))
# print("Valor maximo:", matriz.max())
# print("Promedio total:", matriz.mean())
# print("Promedio total:", matriz.std())

# ✅ Suma y resta entre matrices
# Las matrices deben tener la misma forma (shape) para poder sumarse o restarse.

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print("Suma:\n", a + b)
# print("Resta:\n", a - b)
# Se multiplica posición por posición:
# print("Multiplicacion elemento a elemento:\n", a * b)
# ✅ Multiplicación matricial (Producto punto)
# Esta es la multiplicación matemática real entre matrices:
# print("Multiplicacion matricial:\n", a.dot(b))
# Tambien funciona:
# print(np.dot(a, b))
# print(a @ b)
# ✅ Transponer una matriz
# Cambia filas por columnas:
# print("Transpuesta:\n", a.T)

# # 🧠 Mini Reto 7
# x = np.array([[2, 4],
#               [6, 8]])

# y = np.array([[1, 3],
#               [5, 7]])

# print("Suma:\n", x + y)
# print("Resta:\n", x - y)
# print("Multiplicación elemento a elemento:\n", x * y)
# print("Multiplicación matricial:\n", x.dot(y))
# print("Transpuesta de x:\n", x.T)

# ✅ Comparaciones y Máscaras Booleanas
# Las máscaras booleanas te permiten filtrar valores dentro de arrays o matrices usando condiciones.

# nums = np.array([5, 10, 15, 20, 25])
# print(nums > 10)

# ✅ Filtrar valores con condiciones
# print(nums[nums > 10])
# print(nums[nums <= 15])

# ✅ Condiciones combinadas
# Usamos & (AND), | (OR):
# print(nums[(nums > 10) & (nums < 25)])  # Entre 10 y 25
# print(nums[(nums == 5) | (nums == 25)])  # Igual a 5 o 25

# ✅ Aplicado a matrices
# matriz = np.arange(1, 10).reshape(3, 3)

# print(matriz)
# print(matriz > 5)  # Mascara booleana
# print(matriz[matriz > 5])  # Valores filtrados

# 🧠 Mini Reto 8
# matriz = np.array([
#     [12, 7, 5],
#     [3, 18, 10],
#     [21, 4, 9]
# ])

# print(matriz[matriz > 10])
# print(matriz[(matriz % 2 == 0)])
# print(matriz[(matriz >= 5) & (matriz <= 20)])
# matriz[matriz <= 10] = 0
# print(matriz)

# nums = np.array([10, 15, 20, 25, 30])

# resultado = np.where(nums > 18)
# print(resultado)

# 🔧 Usarlo para reemplazar datos
# nums = np.where(nums < 15, 0, nums)
# print(nums)

# numeros = np.array([5, 12, 18, 25, 30])
# result = np.where((numeros > 10) & (numeros < 25))
# print(numeros[result])

# Mini Reto 10
# valores = np.array([3, 15, 8, 22, 7, 18, 2, 30])

# # 1. Posiciones de los números mayores que 10
# mayores = np.where(valores > 10)

# # 2. Valores menores o iguales a 10
# menores = np.where(valores <= 10)

# # 3. Reemplazar valores > 20 con 99
# remplazo_mayores = np.where(valores > 20, 99, valores)

# # 4. Reemplazar valores < 5 con 0
# remplazo_menores = np.where(valores < 5, 0, valores)

# print("Valores mayores que 10:", valores[mayores])
# print("Valores menores o iguales que 10:", valores[menores])
# print("Reemplazo de >20 por 99:", remplazo_mayores)
# print("Reemplazo de <5 por 0:", remplazo_menores)

# ------------------------
# np.unique
# ✅ ¿Qué hace np.unique?

# Sirve para:
# ✅ Encontrar valores únicos
# ✅ Eliminar duplicados
# ✅ Contar cuántas veces aparece cada valor
# ✅ Obtener el índice donde aparece cada valor

# nums = np.array([2, 4, 2, 8, 4, 10, 2])
# print(np.unique(nums))

# # 🔧 Contar repeticiones con return_counts
# valores, conteo = np.unique(nums, return_counts=True)
# print(valores)
# print(conteo)

# # 🔧 Mostrar posiciones con return_index
# valores, indices = np.unique(nums, return_index=True)
# print(valores)
# print(indices)

# # 🔧 Ordenar y contar palabras con unique
# nombres = np.array(["Ana", "Luis", "Ana", "Pedro", "Luis", "Maria"])
# print(np.unique(nombres, return_counts=True))

# datos = np.array([4, 6, 2, 6, 4, 8, 2, 2, 10, 6, 4])

# 1. Valores únicos
# valores_unicos = np.unique(datos)
# print("Datos unicos: ", valores_unicos)

# # 2. Contar repeticiones
# valores, conteo = np.unique(datos, return_counts=True)
# print("Valores:", valores)
# print("Conteo:", conteo)

# # 3. Posición del primer 6
# posicion_6 = np.where(datos == 6)[0][0]
# print("Posición del primer 6:", posicion_6)

# # 4. Número que más se repite
# mas_repite = valores[np.argmax(conteo)]
# print("Número que más se repite:", mas_repite)

# ✅ np.sort – Ordenar valores
# Ordena un array, pero no modifica el original.
# nums = np.array([10, 4, 7, 2, 9])
# print(np.sort(nums))
# # ✅ np.argsort – Obtener posiciones ordenadas
# # En lugar de ordenar los valores, devuelve los índices en el orden para ordenar el array.
# print(np.argsort(nums))
# # ✅ Ordenar una matriz completa
# matriz = np.array([
#     [3, 1, 2],
#     [9, 7, 8]
# ])
# print(np.sort(matriz))
# # ✅ Ordenar por filas o columnas con axis
# print("Ordenar por columnas:\n", np.sort(matriz, axis=0))
# print("Ordenar por filas:\n", np.sort(matriz, axis=1))

# 🧠 Mini Reto 12
# valores = np.array([12, 5, 8, 20, 15, 3, 25])

# # 1. Ordenar de menor a mayor
# print("Orden ascendente:", np.sort(valores))

# # 2. Ordenar de mayor a menor
# print("Orden descendente:", np.sort(valores)[::-1])

# # 3. Posiciones para ordenar el array
# print("Índices ordenados:", np.argsort(valores))

# # 4. Valor máximo usando ordenamiento
# print("Valor máximo:", np.sort(valores)[-1])

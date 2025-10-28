import numpy as np
# print(np.__version__)
# ➡️ Siguiente tema: Concatenación y particionado de arrays
# Concatenar

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.concatenate([a, b]))

# Concatenar matrices por filas o columnas

# m1 = np.array([[1, 2], [3, 4]])
# m2 = np.array([[5, 6], [7, 8]])

# print(np.vstack([m1, m2]))  # Vertical (filas)
# print(np.hstack([m1, m2]))  # Horizontal (columnas)

# Dividir arrays
# valores = np.array([10, 20, 30, 40, 50, 60])
# print(np.split(valores, 3))  # Lo divide en 3 partes iguales

# ✅ Mini Reto

# x = np.array([2, 4, 6])
# y = np.array([8, 10, 12])

# # 1. Unir dos arrays
# print(np.concatenate([x, y]))

# # 2. Unir matrices vertica y horizontal
# a = np.array([[1, 1], [1, 1]])
# b = np.array([[2, 2], [2, 2]])

# print(np.vstack([a, b]))
# print(np.hstack([a, b]))

# # 3. Divide este array en 4 partes iguales
# z = np.array([100, 200, 300, 400, 500, 600, 700, 800])
# print(np.split(z, 4))

# ✅ ¿Qué es Broadcasting?

# El broadcasting permite hacer operaciones entre arrays de diferente tamaño
# sin necesidad de usar bucles.
# NumPy "expande" automáticamente uno de los arrays para que coincida con el otro.

# ✔️ Operar array + número (esto ya lo viste)

# a = np.array([1, 2, 3])
# print(a + 5)
# ✅ NumPy suma 5 a cada elemento usando broadcasting.

# ✔️ Operación entre arrays de diferentes tamaños

# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# vector = np.array([10, 20, 30])
# print(matriz + vector)
# ✅ El vector se "repite" automáticamente por filas para poder sumarse.

# ❌ Caso que da error
# a = np.array([1, 2, 3])
# b = np.array([1, 2])
# print(a + b)  # ❌ Error: no tienen tamaños compatibles

# ✅ Reglas del Broadcasting (muy simple)
# Para poder operar arrays:
# Las dimensiones deben ser iguales, o
# Una de las dimensiones debe ser 1 (entonces se expande).
# (3,3)  +  (1,3) ✔️ válido
# (5,)   +  (1,) ✔️ válido
# (3,2)  +  (3,) ❌ NO válido

# 🧠 Mini Reto de Broadcasting

# m = np.array([[2, 4, 6],
#               [1, 3, 5],
#               [7, 9, 11]])
# v = np.array([10, 10, 10])

# # 1. Suma
# print(m + v)

# # 2. Multiplicacion
# v2 = np.array([1, 2, 3])
# print(m * v2)

# # 3. Resta
# print(m - 5)

# Funciones útiles de NumPy
# reshape avanzado
# repeat, tile
# clip
# sum con axis aplicado
# expand_dims, ravel

# ✅ reshape avanzado
# Reorganiza la forma de un array SIN cambiar sus valores.
# a = np.arange(12)
# print(a.reshape(3, 4))  # 3 filas, 4 columnas
# print(a.reshape(2, -1))  # -1 deja que NumPy calcule las columnas automaticamente

# ✅ ravel y flatten
# Convierte cualquier matriz en 1 sola dimensión.
# m = np.array([[1, 2], [3, 4]])
# print(m.ravel())  # No crea copia, mas eficiente
# print(m.flatten())  # Crea copia

# ✅ repeat y tile
# Repite valores de un array.
# a = np.array([1, 2, 3])
# print(np.repeat(a, 2))  # Repite cada elemento
# print(np.tile(a, 3))  # Repite todo el array

# ✅ clip
# Limita los valores mínimos y máximos.
# x = np.array([5, 10, 15, 20, 25])
# print(np.clip(x, 7, 24))

# ✅ expand_dims (muy útil)
# Añade una dimensión. Te sirve mucho antes de concatenar.
# a = np.array([1, 2, 3])
# print(np.expand_dims(a, axis=0))  # Fila
# print(np.expand_dims(a, axis=1))  # Columna

# 🧠 Mini Reto
# 1. Array del 1 al 8 como matriz de 2 filas
# a = np.arange(1, 9)
# matriz = a.reshape(2, -1)
# print("Paso 1:\n", matriz)

# # 2. Convertir matriz a vector 1D
# vector = matriz.ravel()
# print("\nPaso 2:\n", vector)

# # 3. Repetir 3 veces el vector
# repetido = np.tile(vector, 3)
# print("\nPaso 3:\n", repetido)

# # 4. Limitar valores entre 5 y 10
# limitado = np.clip(repetido, 5, 10)
# print("\nPaso 4:\n", limitado)

# # 5. Convertir a columna (2D)
# columna = limitado.reshape(-1, 1)
# print("\nPaso 5:\n", columna)

# 🎲 Números Aleatorios con np.random
# Esto se usa mucho en estadística, simulaciones, inteligencia artificial y pruebas de código.

# ✅ Generar números aleatorios simples
# print(np.random.rand(5))  # 5 Números entre 0 y 1 (decimales)
# print(np.random.randint(1, 10))  # Entero aleatorio entre 1 y 9
# print(np.random.randint(1, 10, 5))  # 5 Enteros aleatorios

# ✅ Matrices aleatorias
# print(np.random.rand(2, 3))         # Matriz 2x3 con decimales
# print(np.random.randint(1, 10, (2, 3)))  # Matriz 2x3 con enteros

# ✅ Distribución normal (muy usada)
# print(np.random.randn(5))  # 5 números con distribución normal (media 0)

# ✅ Mezclar y elegir aleatorios
# a = np.array([10, 20, 30, 40, 50])
# np.random.shuffle(a)  # Mezcla el array
# print(a)

# print(np.random.choice(a, 2))  # Elige 2 valores al azar

# # ✅ Hacer reproducibles los resultados (semilla)
# np.random.seed(0)
# print(np.random.rand(3))

# 🧠 Mini Reto Final 🔥
# Escribe código que:
# Genere 10 números enteros aleatorios entre 50 y 100.
# Cree una matriz 3x3 con números aleatorios entre 1 y 9.
# Mezcle los valores del primer arreglo.
# Elija 3 valores aleatorios sin repetirse de ese arreglo.
# Establece una semilla (np.random.seed(42)) para reproducibilidad.

# 5. una semilla (np.random.seed(42)) para reproducibilidad.
np.random.seed(42)

# 1. Aleatorios del 50 al 100
# numeros = np.random.randint(50, 100, 10)
# print("Aleatorios del 50 al 100:\n", numeros)

# # 2. matriz 3x3
# matriz = np.random.randint(1, 10, (3, 3))
# print("\nMatriz 3x3:\n", matriz)

# # 3. Mezcle los valores del primer arreglo.
# np.random.shuffle(numeros)
# print("\nMezcla del arreglo:\n", numeros)

# # 4. 3 valores aleatorios sin repetirse
# valores_aleatorios = np.random.choice(numeros, 3, replace=False)
# print("\n3 valores elegidos aleatoriamente:\n", valores_aleatorios)

# c = np.arange(24).reshape(2, 3, 4)  # 3d array
# print(c)

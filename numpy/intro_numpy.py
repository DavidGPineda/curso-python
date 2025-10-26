import numpy as np

# ✅ Paso 2: Crear arrays (lo más básico en NumPy)
a = np.array([10, 20, 30])
b = np.zeros(5)           # 5 ceros
c = np.ones(4)            # 4 unos
d = np.arange(1, 10, 2)   # Del 1 al 9 de 2 en 2
e = np.linspace(0, 1, 5)  # 5 números entre 0 y 1

# Mini Reto
reto = np.arange(100, 201, 10)

# print("Array a: ", a)
# print("Array b: ", b)
# print("Array c: ", c)
# print("Array d: ", d)
# print("Array e: ", e)
# print("Reto: ", reto)


# Operaciones básicas con arrays
# ✅ Operaciones matemáticas con arrays

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# print("Suma: ", a + b)
# print("Resta: ", a - b)
# print("Multiplicacion: ", a * b)
# print("División: ", a / b)
# print("Potencia: ", a ** 2)

# ✅ Mini Reto 2 😎

# Crea un array con los números 5, 10, 15, 20, 25 y:

# Súmale 5 a todos los elementos

# Multiplícalos por 3

# Eleva cada número al cuadrado

# a = np.array([5, 10, 15, 20, 25])
# suma = np.array([5, 5, 5, 5, 5])


# def agregar_cinco():
# numeros = np.array([5, 10, 15, 20, 25])
# nums = []
# for _ in range(5):
#     nums.append(5)  # Sin asignar a variable
# suma = np.array(nums)
# print("Suma: ", numeros + suma)

# numeros = np.array([5, 10, 15, 20, 25])
# suma = 5
# print("Suma: ", numeros + suma)

# numeros = np.array([5, 10, 15, 20, 25])
# suma = np.array([5] * 5)
# print("Suma: ", numeros + suma)

# tres = 3
# print("Multiplicación: ", numeros * tres)
# print("Cuadrado: ", numeros ** 2)

# print(agregar_cinco())

# numeros = np.array([5, 10, 15, 20, 25])
# print("Original:       ", numeros)
# print("Suma +5:        ", numeros + 5)      # Más elegante
# print("Multiplicación: ", numeros * 3)
# print("Cuadrado:       ", numeros ** 2)


# 🚀 Mini Reto 3

# Ahora crea una función llamada operaciones_basicas() que:

# Cree un array con valores del 1 al 6

# Lo multiplique por 10

# Le reste 4

# Lo divida entre 2

# def operaciones_basicas():
#     valores = np.array([1, 2, 3, 4, 5, 6])
#     print("Original: ", valores)
#     print("x10: ", valores * 10)
#     print("-4: ", valores - 4)
#     print("/2", valores / 2)


# operaciones_basicas()

# ✅ Crear arrays 2D en NumPy
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print("Matriz:")
# print(matriz)
# print("Forma:", matriz.shape)  # Filas y columnas
# print("Dimensiones:", matriz.ndim)

# print(np.zeros((2, 3)))      # Matriz 2x3 de ceros
# print(np.ones((3, 3)))       # Matriz 3x3 de unos
# print(np.eye(4))             # Matriz identidad 4x4


matriz = np.arange(1, 13).reshape(3, 4)
print("Matriz:")
print(matriz)

"""Lambdas"""
# lambda argumentos: expresión
# Las lambdas se usan mucho con funciones como map(), filter() y sorted()

# def cuadrado(x):
#     return x * x


# Con lambda
def cuadrado(x): return x * x


print(cuadrado(5))


def sumar(a, b): return a + b


print(sumar(3, 7))

# map
numeros = [1, 2, 3, 4, 5, 6]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)

# filter
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# sorted
personas = [("Ana", 26), ("Luis", 19), ("Carla", 30)]
ordenadas = sorted(personas, key=lambda persona: persona[1])
print(ordenadas)

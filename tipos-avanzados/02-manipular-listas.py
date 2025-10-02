pets = ["bear", "lion", "wolf", "colibri"]
print(pets[2])

pets[3] = "pangolin"
print(pets)
print(pets[2:])
print(pets[-1])  # el ultimo
print(pets[::2])  # solo pares, empieza desde 0
print(pets[1::2])  # solo pares, empieza desde 1

numeros = list(range(21))

print(numeros[0::2])  # pares
print(numeros[1::2])  # impares

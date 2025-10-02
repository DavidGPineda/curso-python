pets = ["bear", "lion", "lion", "wolf", "pangolin"]

pets.insert(1, "gato")  # donde quieras
pets.append("paloma")  # al final

pets.remove("lion")  # solo elimina el primero
pets.pop()  # elimina el ultimo
pets.pop(3)  # elimina el que quieras, pones el indice
del pets[0]  # otra manera de eliminar
pets.clear()  # limpiar el arreglo completo

print(pets)

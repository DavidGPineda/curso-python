"""Dicionarios"""

my_dict = dict()

print(type(my_dict))

users = {"id": 1, "name": "bear", "age": 50}

print(users)
print(users["id"])
print(users["name"])
print(users["age"])

users["age"] = 20
print(users)

if "surname" in users:
    print("Encontre el surname: ", users["surname"])

print(users.get("id"))
print(users.get("x", 28))
del users["age"]
print(users)

for valor in users:
    print(valor, users[valor])

# devuleve tuplas
for valor in users.items():
    print(valor)

# desempaquetar tupla
for clave, valor in users.items():
    print(clave, ":", valor)

usuarios = [
    {"id": 1, "name": "bear"},
    {"id": 2, "name": "lion"},
    {"id": 3, "name": "wolf"},
    {"id": 4, "name": "pangolin"},
]

print("Tipo de dato: ", type(usuarios))

for user in usuarios:
    print(user["name"])

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

print(persona.keys())
print(persona.values())

persona.update({"edad": 26, "profesion": "Ingenieria"})
print(persona)

ciudad = persona.pop("ciudad")
print(ciudad)
print(persona)

# Crea un nuevo diccionario con claves de una lista y un mismo valor.
claves = ["name", "age", "city"]
nuevo = dict.fromkeys(claves, "hola")
print(nuevo)

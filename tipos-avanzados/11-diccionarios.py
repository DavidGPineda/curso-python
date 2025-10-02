users = {"id": 1, "y": 50, "name": "bear"}

print(users)
print(users["id"])
print(users["y"])
print(users["name"])

users["y"] = 2
print(users)

if "surname" in users:
    print("Encontre el surname: ", users["surname"])

print(users.get("id"))
print(users.get("x", 28))
del users["y"]
print(users)

for valor in users:
    print(valor, users[valor])

# devuleve tuplas
for valor in users.items():
    print(valor)

# desempaquetar tupla
for llave, valor in users.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "name": "bear"},
    {"id": 2, "name": "lion"},
    {"id": 3, "name": "wolf"},
    {"id": 4, "name": "pangolin"},
]

for user in usuarios:
    print(user["name"])

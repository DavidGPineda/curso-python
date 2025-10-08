users = [["bear", 4], ["lion", 6], ["pango", 2]]

# FOR clásico
# names = []
# for user in users:
#     names.append(user[0])
# print(names)

# LIST COMPREHENSION
# names = [user[0] for user in users]
# print(names)

# FILTER (sin transformar, devuelve la sublista completa)
# names = [user for user in users if user[1] > 2]
# print(names)

# FILTER + TRANSFORM (solo el nombre)
# names = [user[0] for user in users if user[1] > 2]
# print(names)

# MAP (transformación usando lambda)
# names = list(map(lambda user: user[0], users))
# print(names)

menosUser = list(filter(lambda user: user[1] > 2, users))
print(menosUser)

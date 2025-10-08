numbers = [2, 85, 96, 12, 34, 75, 96, 5]

numbers.sort()  # ordenar
numbers.sort(reverse=True)  # ordenar al reves
# sorted va a devolver una (nueva lista)
numbers2 = sorted(numbers, reverse=True)

print(numbers)
print(numbers2)

# users = [[4, "bear"], [6, "lion"], [2, "pango"]]
users = [["bear", 4], ["lion", 6], ["pango", 2]]
# si el id esta el inicio, se ordena
# si no esta al inicio, no se ordena


# def ordenar(elemento):
#     return elemento[1]


# users.sort(key=ordenar)
# print(users)

users.sort(key=lambda el: el[1])
print(users)

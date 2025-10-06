""" Tuplas """
# tuplas son listas pero no se pueden modificar
my_tuple = tuple()
my_other_tuple = ()

print("Tipo de dato: ", type(my_tuple))

numbers = (1, 2, 3) + (4, 5, 6) + ("bear", "elliot")

print(numbers[1])
print(numbers)

# punto = tuple([1, 2])
# punto = tuple("bear")

menosNumeros = numbers[:2]

one, two, * otros, names = numbers
print(one, two, otros, names)

# for num in numbers:
#     print(num)

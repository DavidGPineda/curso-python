# tuplas son listas pero no se pueden modificar
numbers = (1, 2, 3) + (4, 5, 6)

print(numbers)

punto = tuple([1, 2])
# punto = tuple("bear")

menosNumeros = numbers[:2]

one, two, * otros = numbers
print(one, two, otros)

for num in numbers:
    print(num)

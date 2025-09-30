def suma(*numbers):
    resultado = 0
    for num in numbers:
        resultado += num
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 59, 41)

saludo = "hola global"
# utilizar variables globales es mala practica


def saludar():
    saludo = "Hola"
    print(saludo)


def saludarBear():
    saludo = "hola bear"
    print(saludo)


saludar()
saludarBear()
print(saludo)

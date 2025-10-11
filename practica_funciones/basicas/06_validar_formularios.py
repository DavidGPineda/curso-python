def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return isinstance(stock, int) and stock >= 0


print(validar_precio(10.5))  # True
print(validar_stock(-1))  # False

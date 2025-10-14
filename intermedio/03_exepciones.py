
# # try / except
# try:
#     numero = int(input("Escribe un número: "))
#     # Si escribes hola -- error
#     print("El número es: ", numero)
# except ValueError:
#     print(" Debes escribir un número valido")

# # Capturar varios tipos de errores

# try:
#     a = int(input("Número A: "))
#     b = int(input("Número B: "))
#     print("Resultado: ", a / b)
# except ValueError:
#     print("Debes ingresar solo números.")
# except ZeroDivisionError:
#     print("No puedes dividir por cero.")

# # Capturar cualquier error (no recomendado siempre)
# try:
#     x = 1 / 0
# except Exception as e:
#     print("Ocurrio un error:", e)

# # Finally y else
# # Finally -- Se ejecuta siempre, haya o no error (ideal para liberar recursos, cerrar archivos, etc)
# # else -- se ejecuta solo si no hubo error

# try:
#     num = int(input("Número: "))
# except ValueError:
#     print("Error: entrada invalida.")
# else:
#     print("Todo bien. Número válido:", num)
# finally:
#     print("Programa terminado.")

# # Crear tus propias exceptiones
# # definir errores personalozados usando clases


class ErrorSaldoInsuficiente(Exception):
    pass


def retirar_dinero(saldo, cantidad):
    if cantidad > saldo:
        raise ErrorSaldoInsuficiente("Saldo insuficiente para la operacion.")
    return saldo - cantidad

# 💡 raise sirve para lanzar una excepción manualmente.


try:
    nuevo_saldo = retirar_dinero(100, 110)
    print("Nuevo saldo:", nuevo_saldo)
except ErrorSaldoInsuficiente as e:
    print("❌", e)

import logging

# Crear un logger principal
logger = logging.getLogger("cajero_logger")
logger.setLevel(logging.DEBUG)
# Captura todos los niveles: DEBUG, INFO, WARNING, ERROR, CRITICAL

# === Handler 1: salida en consola ===
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# === Handler 2: salida a archivo ===
file_handler = logging.FileHandler("errores.log", mode="a")
file_handler.setLevel(logging.ERROR)

# Formato de los mensajes
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# === Agregar handlers al logger ===
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class ErrorSaldoInsuficiente(Exception):
    """Error lanzado cuando el saldo no alcanza para el retiro"""


class CuentaBancaria:
    """Cuenta bancaria"""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        logger.info(
            "Cuenta creada para %s con saldo $%.2f", titular, saldo_inicial)

    def mostrar_saldo(self):
        """Mostrar saldo"""
        print(f"Saldo actual de {self.titular}: ${self.saldo:.2f}")

    def depositar(self, cantidad):
        """Depositar dinero"""
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar deber ser positiva")
        self.saldo += cantidad
        logger.info(
            "Deposito de $%.2f en cuenta de %s. Nuevo saldo: $%.2f",
            cantidad,
            self.titular,
            self.saldo
        )

    def retirar(self, cantidad):
        """Retirar dinero"""
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        if cantidad > self.saldo:
            raise ErrorSaldoInsuficiente("Saldo insuficiente")
        self.saldo -= cantidad
        logger.info(
            "Retiro de $%.2f de la cuenta %s. Nuevo saldo: $%.2f",
            cantidad,
            self.titular,
            self.saldo
        )


def cajero():
    """Cajero"""
    cuenta = CuentaBancaria("Bear", 1000)

    while True:
        print("\n=== Cajero Automatico ===")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Elije una opcion: ")

        try:
            if opcion == "1":
                cuenta.mostrar_saldo()
            elif opcion == "2":
                cantidad = float(input("Cantidad a depositar: "))
                cuenta.depositar(cantidad)
            elif opcion == "3":
                cantidad = float(input("Cantidad a retirar: "))
                cuenta.retirar(cantidad)
            elif opcion == "4":
                print("Gracias por usar el cajero.")
                break
            else:
                print("Opcion invalida")
        except ValueError as e:
            print("Error de valor:", e)
            # logging.error(f"Error de valor: {e}")
            logger.error("Error de valor: %s", e)
        except ErrorSaldoInsuficiente as e:
            print(e)
            logger.error("Saldo insuficiente: %s", e)
        except Exception as e:
            print("Ocurrio un erro inesperado:", e)
            logger.exception("Error inesperado:s")
        finally:
            print("Operacion completada. \n")


if __name__ == "__main__":
    cajero()

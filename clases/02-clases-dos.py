class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

# uso


p = Producto("Camisa", 50)
p.aplicar_descuento(10)
print(p.precio)


# ----------------------------------

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar(self, usuario):
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

# Así evitas usar muchas variables globales y mantienes la lógica encapsulada.
# ----------------------------------


class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} está encendido.")

# Perfecto para juegos, simulaciones o aplicaciones interactivas.

# ----------------------------------


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Admin(Usuario):
    def borrar_usuario(self):
        print("f{self.nombre} puede borrar usuarios")

# Ideal en sistemas con roles o permisos.


# Encapsulacion
# Permite protejer la información interna de la clase

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        # Doble guión bajo = atributo "privado"

    def depositar(self, monto):
        self.__saldo += monto

    def obtener_saldo(self):
        return self.__saldo

# Así evitas que alguien haga cuenta.__saldo = 999999


# Herencia

class Animal:
    def hablar(self):
        print("Hace un sonido")


class Perro(Animal):
    def hablar(self):
        print("Guau!")


# Composición (Una clase dentro de otra)

class Motor:
    def encender(self):
        print("Motor encendido")


class Auto:
    def __init__(self):
        self.motor = Motor()


mi_auto = Auto()
mi_auto.motor.encender()

# Esto se usa muchísimo en proyectos grandes (como Django, FastAPI, videojuegos, etc.).

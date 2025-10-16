"""Alquilar Vehiculos"""


class Vehiculo:
    """Clase base para vehiculos"""

    def __init__(self, marca, modelo, ano, precio_dia):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precio_dia = precio_dia
        self.disponible = True
        # Todos los vehiculos estan disponibles al inicio

    def alquilar(self):
        """Marcar vehiculo como alquilado"""

        if not self.disponible:
            print(f" {self.marca} {self.modelo} no esta disponible.")
        else:
            print(f"Has alquilado {self.marca} {self.modelo}")

    def devolver(self):
        """Marcar el vehiculo como disponible"""
        if self.disponible:
            print(f"{self.marca} {self.modelo} ya esta disponible")
        else:
            self.disponible = True
            print(f"{self.marca} {self.modelo} ha sido devuelto")

    def mostrar_info(self):
        """Mostrar informacion basica"""
        estado = "Disponible" if self.disponible else "Alquilado"
        print(
            f"{self.marca} {self.modelo} ({self.ano}) - ${self.precio_dia}/dia - {estado}")


class Coche(Vehiculo):
    """Clase para coches"""

    def __init__(self, marca, modelo, ano, precio_dia, puertas):
        super().__init__(marca, modelo, ano, precio_dia)
        self.puertas = puertas

    def mostrar_info(self):
        estado = "Disponoble" if self.disponible else "Alquilado"
        print(f"{self.marca} {self.modelo} ({self.ano}) - {self.puertas} puertas - ${self.precio_dia}/dia - {estado}")


class Moto(Vehiculo):
    """Clase para motos"""

    def __init__(self, marca, modelo, ano, precio_dia, cilindrada):
        super().__init__(marca, modelo, ano, precio_dia)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Alquilado"
        print(f"{self.marca} {self.modelo} ({self.ano}) - {self.cilindrada}cc - ${self.precio_dia}/dia - {estado}")


class Cliente:
    """Clase para clientes del sistema de alquiler"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo_alquilado = None

    def alquilar_vehiculo(self, vehiculo):
        if self.vehiculo_alquilado:
            print(f"{self.nombre} ya tiene un vehiculo alquilado")
        elif not vehiculo.disponible:
            print(
                f"El vehiculo {vehiculo.marca} {vehiculo.modelo} no esta disponible")
        else:
            vehiculo.alquilar()
            self.vehiculo_alquilado = vehiculo
            print(f"{self.nombre} ha alquilado {vehiculo.marca} {vehiculo.modelo}.")

    def devolver_vehiculo(self):
        if self.vehiculo_alquilado:
            self.vehiculo_alquilado.devolver()
            print(f"{self.nombre} ha devuelto su vehiculo")
            self.vehiculo_alquilado = None
        else:
            print(f"{self.nombre} no tiene vehiculo alquilado.")


class AgenciaAlquiler:
    """Gestiona los vehiculos disponibles y las operaciones de alquiler"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"{vehiculo.marca} {vehiculo.modelo} agregado al inventario")

    def mostrar_vehiculos(self):
        print(f"\n=== {self.nombre} - Vehiculos Disponilbes")
        for vehiculo in self.vehiculos:
            vehiculo.mostrar_info()


# Crear una agencia
agencia = AgenciaAlquiler("RentaAuto")

# Crear vehiculos
coche1 = Coche("Toyota", "Corolla", 2022, 50, 4)
coche2 = Coche("Ford", "Focus", 2021, 45, 4)
moto1 = Moto("Yamaha", "MT-07", 2023, 35, 700)

# Agregar vehiculos a la agencia
agencia.agregar_vehiculo(coche1)
agencia.agregar_vehiculo(coche2)
agencia.agregar_vehiculo(moto1)

# Mostrar inventario
agencia.mostrar_vehiculos()

# Crear un cliente
cliente = Cliente("Bear")

# Alquilar y devolver
cliente.alquilar_vehiculo(coche1)
cliente.alquilar_vehiculo(moto1)  # no puede por que ya tiene uno
cliente.devolver_vehiculo()

# Estado final
agencia.mostrar_vehiculos()

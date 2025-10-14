
# Crear la clase libro (titulo, autor, estado)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponoble" if self.disponible else "Prestado"
        print(f"{self.titulo} por {self.autor} - {estado}")


# Crear la clase Usuario (nombre, libros que ha prestado lista)


class Usuario:
    """Clase usuario"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def puede_prestar(self):
        """Este metodo sera redifinido en las clases hijas"""
        return True

    def mostrar_libros(self):
        """Mostrar libros"""
        if self.libros_prestados:
            print(f"{self.nombre} tiene estos libros prestados")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene libros prestados")


class Estudiante(Usuario):
    """Clase hija, hereda de usuario"""

    def __init__(self, nombre, grado):
        super().__init__(nombre)
        self.grado = grado

    def puede_prestar(self):
        return len(self.libros_prestados) < 2  # maximo 2 libros


class Profesor(Usuario):
    """Clase hija, hereda de usuario"""

    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    def puede_prestar(self):
        return len(self.libros_prestados) < 5  # maximo 5 libros


# Funciones (metodos) para prestar y devolver libros


class Biblioteca:
    """Classe bibliotecas"""

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """Agregar libros"""
        self.libros.append(libro)

    def prestar_libro(self, libro, usuario):
        """Prestar libros"""

        if not libro.disponible:
            print(f"El libro '{libro.titulo}' ya esta prestado")
            return

        if not usuario.puede_prestar():
            print(f"{usuario.nombre} no puede prestar mas libros")
            return

        libro.disponible = False
        usuario.libros_prestados.append(libro)
        print(f"{usuario.nombre} ha prestado '{libro.titulo}'")

        # print(f"El libro '{libro.titulo}' no está disponible")

    def devolver_libro(self, libro, usuario):
        """Devolver libros"""
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            print(f"{usuario.nombre} ha devuelto '{libro.titulo}'")
        else:
            print(f"{usuario.nombre} no tiene ese libro")


# Crear biblioteca

biblio = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Garcia Márquez")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("El principito", "Saint-Exupery")

# Agregar libros
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.agregar_libro(libro3)

# Crear usuarios
estu = Estudiante("Bear", "11")
prof = Profesor("Laura", "Matematicas")

# Prestamos
biblio.prestar_libro(libro1, estu)
biblio.prestar_libro(libro2, estu)
biblio.prestar_libro(libro3, estu)  # no deberia poder

biblio.prestar_libro(libro3, prof)  # si puede

# Mostrar estado
print("\nEstado final: ")
estu.mostrar_libros()
prof.mostrar_libros()

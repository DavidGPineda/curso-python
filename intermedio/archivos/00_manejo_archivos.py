"""Abrir y leer un archivo"""

# open(nombre_archivo, modo)
# Modos
# "r - leer",
# "w - Escribir-borra lo anterior"
# "a - Agregar (append)",
# "x - Crear un nuevo archivo-error si ya existe"
# importante utilizar with - context manager
# se encarga de cerrar el archivo automaticamente
# (mejor practica)

from pathlib import Path

ruta = Path(__file__).parent / "cigarra.txt"
ruta_frutas = Path(__file__).parent / "frutas.txt"

# 🧩 Ejemplo 1 — Leer un archivo línea por línea

# with open(ruta, "r", encoding="utf-8") as file:
#     for linea in file:
#         print(linea.strip())


# ✍️ Paso 2: Escribir en un archivo

# with open(ruta, "w", encoding="utf-8") as file:
#     file.write("Las cigarras son insectos.")
#     file.write("Las cigarras son una familia de insectos del orden Hemiptera.")
#     file.write(
#         "Tienen un desarrollo vital completo que dura de dos a diecisiete años, según la especie.")

# print("Archivo creado con exito")

# ➕ Paso 3: Agregar texto sin borrar lo anterior

# with open(ruta, "a", encoding="utf-8") as file:
#     file.write("Las cigarras son geniales.")

# print("Linea añadida")


# 📖 Paso 4: Leer todo el contenido de una sola vez

# with open(ruta, "r", encoding="utf-8") as file:
#     contenido = file.read()

# print("Contenido completo del archivo:")
# print(contenido)

# 🔢 Paso 5: Guardar datos de una lista en un archivo

# frutas = ["manzana", "pera", "banana"]

# with open(ruta_frutas, "w", encoding="utf-8") as file:
#     for fruta in frutas:
#         file.write(fruta + "\n")

# print("lista de frutas guardada")

# with open(ruta_frutas, "r", encoding="utf-8") as file:
#     frutas_leidas = [linea.strip() for linea in file]

# print("Frutas desde el archivo", frutas_leidas)


# 🧠 Paso 6: Manejar errores (opcional pero profesional)
# try:
#     with open("archivo_inexistente", "r", encoding="utf-8") as file:
#         contenido = file.read()
# except FileNotFoundError:
#     print("El archivo no existe")

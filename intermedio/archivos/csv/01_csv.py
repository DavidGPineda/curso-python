import csv
from pathlib import Path

ruta_archivo = Path(__file__).parent / "personas.csv"


# with open(ruta_archivo, "r", encoding="utf-8-sig") as file:
#     # lector_csv = csv.reader(file, delimiter=";")
#     lector_csv = csv.DictReader(file, delimiter=";")
#     # next(lector_csv)  # saltar la primera fila del encabezado

#     for fila in lector_csv:
#         print(
#             f"{fila["nombre"]} vive en {fila["ciudad"]} y tiene {fila["edad"]} años")

# 1. Crear un archivo CSV nuevo

# with open(ruta_archivo, "w", newline="", encoding="utf-8") as file:
#     escritor = csv.writer(file, delimiter=";")
#     escritor.writerow(["nombre", "edad", "ciudad"])  # encabezado
# # Esto crea el archivo personas.csv con una sola línea (el encabezado).

# with open(ruta_archivo, "a", newline="", encoding="utf-8") as file:
#     escritor = csv.writer(file, delimiter=";")
#     escritor.writerow(["Ana", 25, "Bogotá"])
#     escritor.writerow(["Luis", 30, "Medellin"])


# with open(ruta_archivo, "r", encoding="utf-8-sig") as file:
#     lector = csv.DictReader(file, delimiter=";")
#     for fila in lector:
#         print(fila)


# 3. Versión mejorada: entrada del usuario

# with open(ruta_archivo, "a", newline="", encoding="utf-8") as file:
#     escritor = csv.writer(file, delimiter=";")

#     while True:
#         nombre = input("Nombre (o 'fin'): ")
#         if nombre.lower() == "fin":
#             break

#         edad = input("Edad: ")
#         ciudad = input("Ciudad: ")
#         escritor.writerow([nombre, edad, ciudad])
#         print("Persona agregada.\n")

# with open(ruta_archivo, "r", encoding="utf-8-sig") as file:
#     lector = csv.DictReader(file, delimiter=";")
#     for fila in lector:
#         print(fila)

# 1. Crear archivo CSV con encabezados usando DictWriter

# with open(ruta_archivo, "w", newline="", encoding="utf-8") as file:
#     encabezados = ["nombre", "edad", "ciudad"]
#     escritor = csv.DictWriter(file, fieldnames=encabezados, delimiter=";")
#     escritor.writeheader()  # escribe los encabezados en la primera fila


# with open(ruta_archivo, "a", newline="", encoding="utf-8") as file:
#     encabezados = ["nombre", "edad", "ciudad"]
#     escritor = csv.DictWriter(file, fieldnames=encabezados, delimiter=";")

#     escritor.writerow({"nombre": "Ana", "edad": 25, "ciudad": "Bogota"})
#     escritor.writerow({"nombre": "Luis", "edad": 30, "ciudad": "Medellin"})
#     escritor.writerow({"nombre": "bear", "edad": 37, "ciudad": "libano"})


# with open(ruta_archivo, "r", encoding="utf-8-sig") as file:
#     lector = csv.DictReader(file, delimiter=";")
#     for fila in lector:
#         print(fila)


# 3. Con entrada de usuario

# nos aseguramos que el archivo exista y tenga emcabezados

encabezados = ["nombre", "edad", "ciudad"]
if not ruta_archivo.exists():
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as file:
        escritor = csv.DictWriter(file, fieldnames=encabezados, delimiter=";")
        escritor.writeheader()

# Agregar personas
with open(ruta_archivo, "a", newline="", encoding="utf-8") as file:
    escritor = csv.DictWriter(file, fieldnames=encabezados, delimiter=";")

    while True:
        nombre = input("Nombre (0 'fin'): ")
        if nombre.lower() == "fin":
            break

        edad = input("Edad: ")
        ciudad = input("Ciudad: ")
        escritor.writerow({"nombre": nombre, "edad": edad, "ciudad": ciudad})
        print("Persona agregada con exito")


with open(ruta_archivo, "r", encoding="utf-8-sig") as file:
    lector = csv.DictReader(file, delimiter=";")
    for fila in lector:
        print(fila)

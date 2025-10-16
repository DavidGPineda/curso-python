"""
👉 Crea un programa que:

Pida al usuario ingresar nombres de personas.

Guarde cada nombre en un archivo llamado personas.txt.

Al final, lea el archivo y muestre la lista completa.

Ingresa un nombre (o 'fin' para terminar): David
Ingresa un nombre (o 'fin' para terminar): Ana
Ingresa un nombre (o 'fin' para terminar): fin

Personas registradas:
David
Ana

"""
import json
from pathlib import Path

ruta_personas = Path(__file__).parent / "personas.txt"
ruta_personas.touch(exist_ok=True)

# Cargar datos existentes

try:
    with open(ruta_personas, "r", encoding="utf-8") as file:
        contenido = file.read().strip()
        personas = json.loads(contenido) if contenido else []
except json.JSONDecodeError:
    personas = []  # si el archivo esta dañado o vacio
except FileNotFoundError:
    personas = []

# --- Entrada de datos ---

while True:
    nombre = input("Ingresa un nombre (o 'fin' para terminar): ").strip()
    if nombre.lower() == "fin":
        break

    # Evitar duplicados
    if nombre.lower() in [p["nombre"].lower() for p in personas]:
        print("Esa persona ya existe.")
        continue

    try:
        edad = int(input("Edad: ").strip())
    except ValueError:
        print("La edad debe ser un número.")
        continue

    ciudad = input("Ciudad: ").strip()

    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    personas.append(persona)

    # Guardar lista completa en JSON
    with open(ruta_personas, "w", encoding="utf-8") as file:
        json.dump(personas, file, ensure_ascii=False, indent=4)

    print(f"Persona {nombre} guardada correctamente.\n")

# Mostrar lista final

print("\n Lista de personas guardadas:")
for p in personas:
    print(f"- {p['nombre']} ({p['edad']} años) - {p['ciudad']}")

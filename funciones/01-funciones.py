"""Funciones"""


def persona(name, surname="fsociaty"):
    return (f"Hola, {name} {surname}")


def empresa(company, person):
    print(f"Empresa: {company}, Persona: {person}")


empresa("fsociaty", persona("Anderson", "Elliot"))


persona("bear", "elliot")
persona("Elliot", "fsociety")
persona("Darleane")

persona(surname="mr.robot", name="ellie")

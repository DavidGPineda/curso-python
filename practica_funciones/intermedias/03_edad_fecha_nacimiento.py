from datetime import datetime


def calcular_edad(fecha_nacimiento):
    if not isinstance(fecha_nacimiento, str):
        raise TypeError("La fecha debe ser un string con formato YYYY-MM-DD")

    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()

    edad = hoy.year - nacimiento.year

    # Si aún no ha cumplido años este año
    if (hoy.month,  hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1

    return edad


print(calcular_edad("1999-02-10"))  # 26

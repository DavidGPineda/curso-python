from datetime import datetime

# Obtener la fecha actual


def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d -- %H:%M:%S")


print(obtener_fecha_actual())

# Calcular cuantos días hay entre fechas


def dias_entre(fecha1, fecha2):
    f1 = datetime.strptime(fecha1, "%Y-%m-%d")
    f2 = datetime.strptime(fecha2, "%Y-%m-%d")
    return abs((f2 - f1).days)


print(dias_entre("1999-02-10", "2025-10-10"))

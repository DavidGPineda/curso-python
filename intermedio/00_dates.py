""" Dates """

# datetime es un módulo estándar de python que te permite trabajar con:
# Fechas (date)
# Horas (time)
# Fechas y horas juntas (datetime)
# Intervalos de tiempo (timedelta)
# Zonas horarias (timezone)

from datetime import datetime, timezone, timedelta

ahora = datetime.now()
print(ahora)
print(ahora.date())
print(ahora.time())

fecha = datetime(2025, 12, 25, 15, 30)
print(fecha)

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print("Hoy: ", today)
print("Mañana: ", tomorrow)
print("Ayer: ", yesterday)

# Formatear Fechas (strftime)

ahora = datetime.now()
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))

# Convertir texto a fecha (strptime)

texto = "25/12/2025 15:30:00"
fecha = datetime.strptime(texto, "%d/%m/%Y %H:%M:%S")
print(fecha)

# Muy útil cuando recibes fechas desde formularios, JSON, o APIs.

# Zonas horarias (timezone)

# UTC
ahora_utc = datetime.now(timezone.utc)
print("UTC: ", ahora_utc)

# Convertir a otra zona (por ejemplo: Argentina -3h)
argentina = ahora_utc.astimezone(timezone(timedelta(hours=-3)))
print("Argentina:", argentina)

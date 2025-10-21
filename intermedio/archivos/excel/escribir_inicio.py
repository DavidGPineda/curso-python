from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
from pathlib import Path

# Ruta al archivo
ruta_archivo = Path(__file__).parent / "reporte.xlsx"
wb = load_workbook(ruta_archivo)
hoja = wb["Inicio"]

# Escribir datos
# hoja["A1"] = "Reporte General"
# hoja["A2"] = "Generado con Python"
# hoja["A3"] = "Fecha: 2025"

# Aplicar formato
hoja["A1"].font = Font(size=16, bold=True)  # Negrita + grande
hoja["A1"].alignment = Alignment(horizontal="center")  # Centrar texto

hoja["A2"].font = Font(italic=True)  # Cursiva
hoja["A2"].alignment = Alignment(horizontal="left")

# Ajustar ancho de columna
hoja.column_dimensions["A"].width = 35

# Guardar cambios
wb.save(ruta_archivo)
print("Datos escritos en la hoja 'Inicio'")

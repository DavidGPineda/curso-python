from openpyxl import load_workbook
from pathlib import Path

ruta_archivo = Path(__file__).parent / "reporte.xlsx"
wb = load_workbook(ruta_archivo)
hoja = wb["Ventas"]


hoja.delete_rows(2)
wb.save(ruta_archivo)
print("Fila eliminada")

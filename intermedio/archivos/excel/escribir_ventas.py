from openpyxl import load_workbook
from pathlib import Path

# Ruta del archivo Excel
ruta_archivo = Path(__file__).parent / "reporte.xlsx"
wb = load_workbook(ruta_archivo)
hoja = wb["Ventas"]

# Escribir encabezados
# encabezados = ["ID", "Producto", "Precio", "Cantidad", "Total"]
# hoja.append(encabezados)

# Escribir encabezados SOLO si está vacía la hoja
if hoja.max_row == 1 and hoja["A1"].value != "ID":
    hoja.append(["ID", "Producto", "Precio", "Cantidad", "Total"])

# Limpiar fila viejas (opcional pero recomendado)
if hoja.max_row > 1:
    hoja.delete_rows(2, hoja.max_row)

# Datos de ejemplo
ventas = [
    [1, "Laptop Dell", 3500000, 2, 7000000],
    [2, "Mouse Logitech", 80000, 5, 400000],
    [3, "Monitor Samsung", 900000, 1, 900000],
    [4, "Teclado Redragon", 120000, 3, 360000]
]

# Agregar filas
# for fila in ventas:
#     hoja.append(fila)

# Agregar filas con fórmula
fila_inicio = 2
for i, fila in enumerate(ventas, start=fila_inicio):
    hoja.cell(row=i, column=1, value=fila[0])  # ID
    hoja.cell(row=i, column=2, value=fila[1])  # Producto
    hoja.cell(row=i, column=3, value=fila[2])  # Precio
    hoja.cell(row=i, column=4, value=fila[3])  # Cantidad
    hoja.cell(row=i, column=5, value=f"=C{i}*D{i}")  # Formula en "Total"

# Guardar
wb.save(ruta_archivo)
print("Datos agregados correctamente con fórmula en columna TOTAL")

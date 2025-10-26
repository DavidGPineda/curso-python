from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles.protection import Protection
from pathlib import Path

# Ruta del archivo
ruta_archivo = Path(__file__).parent / "reportes.xlsx"
wb = load_workbook(ruta_archivo)
hoja = wb["Inventario"]

# ---- 1. Crear validaciones ----

# ID (entero positivo)
dv_id = DataValidation(type="whole", operator="greaterThan", formula1="0",
                       allow_blank=False, showErrorMessage=True,
                       error="Ups! ID debe ser un número entero único 😎")
hoja.add_data_validation(dv_id)
dv_id.add(f"A2:A1001")

# Producto (texto obligatorio)
dv_producto = DataValidation(type="custom", formula1='LEN(B2)>0',
                             allow_blank=False, showErrorMessage=True,
                             error="Ups! El producto no puede estar vacío 👇")
hoja.add_data_validation(dv_producto)
dv_producto.add(f"B2:B1001")

# Categoría (lista desplegable)
categorias = ["Hombre", "Mujer", "Unisex", "Niños", "Accesorios"]
dv_categoria = DataValidation(type="list", formula1=f'"{",".join(categorias)}"',
                              allow_blank=False, showDropDown=True,
                              showErrorMessage=True,
                              error="Ups! Selecciona una categoría válida 👇")
hoja.add_data_validation(dv_categoria)
dv_categoria.add(f"C2:C1001")

# Talla (lista desplegable, permite vacío o "-")
tallas = ["XS", "S", "M", "L", "XL", "XXL", "-"]
dv_talla = DataValidation(type="list", formula1=f'"{",".join(tallas)}"',
                          allow_blank=True, showDropDown=True,
                          showErrorMessage=True,
                          error="Ups! Selecciona una talla válida o '-' 👇")
hoja.add_data_validation(dv_talla)
dv_talla.add(f"D2:D1001")

# Stock (entero ≥ 0)
dv_stock = DataValidation(type="whole", operator="greaterThanOrEqual", formula1="0",
                          allow_blank=False, showErrorMessage=True,
                          error="Ups! En Stock solo se permiten números positivos 👇")
hoja.add_data_validation(dv_stock)
dv_stock.add(f"E2:E1001")

# Precio (número ≥ 0)
dv_precio = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0",
                           allow_blank=False, showErrorMessage=True,
                           error="Ups! Precio debe ser positivo 👇")
hoja.add_data_validation(dv_precio)
dv_precio.add(f"F2:F1001")

# Valor Total (bloqueada para edición)
for fila in range(2, 1002):
    hoja[f"G{fila}"].protection = Protection(locked=True)


# ---- 2. Activar protección de hoja ----
# Nota: La hoja se protegerá para que Valor Total no se edite
hoja.protection.sheet = True
hoja.protection.enable()

# ---- 3. Guardar cambios ----
wb.save(ruta_archivo)
print("✅ Validaciones profesionales aplicadas en Inventario con mensajes amigables")

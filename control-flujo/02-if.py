edad = 60

if edad >= 70:
    print("Entra gratis")
elif edad >= 55:
    print("Entra con descuento")
elif edad >= 18:
    print("Puedes ver la peli")
else:
    print("No puedes entrar")

print("Listo")

# El orden es importante ya que si ponemos el >= a 18 en
# primer lugar no va evaluar otros elif ya que el primero fue verdadero

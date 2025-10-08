# and, or, not

# and => los dos deben ser verdaderos o falsos para que sea
# true, si uno es true y otro false, pues false

# or => en caso que alguno sea true, va a ser true, solo se necesita uno, si ambos son false, sera false

# not => negara el resultado de la operacion

gas = False
encendido = True
edad = 18

if not gas and encendido and edad > 17:
    print("Puedes avanzar")


# and → ambas deben cumplirse
# or → al menos una
# not → niega (invierte el resultado lógico)

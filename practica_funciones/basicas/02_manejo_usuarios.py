def nombre_completo(nombre, apellido):
    return f"{nombre.capitalize()} {apellido.capitalize()}"


print(nombre_completo("bear", "pineda"))

# Verificar si un correo es valido (version simple)


def correo_valido(email):
    return "@" in email and "." in email


print(correo_valido("usuario@gmail.com"))  # True
print(correo_valido("usuariogmail.com"))  # False

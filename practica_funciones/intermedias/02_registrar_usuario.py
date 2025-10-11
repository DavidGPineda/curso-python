def registrar_usuario(nombre, edad, correo):
    if not isinstance(nombre, str) or len(nombre.strip()) == 0:
        raise ValueError("El nombre debe ser un texto válido")

    if not isinstance(edad, int) or edad < 18:
        raise ValueError("Debe ser mayor de edad para registrarme")

    if not isinstance(correo, str) or "@" not in correo:
        raise ValueError("Correo electronico inválido")

    return {
        "nombre": nombre.strip().capitalize(),
        "edad": edad,
        "correo": correo.strip().lower()
    }


usuario = registrar_usuario(" bear ", 22, "BEAR@correo.com")
print(usuario)

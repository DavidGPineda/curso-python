# Contar cuántas palabras tiene un texto
def contar_palabras(texto):
    return len(texto.split())


print(contar_palabras("Hola soy bear y me gusta programar"))


# Limpiar texto (por ejemplo, antes de guardar en base de datos)
def limpiar_texto(texto):
    return texto.strip().lower()


print(limpiar_texto(" Hola bear "))

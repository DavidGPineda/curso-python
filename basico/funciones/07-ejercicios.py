def no_espace(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_polindromo(text):
    texto = no_espace(text)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_polindromo("amo la paloma"))

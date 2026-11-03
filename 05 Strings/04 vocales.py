def quita_vocales(texto: str) -> str:
    # vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    # resultado = ""
    # for letra in texto:
    #     if letra not in vocales:
    #         resultado += letra
    # return resultado

    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    for vocal in vocales:
        texto = texto.replace(vocal, "")
    return texto
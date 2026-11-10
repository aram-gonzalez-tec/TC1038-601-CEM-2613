def cambio(texto: str) -> str:
    resultado = ""
    vocales = "aeioua"
    for caracter in texto:
        if caracter in vocales:
            resultado += vocales[vocales.find(caracter)+1]
        else:
            resultado += caracter
    return texto
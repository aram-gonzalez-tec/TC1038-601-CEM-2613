def es_palíndromo(texto: str) -> bool:
    texto = texto.lower()
    nuevo_texto = ""
    for caracter in texto:
        if caracter.isalpha():
            nuevo_texto += caracter
    return nuevo_texto == nuevo_texto[::-1]
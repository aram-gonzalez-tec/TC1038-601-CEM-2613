def iniciales(nombre: str) -> str:
    iniciales = ""
    for parte in nombre.split():
        iniciales += parte[0].upper()
    return iniciales
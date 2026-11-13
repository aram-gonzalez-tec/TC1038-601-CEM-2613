def eliminar_ocurrencias(lista: list, elemento) -> list:
    # Eliminando
    lista = lista.copy()
    while elemento in lista:
        lista.remove(elemento)
    return lista
    # Construyendo
    resultado = []
    for i in lista:
        if i != elemento:
            resultado.append(i)
    return resultado
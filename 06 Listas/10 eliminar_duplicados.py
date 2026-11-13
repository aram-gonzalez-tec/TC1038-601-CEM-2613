def eliminar_duplicados(lista: list) -> list:
    resultado = []
    for i in lista:
        if i not in resultado:
            resultado.append(i)
    return resultado

lista = [24,65,3,46,3,2,1,4,3,21,2,3,1,1,1,2]
print(eliminar_duplicados(lista))
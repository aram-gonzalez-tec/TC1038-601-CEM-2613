def k_elementos(lista: list, número: int) -> list:
    return lista[::número]

lista = [1,2,3,4,5,6,7,8,9]
número = 3
print(k_elementos(lista, número)) # -> [1,4,7]
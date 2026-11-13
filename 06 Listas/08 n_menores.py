def n_menores(lista: list, número: int) -> list:
    if número <= len(lista):
        return sorted(lista)[:número]

lista = [4,6,3,4,7,4,22,45,1,1,3,56,3]
print(n_menores(lista, 3))
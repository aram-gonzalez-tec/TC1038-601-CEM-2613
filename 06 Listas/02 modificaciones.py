lista = [1,2,3,4,5]
# Agregar un elemento
# lista.append(elemento) -> Agregar un elemento al final de la lista
lista.append(6)
print(lista)
lista.insert(2, "nuevo")
print(lista)
lista.insert(10, "otro elemento")
print(lista)
lista.insert(-20, "otro más")
print(lista)
# Eliminar elementos
eliminado = lista.pop()
print(f"Elemento elminado: {eliminado}")
print(lista)
eliminado = lista.pop(3)
print(f"Elemento elminado: {eliminado}")
print(lista)
del lista[0]
print(lista)
# Extend
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)
print(lista1)
print(lista2)

def suma_listas(lista1, lista2):
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma
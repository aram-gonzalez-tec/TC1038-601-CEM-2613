lista = [3,6,3,2,7,8,5,3,2,8,5,3,2,1,3,5,1]
print(lista.count(2)) # Cuántas veces aparece el elemento en la lista
print(lista.index(5)) # Encuentra la primera ocurrencia del elemento
lista_ordenada = sorted(lista) # Genera una nueva lista con el contenido ordenado
print(lista)
print(lista_ordenada)
lista.sort() # Ordena la lista existente
print(lista)
lista.sort(reverse=True) # Ordena de manera descendente
print(lista)
lista.reverse() # Invierte el orden de la lista
print(lista)
lista = ["zorro", "aeroplano", "manzana", "plátano", "Azucar", "Zebra"]
lista.sort()
print(lista)
lista = [
    [867684, "Juan", 100],
    [448384, "Pablo", 50],
    [947574, "Aaron", 70],
]
def llave(elemento):
    return elemento[2]
lista.sort(key=llave)
print(lista)
lista.sort(key=lambda elemento: elemento[2])
print(lista)
# ---------------------------------
lista = [1,2,3,4,5,6,5,8,7,9,7,5,9,8,4,1]
print(len(lista)) # Cuántos elementos tiene la lista
print(min(lista)) # Valor más pequeño de la lista
print(max(lista)) # Valor más grande de la lista
print(sum(lista)) # Suma de elementos de la lista

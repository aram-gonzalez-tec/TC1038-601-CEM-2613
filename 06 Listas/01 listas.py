lista = [1,4,6,True,[5,7], "hola"]
print(lista)
lista = [] 
print(lista)
lista = [0] * 5
print(lista)
lista = [1,2] + [4,5]
print(lista)
# -------------------------------
lista = [2,4,"Hola",[7,8,["adiós",True],65],99,100]
print(lista[2])
print(lista[3])
print(lista[3][-1])
print(lista[3][2][0])
# slicing
print(lista[2:])
# Cambiar un elemento
lista[-2] = "otro elemento"
print(lista)
lista[3][2][0] = "otro cambio"
print(lista)
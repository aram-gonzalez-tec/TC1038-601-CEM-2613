# for i in range(inicio, final, paso)
# for i in range(5,11,2)
i = 5 # inicio
while i <= 10: # final
    print(f"El valor de i es: {i}")
    # i = i + 2
    i += 2 # paso
print("-"*30)

# for i in texto:
texto = "Hola mundo"
print(texto[3])
print(texto[-7])
i = 0
while i < len(texto):
    print(f"texto[{i}] -> {texto[i]}")
    i += 1
print("-"*30)

i = -1
while i >= -len(texto):
    print(f"texto[{i}] -> {texto[i]}")
    i -= 1

lista = [3,6,3,"hola",True]
i = 0
while i < len(lista):
    print(f"lista[{i}] -> {lista[i]}")
    i += 1
print("-"*30)

seguir_jugando = "1"
while seguir_jugando == "1":
    print("Lógica del juego...")
    seguir_jugando = input("¿Volver a jugar? 1) Sí, 2)No: ").strip()
    while seguir_jugando != "1" and seguir_jugando != "2":
        print("Error, debes seleccionar 1 para sí o 2 para no.")
        seguir_jugando = input("¿Volver a jugar? 1) Sí, 2)No: ").strip()
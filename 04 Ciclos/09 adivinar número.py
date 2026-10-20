import random

secreto = random.randint(1,100)
intentos = 1
intento = int(input("Adivina el número entre 1 y 100: "))
while intento != secreto:
    if intento < secreto:
        print("El número que buscas es mayor.")
    elif intento > secreto:
        print("El número que buscas es menor.")
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
print(f"Adivinase el número, te tomó {intentos} intentos.")
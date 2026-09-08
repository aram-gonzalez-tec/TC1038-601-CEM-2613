import random

opción = int(input("""Bienvenido al juego de dados.
Adivina cuál será el resultado de la suma de dos dados:
1) Abajo de 7
2) Igual a 7
3) Arriba de 7
Ingresa tu opción: """))
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma_dados = dado1 + dado2
print(f"El primer dado cayó: {dado1}")
print(f"El segundo dado cayó: {dado2}")
print(f"La suma de los dados fue: {suma_dados}")
if suma_dados < 7 and opción == 1 \
    or suma_dados == 7 and opción == 2 \
        or suma_dados > 7 and opción == 3:
    print("Felicidades, atinaste a la suma.")
else:
    print("Perdiste, más suerte para la próxima.")
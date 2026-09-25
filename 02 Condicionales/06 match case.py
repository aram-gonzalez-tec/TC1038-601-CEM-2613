edad = int(input("Ingresa tu edad: "))
match edad:
    case _ if edad >= 18:
        print("Eres mayor de edad.")
    case _:
        faltante = 18 - edad
        print(f"Te faltan {faltante} años para ser mayor de edad.")
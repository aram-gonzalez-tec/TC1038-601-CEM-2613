edad = int(input("Ingrese su edad: "))
licencia = int(input("¿Tienes licencia? 1)Sí 2)No: "))
if edad >= 18 and licencia == 1:
    print("Puedes rentar un auto.")
else:
    if edad < 18:
        print("Eres menor de edad, no cumples este requisito.")
    if licencia == 2:
        print("No tienes licencia, no cumples este requisito.")
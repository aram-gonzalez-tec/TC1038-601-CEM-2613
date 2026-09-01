# Introducir una calificación
# Escribir su equivalente en letra
# (90, 100] -> A
# (80, 90] -> B
# (70, 89] -> C
# [0, 70] -> F
calificación = float(input("Ingresa tu calificación: "))
if calificación > 90:
    print("A")
else:
    if calificación > 80:
        print("B")
    else:
        if calificación > 70:
            print("C")
        else:
            print("F")
# -----------------------------------
if calificación > 90:
    print("A")
elif calificación > 80:
    print("B")
elif calificación > 70:
    print("C")
else:
    print("F")
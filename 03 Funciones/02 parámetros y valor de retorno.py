# Función sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"La suma es: {resultado}")
#suma1()

# Función con parámetros y sin valor de retorno
def suma2(x: float, y: float) -> None:
    resultado = x + y
    print(f"La suma es: {resultado}")

# suma2(50, 100)
# a = float(input("Ingresa el valor de x: "))
# b = float(input("Ingresa el valor de y: "))
# suma2(a, b)
# suma2("hola", "mundo")

# Función con parámetros y con valor de retorno
def suma3(x: float, y: float) -> float:
    resultado = x + y
    return resultado

x = suma3(6, suma3(5, 8) + 7 / 2)
y = suma3(x, 25)

    
# def a():
#     def b():
#         print("B")
#     return b

def hola():
    print("Hola")
    return ""
    print("Adiós") # Esta línea de código es inalcanzable

# Crear una función de nombre calificación(número) que reciba un
# número de punto flotante y como valor de retorno devuelva el
# equivalente de la calificación en letra en base a los siguientes
# rangos:
# >= 90 -> A
# >= 80 -> B
# >= 70 -> C
# < 70 -> F

def calificación(número: float) -> str:
    if número >= 90:
        return "A"
    elif número >= 80:
        return "B"
    elif número >= 70:
        return "C"
    return "F"

def fórmula_general(a: float = 1, b: float = 5, c:float = 1) -> float:
    x1 = (-b + (b**2 - 4*a*c)**(0.5)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5)) / (2*a)
    return x1, x2

resultado = fórmula_general(1,5,1)
print(f"El resultado es: {resultado}")
res1 = resultado[0]
res2 = resultado[1]
print(f"El valor de x1 es: {res1}")
print(f"El valor de x2 es: {res2}")
r1, r2 = fórmula_general(1,5,1)
print(f"El valor de x1 es: {r1}")
print(f"El valor de x2 es: {r2}")
resultado = fórmula_general(c=50,a=10,b=100)
resultado = fórmula_general(10,c=50,b=100)
resultado = fórmula_general(10,c=50)

print("Hola", "mudo", sep="+-+", end="???")
print("Hola", "mudo", sep="+-+", end="???")

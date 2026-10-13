def porcentaje(cantidad: float, pct:float) -> float|None:
    if pct < 0 or pct > 100:
        return None
    return cantidad * pct / 100

def clasificar_numero(n: int) -> str:
    if n == 0:
        return "cero"
    if n > 0:
        signo = "positivo"
    else:
        signo = "negativo"
    if n % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    return f"{signo} {paridad}"

def mayor_de_dos(a: float, b: float) -> float:
    if a > b:  
        return a
    return b

def mayor_de_tres(a: float, b: float, c: float) -> float:
    return mayor_de_dos(mayor_de_dos(a,b), c)

def es_bisiesto(año: int) -> bool:
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def días_en_mes(mes: int, año: int) -> int:
    if mes == 2:
        if es_bisiesto(año):
            return 29
        return 28
    elif mes in [4,6,9,11]:
        return 30
    elif mes in [1,3,5,7,8,12]:
        return 31
    return -1

if __name__ == "__main__":
    # cantidad = 100
    # pct = 15
    # res = porcentaje(cantidad, pct)
    # print(f"El resultado de porcentaje({cantidad},{pct}) es: {res}")
    # cantidad = 100
    # pct = -15
    # res = porcentaje(cantidad, pct)
    # print(f"El resultado de porcentaje({cantidad},{pct}) es: {res}")
    # cantidad = 100
    # pct = 0
    # res = porcentaje(cantidad, pct)
    # print(f"El resultado de porcentaje({cantidad},{pct}) es: {res}")
    # cantidad = 100
    # pct = 100
    # res = porcentaje(cantidad, pct)
    # print(f"El resultado de porcentaje({cantidad},{pct}) es: {res}")
    # cantidad = 100
    # pct = 120
    # res = porcentaje(cantidad, pct)
    # print(f"El resultado de porcentaje({cantidad},{pct}) es: {res}")
    n = 0
    res = clasificar_numero(n)
    print(f"El número {n} es: {res}")
    n = 8
    res = clasificar_numero(n)
    print(f"El número {n} es: {res}")
    n = -8
    res = clasificar_numero(n)
    print(f"El número {n} es: {res}")
    n = 5
    res = clasificar_numero(n)
    print(f"El número {n} es: {res}")
    n = -5
    res = clasificar_numero(n)
    print(f"El número {n} es: {res}")
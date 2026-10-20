def primo(n: int) -> bool:
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# Crea una función muestra_primos(n) que permita ingresar un 
# número n y que imprima todos los números primos que están 
# entre 2 y n (inclusivos).

def muestra_primos(n: int) -> None:
    for i in range(2,n+1):
        if primo(i):
            print(i)
            
if __name__ == "__main__":
    muestra_primos(5)


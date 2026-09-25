def raíz_cuadrada(número: int) -> float:
    return número ** 0.5

if __name__ == "__main__":
    prueba = raíz_cuadrada(4)
    print(f"Resultado: {prueba}")
    prueba = raíz_cuadrada(-4)
    print(f"Resultado: {prueba}")
    prueba = raíz_cuadrada(0)
    print(f"Resultado: {prueba}")

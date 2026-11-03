cuenta = 0
while (precio := float(input("Ingrese el precio del producto: "))) >= 0:
    cuenta += precio
print(f"El total a pagar es: ${cuenta:,.2f}")
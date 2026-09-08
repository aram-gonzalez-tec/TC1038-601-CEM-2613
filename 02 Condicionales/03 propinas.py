monto = float(input("Ingrese el monto de la cuenta: "))
personas = int(input("Ingrese el número de personas: "))
por_persona = monto / personas
if por_persona < 150:
    propina = 10
elif por_persona >= 150 and por_persona <= 250:
    propina = 13
else:
    propina = 15
total = por_persona * (1 + propina / 100)
print(f"Total a pagar: ${total:,.2f}, se incluyó {propina}% de propina.")
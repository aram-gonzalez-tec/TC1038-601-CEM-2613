a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# Formas antiguas
# print("x1 es:", x1)
# print("x1 es " + str(x1))
# print("x1 es {0}, x2 es: {1}".format(x1, x2))

# f-strings
# : -> aplicar formato especial
# , -> separador de miles
# .4 -> redondear a 4 decimales
# f -> formato float (si no se pone se imprime en formato científico)
print(f"x1 es: {x1:,.4f}")
print(f"x2 es: {x2:,.4f}")
# print(f"Ejemplo separador: {373_898_477_328.3443:,.1}")
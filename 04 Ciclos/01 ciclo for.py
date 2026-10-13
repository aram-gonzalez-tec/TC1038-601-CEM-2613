lista = [1,2,3,4,5]

for i in lista:
    print(f"El valor de i es: {i}")
print("-"*30)

texto = "Hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
print("-"*30)
    
# range(final) -> Secuencia numérica que empieza en 0, avanza
# de 1 en 1 y termina antes de final
for i in range(5):
    print(f"El valor de i es: {i}")
print("-"*30)

# range(inicio, final) -> Secuencia numérica que empieza en inicio,
# avanza de +1 en +1 y termina antes de final
for i in range(5,10):
    print(f"El valor de i es: {i}")
print("-"*30)    

for i in range(10, 5):
    print(f"El valor de i es: {i}")
print("-"*30)

# range(inicio, final, paso) -> Secuencia numérica que inicia en inicio,
# avanza de paso en paso y termina antes de llegar a final
for i in range(10,5,-1):
    print(f"El valor de i es: {i}")
alumnos = ["Ángel", "Román", "Perla", "Diego", "David"]
nombre = input("Ingresa el nombre del alumno a buscar: ")
encontrado = False
for alumno in alumnos:
    if nombre == alumno:
        encontrado = True
if encontrado:        
    print(f"{nombre} sí está en la lista.")
else:
    print(f"{nombre} no está en la lista.")
    
# ----------------------------------------

for alumno in alumnos:
    if nombre == alumno:
        print(f"{nombre} sí está en la lista.")
        break
else: # Sólo se ejecuta en caso de que el ciclo no haya ejecutado break
    print(f"{nombre} no está en la lista.")
texto = "Hola MUNDO, ¿cómo Estás?"
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.replace("o", "0"))
print(texto.replace("Hola", ""))
texto = "    \n     hola    \t     "
print(texto.lstrip())
print(texto.rstrip())
print(texto.strip())
texto = "Hola mundo, ¿cómo estás?"
print(texto.split())
print(texto.split("o"))
lista = ["Hola", "mundo", "aquí", "estoy"]
print("+-+".join(lista))

texto = "Hola mundo"
print(len(texto))

print(texto.islower()) # ¿Todo está en minúsculas?
print(texto.isupper()) # ¿Todo está en mayúsculas?

print(texto.isalpha()) # ¿Todo es parte del alfabeto?
print(texto.isnumeric()) # ¿Todo es un número?
print(texto.isalnum()) # ¿Todo es alfanumérico?

print(texto.count("o")) # ¿Cuántas veces aparece la o?

print(texto.find("o"))
print(texto.index("o"))

print(texto.find("z"))
if "z" in texto:
    print(texto.index("z"))
    
print(texto.startswith("Ho"))
print(texto.endswith("la"))
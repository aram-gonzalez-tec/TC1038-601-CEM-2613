lista = ["hola", "mundo", "casa", "árbol"]
# 1. hola
# 2. mundo
# 3. casa
# 4. árbol
for i in range(len(lista)):
    print(f"{i+1}. {lista[i]}")
    
print("-"*30)

for k,v in enumerate(lista):
    print(f"{k+1}. {v}")
número = int(input("Ingresa un número: "))
if número % 3 == 0 and número % 5 == 0:
    print("FizzBuzz")
elif número % 3 == 0:
    print("Fizz")
elif número % 5 == 0:
    print("Buzz")
else:
    print(f"{número} no es divisible ni entre 3 ni entre 5")
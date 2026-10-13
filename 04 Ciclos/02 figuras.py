# Generar una función de nombre dibujar_figura(n, largo) que reciba el 
# número de lados de la figura y dibuje un poligono regular del
# número de lados indicado y con el largo recibido.
import turtle as t

def dibujar_figura(n: int, largo: int) -> None:
    for i in range(n):
        t.forward(largo)
        t.left(360/n)

if __name__ == "__main__":
    for i in range(4,10):
        dibujar_figura(i, 100)
        t.forward(200)
    t.mainloop()
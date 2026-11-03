import turtle as t

def figura(lados: int, largo: int) -> None:
    t.forward(largo)
    t.left(360/lados)
    
def espirógrafo(lados: int, largo: int, repeticiones: int, ángulo: int) -> None:
    for i in range(repeticiones):
        figura(lados, largo)
        t.left(ángulo)

if __name__ == "__main__":
    t.speed(0)
    espirógrafo(4, 100, 50, 10)
    t.mainloop()
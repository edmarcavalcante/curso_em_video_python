from termostato import Termostato
from property_RealPython import Circle
from validating_input import Point


def main():
    t1 = Termostato()
    t1.aumentar
    print(t1.valor)
    t1.valor = 25
    print(t1.valor)

    t1.valor = 28
    print(t1.valor)
    t1.valor = 19
    print(t1.valor)
    t1.valor = 10
    print(t1.valor)

    t1.aumentar
    print(t1._temperatura)
    print("="*60)

    c1 = Circle(20)
    
    c1.radius
    c1.radius = 30
    c1.radius
    #del c1
    print(c1.radius)

    print("="*30 + "Point Class" + "="*30)

    p1 = Point(20, 15)
    p1.x
    p1.y
    p1.x = 10
    p1.x
    

if __name__ == "__main__":
    main()
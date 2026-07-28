from termostato import Termostato
from property_RealPython import Circle
from validating_input import Point
from logging_exemplo import Circle_


def main():

    print("="*20 + "Início termostato" + "="*20)
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

    print("Agora com aumento")
    t1.aumentar()
    print(t1.valor)

    #print("="*60)

    print("="*20 + "Início Circle" +  "="*20)
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

    print("="*30 + "Logging Class" + "="*30)
    cc1 = Circle_(12)
    cc1.radius = 100
    cc1.radius
    cc1.radius = "Edmar"




if __name__ == "__main__":
    main()
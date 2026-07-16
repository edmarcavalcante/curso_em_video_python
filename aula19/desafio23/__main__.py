from classe_poligono import Poligono
from quadrado import Quadrado
from circulo import Circulo



def main():
    q1 = Quadrado(5)
    c1 = Circulo(6)

    
    q1.perimetro() 
    q1.area()
    
    c1.perimetro()
    c1.area()
    

if __name__ == "__main__":
    main()
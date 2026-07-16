from classe_poligono import Poligono
from math import pi
#Circulo(Poligono)
#-raio
#perimetro() 
#area()

class Circulo(Poligono):

    def __init__(self,raio, qnt_lados = 1):
        super().__init__(qnt_lados)
        self.raio = raio
    
    def perimetro(self):
        print(f'O perímetro do círculo é: {2* pi * self.raio:.2f}.')

    def area(self):
        print(f'A área do círculo é: {pi*self.raio**2:.2f}')
    
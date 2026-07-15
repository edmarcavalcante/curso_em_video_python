# Criar uma classe Polígono que contenha:

#Poligono(ABS)
#-qnt_lados
#perimetro() {abstratct}
#area() {abstratct}

#Quadrado(Poligono)
#-comprimento_lado
#perimetro() 
#area() 

#Circulo(Poligono)
#-raio
#perimetro() 
#area() 

from abc import ABC 
from abc import abstractmethod

class Poligono(ABC):
    
    def __init__(self,qnt_lados:int):
        self.qnt_lados = qnt_lados

    @abstractmethod
    def perimetro():
        pass

    @abstractmethod
    def area():
        pass
    





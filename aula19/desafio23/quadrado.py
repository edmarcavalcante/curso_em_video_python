from classe_poligono import Poligono

#Quadrado(Poligono)
#-Comprimento_lado
#perimetro() 
#area()

class Quadrado(Poligono):
    
    def __init__(self, comprimento_lado, qnt_lados = 4):
        super().__init__(qnt_lados)
        self.comprimento = comprimento_lado
        
    
    def perimetro(self):
        print (f'O perímetro do quadrado é {self.qnt_lados * self.comprimento}')

    def area(self):
        print (f'A área do quadrado é {self.comprimento ** 2}')

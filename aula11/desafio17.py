# Criar etiqueta de nome e preço de produtos

from rich import print
from rich.panel import Panel

class Produto ():

    def __init__(self,nome:str,preco:float)-> str:
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = Panel(f'Meu produto é {self.nome} e custa {self.preco:,.2f}',title="Etiqueta do Produto",width=40,)
        return conteudo

p1 = Produto("carro",150.8925)
print(p1.etiqueta())
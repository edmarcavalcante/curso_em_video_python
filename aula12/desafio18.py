
from rich import print
from rich.panel import Panel
# Criar um classe que faz um levantamento de custo de um churrasco
# considerando a quantidade de pessoas e o kg da carne

class Churrasco():
    
    preco_carne = float(45.50)
    consumo_medio = float(0.4)

    def __init__(self, nome_currasco:str, qnt_convidados:int):
        self.nome = nome_currasco
        self.qnt = qnt_convidados

    
    def analisar(self):
        quant_carne_total = self.consumo_medio * self.qnt
        valor_pessoa = (quant_carne_total*self.preco_carne) / self.qnt

        texto1 = f'Analisando o [red]{self.nome}[/red] com [blue]{self.qnt}[/blue] pessoas!'
        texto2 = f'Cada participante comerá [blue]{self.consumo_medio}[/blue] kg ao custo de [blue]R$ {self.preco_carne}[/blue]'
        texto3 = f'Recomenda-se comprar [blue]{quant_carne_total} kg[/blue] de carne.'
        texto4 = f'Será necessário [blue]Kg {quant_carne_total*self.preco_carne}[/blue] de carne.'
        texto5 = f'Cada pessoa pagará [blue]R$ {valor_pessoa}[/blue] para participar.'
        texto6 = f'{texto1} \n{texto2}\n{texto3}\n{texto4}\n{texto5}'
        
        painel = Panel(texto6,title=self.nome,width=60,)

        return painel
    
ch1 = Churrasco("Churras da Firma", 15)
print(ch1.analisar())







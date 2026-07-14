# Classe funcionário
from  rich import inspect, print, console  
class Funcionario():
    empresa = "Leonardo D'Vinci"
    def __init__(self,nome:str,setor:str,cargo:str) -> str:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, sou {self.nome} e sou {self.cargo} do setor {self.setor} da empresa [red]{self.empresa}'

func1 = Funcionario('Edmar','CMA', 'Auditor')

print(func1)
print(func1.apresentacao())
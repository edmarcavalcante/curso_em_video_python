

#Criar uma classe que simule o comportamwnto de um livro

class Livro():

    def __init__(self,nome:str,total_pg:int):
        self.nome = nome
        self.total_pg = total_pg
        self.pg_atual = 1


    def passar(self,qnt = 1):
        
        self.qnt = qnt
        
        
        if (self.qnt + self.pg_atual) > self.total_pg:
            
            print(f'O livro tem {self.total_pg} ao total. Você está ultrapassando o limite.')
            self.pg_atual = self.total_pg
        
        else:
            self.pg_atual += self.qnt
            print(f'Você passou {self.qnt} e agora está na página {self.pg_atual} do livro.')
        
        return self.pg_atual

        


    
liv1 = Livro("100 dias entre o céu e o mar", 80)

liv1.passar(15)
#print(liv1.pg_atual)
liv1.passar(20)
liv1.passar(60)
liv1.passar(30)


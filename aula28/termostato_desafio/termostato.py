# Desafio 28 — Termostato Orientado a Objetos
#Classe: Termostato
#Atributo privado/protegido para armazenar a temperatura interna.
#Propriedade validável temperatura:
#Temperatura padrão de inicialização: 24ºC.
#Faixa permitida: entre 16.0ºC e 30.0ºC (valores abaixo de 16 ficam travados em 16; acima de 30 ficam travados em 30).
#Passo de ajuste: aceita apenas incrementos/valores de meio em meio grau (ex: 24.0, 24.5, 25.0). Valores como 25.2 devem ser rejeitados ou lançar erro de valor inválido.
#Propriedade f_temperatura (somente leitura): retorna uma string da temperatura já formatada com o símbolo de graus (ex: "25.0ºC").

class Termostato:
    def __init__(self, valor:float = 20):
        self._temperatura = valor

    
    @property
    def valor(self):
        return self._temperatura
    
    @valor.setter
    def valor(self,valor):
        if 16 <= valor <= 30:
            self._temperatura = valor
        else:
            print("Valor inválido")


    
    def aumentar (self):
        
        self._temperatura += 0.5 
        
class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota #método protegido

    # MÉTODOS ACESSORES  (GET SET)
    def get_nota(self):
        print(f"{self._nota}")
    
    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print (f"Valor inválido")

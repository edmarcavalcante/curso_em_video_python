class Avaliacao2:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota #método protegido

    # o @property é utilizado para manipulação de atributos validáveis

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0<= valor <=10:
            self._nota = valor
        else:
            print(f"Valor inválido >> {valor}")

    @nota.deleter
    def nota(self):
        pass

    # Diferença entre @property e métodos acessores (get set)
    # com @property você pode atribuir valor a um atributo da seguinte forma

    # >> classe.nota = 10

    # Se for utilizar os métodos acessores:

    # >> classe.set_nota(10)    
from classe_avaliacao import Avaliacao
from classe_avaliacao2 import Avaliacao2
from rich import inspect, print

def main():
    av1 = Avaliacao("Pedro", "Matemática", 10)
    inspect(av1, private=True) # esse parâmetro permite visualizar os métodos privados
    av1.set_nota(50)
    av1.set_nota(-1)
    av1.get_nota()
    av1.set_nota(9.5)
    av1.get_nota()

    av2 = Avaliacao2("Maria", "Pintura", 10)
    av2.nota = 5
    print(av2.nota)
    inspect(av2, private=True)
    av2.nota = 8
    print(av2.nota)
    inspect(av2, private=True)
    av2.nota = 11
    print(av2.nota)
    inspect(av2, private=True)


if __name__ == "__main__":
    main()


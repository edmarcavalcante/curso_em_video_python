from rich import print
from rich.panel import Panel
from rich.style import Style
from classe_transporte import Transporte
from classe_moto import Moto

estilo = Style(color="red",bgcolor="white",bold=True,italic=True)


def main():

    m1 = Moto(50,9.5)
    m1.calc_frete()

if __name__=="__main__":
    main()

from rich import print
from rich import inspect
from rich.panel import Panel
from rich.style import Style
from classe_transporte import Transporte
from classe_moto import Moto
from classe_caminhao import Caminhao
from rich import print
from rich.table import Table

estilo = Style(color="red",bgcolor="white",bold=True,italic=True)


def main():

    m1 = Moto(50,9.5)
    m1.calc_frete()
    print(inspect(m1))
    c1 = Caminhao(60,9.5)
    c1.calc_frete()
    print(inspect(c1))

    lista = [m1, c1]
    
    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("KM")
    tabela.add_column("Transporte")
    tabela.add_column("Preço R$")

    for item in lista:
        print(dir(item))
        tabela.add_row(f"{item.distancia}", item.__class__.__name__, f"{item.calc_frete()}")

    print(tabela)




if __name__=="__main__":
    main()

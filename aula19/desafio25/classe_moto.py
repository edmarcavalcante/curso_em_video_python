from classe_transporte import Transporte
from rich import print
from rich.panel import Panel
from rich.style import Style
from rich.theme import Theme
from rich.console import Console

estilo = Style(color="red",bgcolor="white",bold=True,italic=True)

from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "dim cyan",
    "logging.level.critical": " bold reverse red",
    "danger": "bold red"})


class Moto(Transporte):
    def __init__(self, distancia, frete,fator=0.50):
        super().__init__(distancia, frete)
        self.fator = fator

    def calc_frete(self):
        console = Console(theme=custom_theme)
        print("\n"*5)
        console.print(f'O frete custa [logging.level.critical]R$ {self.frete}[/logging.level.critical] por Km. A distância é [logging.level.critical]{self.distancia}[/logging.level.critical] e o fator é [logging.level.critical]{self.fator}[/logging.level.critical]. Logo o custo do frete de moto fica => [logging.level.critical]R$ {self.distancia*self.frete*self.fator}[/logging.level.critical] ')    
        print("\n"*3)

        return self.distancia*self.frete*self.fator
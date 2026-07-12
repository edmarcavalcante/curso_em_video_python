from rich import print
from rich.table import Table

minha_tabela = Table(title="[red]Minha Tabela",caption="[yellow]Aqui é o caption")

minha_tabela.add_column("Nome",justify="right")
minha_tabela.add_column("Preço",justify="center")
minha_tabela.add_row("Feijão", "R$ 8,00")
minha_tabela.add_row("Arroz", "R$ 6,50")

print(minha_tabela)
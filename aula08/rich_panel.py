from rich import print
from rich.panel import Panel

caixa = Panel("[white]Esse aqui é meu painel de exemplo",
              title="[yellow]Título Painel",
              subtitle="[green]Subtítulo Painel", 
              width=40)
print(caixa)


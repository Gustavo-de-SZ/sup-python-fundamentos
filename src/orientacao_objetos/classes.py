from datetime import date
from rich.console import Console
from rich.table import Table


class Endereco: 
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []

class Jogo: 
    def __init__(self):
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificao: str = None



gta_vi = Jogo()
gta_vi.titulo = "gta vi"
gta_vi.data_lancamento = date(2077, 2, 28 )
gta_vi.preco: float = 650
gta_vi.genero = "Ação"
gta_vi.classificao = "M"

the_witcher = Jogo()
the_witcher.titulo = "the witcher 4"
the_witcher.data_lancamento = date(2077, 12, 25)
the_witcher.preco:float = 500
the_witcher.genero = "rpg"
the_witcher.classificao = "m"

league_of_legends = Jogo()
league_of_legends.titulo = "LOL"
league_of_legends.data_lancamento = date(2009, 10, 10)
league_of_legends.preco: float = 0
league_of_legends.genero = "moba"
league_of_legends.classificao = "12"


colunas = ["titulo", "data lancamento", "preco", "genero", "classificao"]

tabela = Table(*colunas)

tabela.add_row(
    gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificao
)
tabela.add_row(
    the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificao
)
tabela.add_row(
    league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificao
)

console = Console()
console.print(tabela)
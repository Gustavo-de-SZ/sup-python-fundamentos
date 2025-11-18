
from datetime import date
from rich.table import Table
from rich.console import Console
class Cachorro:

    def __init__(self, raca_param: str, peso: float, idade: int, cor: str = "Caramelo"):
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor

        self.cidade_natal = "Blumenau"



def exemplo_construtor_cachorro():

    tobby = Cachorro ("Dobberman", 45.20, 15, "Preto")
    print("raça:", tobby.raca)
    print("peso:", tobby.peso)
    print("idade:", tobby.idade)
    print("cidade natal:", tobby.cidade_natal)
    print("cor:", tobby.cor)
    daschund = Cachorro ("Salsicha", 70.00, 5)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)




class Passagem:

    def __init__(
        self,
        destino: str,
        qtd_dias: int,
        data_inicio: date,
        qtd_pessoas: int = 2,       # DEFAULT
        partida: str = "São Paulo"  # DEFAULT
    ):
        self.destino = destino
        self.qtd_dias = qtd_dias
        self.data_inicio = data_inicio
        self.qtd_pessoas = qtd_pessoas
        self.partida = partida


def exemplo_construtor_passagem():
    passagem1 = Passagem("Rio de Janeiro", 5, date(2025, 1, 10))
    passagem2 = Passagem("Bahia", 7, date(2025, 3, 20))
    passagem3 = Passagem("Curitiba", 4, date(2025, 5, 1), 3)
    passagem4 = Passagem("Porto Alegre", 10, date(2025, 7, 15), 4, "Florianópolis")

    console = Console()
    table = Table("Destino", "Dias", "Data Início", "Qtd Pessoas", "Partida")

    for p in [passagem1, passagem2, passagem3, passagem4]:
        table.add_row(
            p.destino,
            str(p.qtd_dias),
            p.data_inicio.strftime("%d/%m/%Y"),
            str(p.qtd_pessoas),
            p.partida
        )

    console.print(table)




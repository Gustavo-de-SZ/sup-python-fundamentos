from datetime import date
from rich.console import Console
from rich.table import Table


# class Endereco: 
#     def __init__(self):
#         self.cidade: str = None
#         self.pais: str = None


# class Desenvolvedora:
#     def __init__(self):
#         self.nome: str = None
#         self.sede: Endereco = None
#         self.proprietario: str = None
#         self.jogos: List[Jogo] = []

# class Jogo: 
#     def __init__(self):
#         self.titulo: str = None
#         self.data_lancamento: date = None
#         self.preco: float = None
#         self.genero: str = None
#         self.classificao: str = None
#         self.desenvolvedora: Desenvolvedora = None

# def exemplo_01():
#     endereco_rockstar = Endereco()
#     endereco_rockstar.cidade = "New york"
#     endereco_rockstar.pais = "US"

#     rockstar_games = Desenvolvedora()
#     rockstar_games.nome = "rockstar games"
#     rockstar_games.proprietario = "take 2 int"
#     rockstar_games.sede = endereco_rockstar

#     gta_vi = Jogo()
#     gta_vi.titulo = "gta vi"
#     gta_vi.data_lancamento = date(2077, 2, 28 )
#     gta_vi.preco: float = 650
#     gta_vi.genero = "Ação"
#     gta_vi.classificao = "M"
#     gta_vi.desenvolvedora = rockstar_games

#     the_witcher = Jogo()
#     the_witcher.titulo = "the witcher 4"
#     the_witcher.data_lancamento = date(2077, 12, 25)
#     the_witcher.preco:float = 500
#     the_witcher.genero = "rpg"
#     the_witcher.classificao = "m"

#     league_of_legends = Jogo()
#     league_of_legends.titulo = "LOL"
#     league_of_legends.data_lancamento = date(2009, 10, 10)
#     league_of_legends.preco: float = 0
#     league_of_legends.genero = "moba"
#     league_of_legends.classificao = "12"

#     rockstar_games.jogos.append(gta_vi)
#     rockstar_games.jogos.append(the_witcher)
#     rockstar_games.jogos.append(league_of_legends)
#     colunas = ["desenvolvedora", "titulo", "data lancamento", "preco", "genero", "classificao"]

#     tabela = Table(*colunas)

#     tabela.add_row(
#         gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificao
#     )
#     tabela.add_row(
#         "na", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificao
#     )
#     tabela.add_row(
#     "na", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificao
#     )

#     console = Console()
#     console.print(tabela)
    
class Marca:
    def __init__(self):
        self.nome: str = None
        self.id: int = None
        self.fundador: str = None
        self.data_fundacao: date = None
        self.faturamento: float = None
        
        
def exercicio_marca():
    
    nike = Marca()
    nike.nome:str = "nike"
    nike.id:int = 1
    nike.fundador: str = "eu"
    nike.data_fundacao = date(2000, 10, 10)
    nike.faturamento:float = 100000000
    
    batatinha = Marca()
    batatinha.nome:str = "batatinha"
    batatinha.id:int = 2
    batatinha.fundador: str = "eu não"
    batatinha.data_fundacao = date(2010, 10, 10)
    batatinha.faturamento:float = 900000000
    
    console = Console()
    console.print("nome: " + nike.nome,"id: " +  str(nike.id), "fundador: " + nike.fundador, "data: " + str(nike.data_fundacao), "faturamento: " + str(nike.faturamento))
    console.print("nome: " + batatinha.nome,"id: " +  str(batatinha.id), "fundador: " + batatinha.fundador, "data: " + str(batatinha.data_fundacao), "faturamento: " + str(batatinha.faturamento))
    
    
class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.data_nascimento: date = None
        

class Ticket:
    def __init__(self):
        self.numero: float = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao: str = None
        

def exercicio_ticket():
    user1 = Usuario()
    user1.nome_completo = "joao"
    user1.data_nascimento: date = (2000, 10, 10)
    
    user2 = Usuario()
    user2.nome_completo = "gus"
    user2.data_nascimento: date = (2000,10, 10)
    
    ticket1 = Ticket()
    ticket1.numero: float = 1
    ticket1.usuario = user1
    ticket1.data_abertura = date(2025, 11, 12)
    ticket1.status: str = "em análise"
    ticket1.data_fechamento: date = ""
    ticket1.descricao: str = "sla kk"
    
    ticket2 = Ticket()
    ticket2.numero: float = 2
    ticket2.usuario = user2
    ticket2.data_abertura = date(2025,11, 2)
    ticket2.status: str = "finalizado"
    ticket2.data_fechament =  date(2025, 11, 12)
    ticket2.descricao: str = "sla kkkkkkkk"
    
    console = Console()
    console.print("numero: "+ str(ticket1.numero),"usuario: " +  ticket1.usuario.nome_completo,"data de abertura: " + str(ticket1.data_abertura),"status: " +  ticket1.status,"data de fechamento: " +  str(ticket1.data_fechamento),"descricao: " + ticket1.descricao)
    console.print("numero: "+ str(ticket2.numero),"usuario: " +  ticket2.usuario.nome_completo,"data de abertura: " + str(ticket2.data_abertura),"status: " +  ticket2.status,"data de fechamento: " +  str(ticket2.data_fechamento),"descricao: " + ticket2.descricao)
    
   

exercicio_ticket()


# def limpar_tela():
#     if sistema == "Windows"
#     os.system("cls")
#     else:
#         os.system("clear")
        
# console = Console()
# desenvolvedoras: List[Desenvolvedora] = []
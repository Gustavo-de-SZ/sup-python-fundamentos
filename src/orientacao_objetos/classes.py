from __future__ import annotations
from datetime import date
from typing import List
from rich.console import Console
from rich.table import Table
from rich.align import Align
import questionary
import os
import platform


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
        self.desenvolvedora: Desenvolvedora = None

def exemplo_01():
    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New york"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "rockstar games"
    rockstar_games.proprietario = "take 2 int"
    rockstar_games.sede = endereco_rockstar

    gta_vi = Jogo()
    gta_vi.titulo = "gta vi"
    gta_vi.data_lancamento = date(2077, 2, 28 )
    gta_vi.preco: float = 650
    gta_vi.genero = "Ação"
    gta_vi.classificao = "M"
    gta_vi.desenvolvedora = rockstar_games

    the_witcher = Jogo()
    the_witcher.titulo = "the witcher 4"
    the_witcher.data_lancamento = date(2077, 12, 25)
    the_witcher.preco: float = 500
    the_witcher.genero = "rpg"
    the_witcher.classificao = "m"

    league_of_legends = Jogo()
    league_of_legends.titulo = "LOL"
    league_of_legends.data_lancamento = date(2009, 10, 10)
    league_of_legends.preco: float = 0
    league_of_legends.genero = "moba"
    league_of_legends.classificao = "12"

    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)
    colunas = ["desenvolvedora", "titulo", "data lancamento", "preco", "genero", "classificao"]

    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificao
    )
    tabela.add_row(
        "na", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificao
    )
    tabela.add_row(
    "na", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificao
    )

    console = Console()
    console.print(tabela)
    
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
    ticket2.data_fechamento =  date(2025, 11, 12)
    ticket2.descricao: str = "sla kkkkkkkk"
    
    console = Console()
    console.print("numero: "+ str(ticket1.numero),"usuario: " +  ticket1.usuario.nome_completo,"data de abertura: " + str(ticket1.data_abertura),"status: " +  ticket1.status,"data de fechamento: " +  str(ticket1.data_fechamento),"descricao: " + ticket1.descricao)
    console.print("numero: "+ str(ticket2.numero),"usuario: " +  ticket2.usuario.nome_completo,"data de abertura: " + str(ticket2.data_abertura),"status: " +  ticket2.status,"data de fechamento: " +  str(ticket2.data_fechamento),"descricao: " + ticket2.descricao)
    
   




def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
desenvolvedoras: List[Desenvolvedora] = []

def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair":
        menu_geral = questionary.select("Escolha o sistema", choices=["Desenvolvedora", "Sair"]).ask().lower()
        limpar_tela()
        if menu_geral == "desenvolvedora":
            exemplo_crud_lista_objetos()

def exemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()
        

 
def adicionar_desenvolvedora():
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietário").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.sede.pais = questionary.text("Digite o país da sede").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    table = Table("Nome", "Proprietário", "Endereço")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )
    
    
    console.print(table)








class Dono:
    def __init__(self):
        self.nome: str = None
        self.cpf: str = None
        self.bairro: str = None
        self.rua: str = None
        self.numero: str = None  


class Animal:
    def __init__(self):
        self.raca: str = None
        self.dono: Dono = None
        self.data_nascimento: date = None
        self.peso: float = None
        self.altura: float = None
        self.sexo: str = None
        self.cor: str = None
        self.origem_raca: str = None



def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
animais: List[Animal] = []



def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair":
        menu_geral = questionary.select(
            "Escolha o sistema",
            choices=["Animal", "Sair"]
        ).ask().lower()

        limpar_tela()

        if menu_geral == "animal":
            exemplo_crud_animais()


def exemplo_crud_animais():
    menu = ""
    while menu != "sair":
        menu = questionary.select(
            "Escolha o menu",
            choices=["Adicionar", "Listar", "Sair"]
        ).ask().lower()

        limpar_tela()

        if menu == "adicionar":
            adicionar_animal()
        elif menu == "listar":
            listar_animais()


def adicionar_animal():
    console.print(Align.center("Cadastro de Animal"), style="blue")

    animal = Animal()
    animal.raca = questionary.text("Digite a raça do animal:").ask()

 
    dono = Dono()
    dono.nome = questionary.text("Digite o nome do dono:").ask()
    dono.cpf = questionary.text("Digite o CPF do dono:").ask()
    dono.bairro = questionary.text("Digite o bairro do dono:").ask()
    dono.rua = questionary.text("Digite a rua do dono:").ask()
    dono.numero = questionary.text("Digite o número da casa/apto do dono:").ask()
    animal.dono = dono

   
    ano = int(questionary.text("Ano de nascimento (ex: 2020):").ask())
    mes = int(questionary.text("Mês de nascimento (1-12):").ask())
    dia = int(questionary.text("Dia de nascimento (1-31):").ask())

    animal.data_nascimento = date(ano, mes, dia)

    animal.sexo = questionary.select(
        "Selecione o sexo do animal:",
        choices=["Macho", "Fêmea"]
    ).ask()

    animal.cor = questionary.text("Digite a cor do animal:").ask()
    animal.origem_raca = questionary.text("Digite a origem da raça do animal:").ask()

    animais.append(animal)
    animais.append(animal)
     
    console.print("Animal cadastrado com sucesso!", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()

            
            
def listar_animais():
    if len(animais) == 0:
        console.print("Nenhum animal.", style="red")
        input("Pressione ENTER...")
        limpar_tela()
        return

    table = Table(
        "Raça",
        "Data Nasc.",
        "Peso (kg)",
        "Altura (m)",
        "Sexo",
        "Cor",
        "Origem Raça",
        "Nome do Dono",
        "CPF",
        "Endereço"
    )

    for animal in animais:
        endereco = f"{animal.dono.rua}, {animal.dono.numero} - {animal.dono.bairro}"
        table.add_row(
            animal.raca,
            animal.data_nascimento.strftime("%d/%m/%Y") if animal.data_nascimento else "-",
            f"{animal.peso:.2f}",
            f"{animal.altura:.2f}" ,
            animal.sexo or "-",
            animal.cor or "-",
            animal.origem_raca or "-",
            animal.dono.nome,
            animal.dono.cpf,
            endereco
        )

    console.print(table)
    input("Pressione ENTER")
    limpar_tela()





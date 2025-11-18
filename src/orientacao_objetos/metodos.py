from typing import List
import questionary
from rich.table import Table
from rich.console import Console
import os
import platform

console = Console()

class Player: 
    def __init__(self, nick: str):
        self.nick = nick
        self.vida = 100
        self.stamina = 100


    def ataque(self, adversario: "Player"):
        print(self.nick, "atk basico", adversario.nick)
        self.stamina = self.stamina - 5
        adversario.vida = adversario.vida - 2
    
    
    def ataque_escada(self, adversario: "Player"):
        print(self.nick, "atk escada", adversario.nick)
        self.stamina = self.stamina - 2
        adversario.vida = adversario.vida - 10

    
    def ult(self, adversario1: "Player", adversario2: "Player"):
        print(self.nick, "ult", adversario1.nick, adversario2.nick)
        self.stamina = self.stamina - 25
        adversario1.vida = adversario1.vida - 30
        adversario2.vida = adversario2.vida - 15
    
def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
    
def exemplo_player():
    gustavo = Player("gustavo")
    
    lucas = Player("beneva")
    
    felipe = Player("geraldao")
    
    game_over = False
    players =[gustavo, lucas, felipe]
    indice_player_atual = 0
    
    choices = [
        questionary.Choice(gustavo.nick, gustavo),
        questionary.Choice(lucas.nick, lucas),
        questionary.Choice(felipe.nick, felipe),
        ]
    while game_over == False:
        player_atual = players[indice_player_atual]
        limpar_tela()
        
        ataque = questionary.select(
            f"{player_atual.nick} escolha seu ataque", choices=[
                "Basico", "escada", "ULT", "nenhum"
            ]
        ).ask()
        
        if ataque == "ULT":
            adversarios = questionary.checkbox(
                "escolha seus adversarios", choices=choices,
            ).ask()
            player_atual.ult(adversario1=adversarios[0], adversario2=adversarios[1])
        elif ataque == "Basico":
            adversarios = questionary.select(
                "escolha seus adversarios", choices=choices,
            ).ask()
            player_atual.ataque(adversarios)
        elif ataque == "escada":
            adversarios = questionary.select(
                "escolha seus adversarios", choices=choices,
            ).ask()
            player_atual.ataque_escada(adversarios)
        
        apresentar_dados(lucas, gustavo, felipe)
        
        for player_verificar_gamer in players:
            if player_verificar_gamer.vida <= 0:
                game_over = True
        
        
        indice_player_atual += 1
        if indice_player_atual == len(players):
            indice_player_atual = 0
            
            
def apresentar_dados(*players: List[platform]):
    tabela = Table()
    tabela.add_column("Player")
    tabela.add_column("Vida")
    tabela.add_column("Stamina")
    
    for player in players:
        tabela.add_row(player.nick, str(player.vida), str(player.stamina))
        
    console.print(tabela)
    input("Aprte enter para prixmo round")
    
exemplo_player()
from typing import Dict, List
from json import dumps, load
from pathlib import Path


def escrever_json(data: List, nome_arquivo: str):
    
    caminho = Path(nome_arquivo).resolve()
    json_string: str = dumps(data, ensure_ascii=False)
    with open(caminho, mode="w", encoding="UTF-8") as arquivo:
        arquivo.write(json_string)
        arquivo.flush()
        
        
def ler_json(nome_arquivo: str) -> list | dict:
    caminho = Path(nome_arquivo).resolve()
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        dado_deserializado = load(arquivo)
        return dado_deserializado
    

def exemplo_criar_arquivo():
    produtos = [
        {
            "nome": "abacate",
            "preco": 25.00    
        },
        {
            "nome": "banana",
            "preco": 10
        },
        {
        "nome": "uva",
        "preco": 25
        }
        
    ]
    escrever_json(produtos, "produtos.json")
    
    games = ["Minecraft", "Roblox", "CS"]
    escrever_json(games, "games.json")
    
    mine = {
        "nome": "minecraft",
        "classificacao": 18,
        "preco": 350
    }
    escrever_json(mine, "mine.json")
    
# exemplo_criar_arquivo()

# produtos = ler_json("produtos.json")
# games= ler_json("games.json")
# mine = ler_json("mine.json")

# print(produtos[2].get("nome"))
# print(games[0])
# print(mine.get("nome"))
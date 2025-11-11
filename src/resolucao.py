from typing import Dict, List
from src.arquivos import ler_json, escrever_json
from rich.console import Console
from rich.table import Table

def resolver():


    usuarios: List[dict[str, any]] = ler_json("data/usuarios.json")
    
    ativos, suspensos, inativos = [], [], []
    
    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta")
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")
        
        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")
        
        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")
        email = dados_pessoais.get("email")
        
        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontuaocao": pontuacao,
            "plano": plano
        }
        
        if status =="ativo":
            ativos.append(dados)
        elif status =="suspenso":
            suspensos.append(dados)
        else:
            inativos.append(dados)
            
    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspenso.json")
    escrever_json(inativos, "data/inativos.json")

    apresentar_tabela(ativos, "contas ativas")
    apresentar_tabela(suspensos, "contas suspensas")
    apresentar_tabela(inativos, "contas inativas")

def apresentar_tabela(dados: List[dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome")
    table.add_column("email")
    table.add_column("tipo")
    table.add_column("pontuacao")
    table.add_column("plano")
    
    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome"),
            dado.get("email"),
            dado.get("tipo"),
            dado.get("pontos"),
            dado.get("plano"),
        )
        
        console = Console()
        console.print(table)
        
# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free
# Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários
# Exercício 03
#   Percorrer a lista de usuário, armazenando no arquivo 'enderecos.json' todos os endereços dos usuários
# Ex.: ["Rua - Numero - Bairro - CEP - UF", "Rua - Numero - Bairro - CEP - UF"]
# Exercício 04:
#   Percorrer a lista de usuários agrupando os dados por estado, salvando o telefone e e-mail de cada usuário em uma lista por estado. Deve armazenar uma lista com os usuários conforme abaixo:
#   Ex.: sc.json
#       [{"email": "elisa.rocha@example.com", "telefone": "......"}]

def exercicio_1():
    usuarios: List[dict[str, any]] = ler_json("data/usuarios.json")
    
    free = []
    
    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        assinatura = usuario.get("assinatura")
        plano = assinatura.get("plano")
        
        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")
        
        dados = {
            "nome": nome,
            "plano": plano
        }
        
        if plano == "Free":
            free.append(dados)
        escrever_json(free, "data/free.json")

def exercicio_2():
     usuarios: List[dict[str, any]] = ler_json("data/usuarios.json")
     
     tags = []
     
     for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        tags = usuario.get("tags")
        
        
        dados = {
            "tags": tags
        }
        
        
        
        
     
     
        
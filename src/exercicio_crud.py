from typing import Dict, List
import questionary
import requests
from rich.console import Console
from rich.table import Table
import os
import platform


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def crud():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu principal", choices=[
            "Clientes", "Produtos", "Funcionários", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Clientes":
            menu_cliente()
        elif opcao == "Produtos":
            menu_produto()
        elif opcao == "Funcionários":
            menu_funcionario()



def menu_cliente():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu", choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        limpar_tela()
        if opcao == "Listar":
            listar_clientes()
        elif opcao == "Cadastrar":
            cadastrar_cliente()
        elif opcao == "Excluir":
            exluir_cliente()
        elif opcao == "Editar":
            editar_cliente()


def listar_clientes():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/clientes"
    response = requests.get(url)
    if response.status_code == 200:
        clientes: List[Dict[str, str | float | int]] = response.json()
        tabela = Table(title="Clientes")
        tabela.add_column("Código")
        tabela.add_column("Nome")
        tabela.add_column("Telefone")
        tabela.add_column("Crédito")

        for cliente in clientes:
            tabela.add_row(
                str(cliente.get("id")),
                cliente.get("nome") or "",
                cliente.get("telefone") or "",
                f"R$ {cliente.get('credito') or 0}"
            )
        Console().print(tabela)
    else:
        print(f"Erro ao listar clientes. Status {response.status_code}\n{response.text}")


def cadastrar_cliente():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/clientes"
    nome = questionary.text("Nome do cliente").ask().strip()
    telefone = questionary.text("Telefone").ask()
    credito = float((questionary.text("Crédito").ask() or "0").replace(",", "."))
    payload = {"nome": nome, "telefone": telefone, "credito": credito}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in (200, 201):
        print("Cliente cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar cliente\n{response.text}")


def exluir_cliente():
    listar_clientes()
    id_ = questionary.text("ID do cliente para excluir").ask()
    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/clientes/{id_}"
    response = requests.delete(url)

    if response.status_code in (200, 202, 204):
        print("Cliente excluído com sucesso!")
    elif response.status_code == 404:
        print("Cliente não encontrado.")
    else:
        print(f"Erro ao excluir cliente\n{response.text}")


def editar_cliente():
    listar_clientes()
    id_ = questionary.text("ID do cliente para editar").ask()
    nome = questionary.text("Nome do cliente").ask().strip()
    telefone = questionary.text("Telefone").ask()
    credito = float((questionary.text("Crédito").ask() or "0").replace(",", "."))
    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/clientes/{id_}"
    payload = {"nome": nome, "telefone": telefone, "credito": credito}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code in (200, 204):
        print("Cliente alterado com sucesso!")
    else:
        print(f"Erro ao editar cliente\n{response.text}")


def menu_produto():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Menu de produtos", choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        limpar_tela()
        if opcao == "Listar":
            listar_produtos()
        elif opcao == "Cadastrar":
            cadastrar_produto()
        elif opcao == "Editar":
            editar_produto()
        elif opcao == "Excluir":
            excluir_produto()


def listar_produtos():
    url = "https://api.franciscosensaulas.com/api/v1/empresa/produtos"
    response = requests.get(url)
    if response.status_code == 200:
        produtos = response.json()
        tabela = Table(title="Produtos")
        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Preço")
        tabela.add_column("Categoria")

        for p in produtos:
            tabela.add_row(
                str(p.get("id")),
                p.get("nome") or "",
                f"R$ {p.get('preco') or 0}",
                p.get("categoria") or ""
            )
        Console().print(tabela)
    else:
        print(f"Erro ao listar produtos. Status {response.status_code}\n{response.text}")


def cadastrar_produto():
    url = "https://api.franciscosensaulas.com/api/v1/empresa/produtos"
    nome = questionary.text("Nome do produto").ask().strip()
    preco = float((questionary.text("Preço").ask() or "0").replace(",", "."))
    categoria = questionary.text("Categoria").ask().strip()
    payload = {"nome": nome, "preco": preco, "categoria": categoria}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in (200, 201):
        print("Produto cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar produto\n{response.text}")


def editar_produto():
    listar_produtos()
    id_ = questionary.text("ID do produto para editar").ask()
    nome = questionary.text("Nome do produto").ask().strip()
    preco = float((questionary.text("Preço").ask() or "0").replace(",", "."))
    categoria = questionary.text("Categoria").ask().strip()
    url = f"https://api.franciscosensaulas.com/api/v1/empresa/produtos/{id_}"
    payload = {"nome": nome, "preco": preco, "categoria": categoria}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code in (200, 204):
        print("Produto alterado com sucesso!")
    else:
        print(f"Erro ao editar produto\n{response.text}")


def excluir_produto():
    listar_produtos()
    id_ = questionary.text("ID do produto para excluir").ask()
    url = f"https://api.franciscosensaulas.com/api/v1/empresa/produtos/{id_}"
    response = requests.delete(url)

    if response.status_code in (200, 202, 204):
        print("Produto excluído com sucesso!")
    elif response.status_code == 404:
        print("Produto não encontrado.")
    else:
        print(f"Erro ao excluir produto\n{response.text}")



def menu_funcionario():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Menu de funcionários", choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        limpar_tela()
        if opcao == "Listar":
            listar_funcionarios()
        elif opcao == "Cadastrar":
            cadastrar_funcionario()
        elif opcao == "Editar":
            editar_funcionario()
        elif opcao == "Excluir":
            excluir_funcionario()


def listar_funcionarios():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios"
    response = requests.get(url)
    if response.status_code == 200:
        funcionarios = response.json()
        tabela = Table(title="Funcionários")
        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Cargo")
        tabela.add_column("Salário")

        for f in funcionarios:
            tabela.add_row(
                str(f.get("id")),
                f.get("nome") or "",
                f.get("cargo") or "",
                f"R$ {f.get('salario') or 0}"
            )
        Console().print(tabela)
    else:
        print(f"Erro ao listar funcionários. Status {response.status_code}\n{response.text}")


def cadastrar_funcionario():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios"
    nome = questionary.text("Nome do funcionário").ask().strip()
    cargo = questionary.text("Cargo").ask().strip()
    salario = float((questionary.text("Salário").ask() or "0").replace(",", "."))
    payload = {"nome": nome, "cargo": cargo, "salario": salario}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in (200, 201):
        print("Funcionário cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar funcionário\n{response.text}")


def editar_funcionario():
    listar_funcionarios()
    id_ = questionary.text("ID do funcionário para editar").ask()
    nome = questionary.text("Nome do funcionário").ask().strip()
    cargo = questionary.text("Cargo").ask().strip()
    salario = float((questionary.text("Salário").ask() or "0").replace(",", "."))
    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios/{id_}"
    payload = {"nome": nome, "cargo": cargo, "salario": salario}
    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code in (200, 204):
        print("Funcionário alterado com sucesso!")
    else:
        print(f"Erro ao editar funcionário\n{response.text}")


def excluir_funcionario():
    listar_funcionarios()
    id_ = questionary.text("ID do funcionário para excluir").ask()
    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios/{id_}"
    response = requests.delete(url)

    if response.status_code in (200, 202, 204):
        print("Funcionário excluído com sucesso!")
    elif response.status_code == 404:
        print("Funcionário não encontrado.")
    else:
        print(f"Erro ao excluir funcionário\n{response.text}")





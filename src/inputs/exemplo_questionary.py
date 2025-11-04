from questionary import text, password, select, checkbox, confirm

sabores_pizza = [
    "Calabresa",
    "Mussarela",
    "Frango com Catupiry",
    "Portuguesa",
    "Quatro Queijos",
    "Marguerita",
    "Pepperoni",
    "Bacon",
    "Napolitana",
    "Vegetariana"
]


def __solicitar_text() -> str:
    cliente = text("digite o nome do cliente").ask()
    return cliente


def __solicitar_senha() -> str:
    senha = password("digite a senha").ask()
    return senha


def __escolher_opcao() -> str:
    opcoes = ["Pequena", "Media", "Grande"]
    opcao_escolhida = select("escolha o tamanho da pizza", choices=opcoes).ask()
    return opcao_escolhida


def __escolher_sabores(tamanho: str) -> list:
    quantidade_maxima_sabores =1 
    if tamanho == "Média":
        quantidade_maxima_sabores = 2
    elif tamanho == "Grande":
        quantidade_maxima_sabores = 4
    
    
    sabores = checkbox(
        "Escolha os sabores",
        choices=sabores_pizza,
        validate=lambda elementos: __validar_quantidade_sabores(elementos, quantidade_maxima_sabores)).ask()
    
    return sabores


def __validar_quantidade_sabores(elementos: list[str], quantidade_maxima: int) -> bool| str:
    if len(elementos) == 0:
        return "no minimo 1"
    if len (elementos) > quantidade_maxima:
        return f"no maximo {quantidade_maxima}"
    return True


def __solicitar_confirmacao() -> bool:
    confirmado = confirm("voce confirma o pedido").ask()
    return confirmado

def exemplos():
    cliente = __solicitar_text()
    senha = __solicitar_senha()
    if cliente == "proway.com" and senha == "Batatinha":
        tamanho = __escolher_opcao()
        sabores = __escolher_sabores(tamanho)
        pedido_confirmado = __solicitar_confirmacao()
        
        if pedido_confirmado == True:
            print("confirmado")
        else:
            print("cancelado")

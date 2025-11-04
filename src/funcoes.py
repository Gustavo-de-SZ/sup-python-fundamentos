def funcao_sem_retorno():
    print("Olá mundo")


def funcao_com_retorno() -> str:
    produto: str = "iPhone 17 Pro Max"
    return produto


def funcao_executar():
    funcao_sem_retorno()
    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)


# ---------------------- Funções de Pedido ----------------------

def solicitar_nome_jogo() -> str:
    nome: str = input("Digite o nome do jogo: ").strip()
    return nome


def solicitar_preco_jogo() -> float:
    preco: float = float(input("Digite o preço: ").replace(",", "."))
    return preco


def solicitar_quantidade_jogo() -> int:
    quantidade: int = int(input("Digite a quantidade: "))
    return quantidade


def solicitar_pedido_fechado() -> bool:
    pedido_fechado: str = input("Pedido fechado (s/n): ").strip().lower()
    return pedido_fechado == "s"


def solicitar_valor_pagamento() -> float:
    valor_pagamento: float = float(input("Digite o valor pago: ").replace(",", "."))
    return valor_pagamento


def processar_pedido():
    nome: str = solicitar_nome_jogo()
    preco: float = solicitar_preco_jogo()
    quantidade: int = solicitar_quantidade_jogo()
    pedido_fechado: bool = solicitar_pedido_fechado()

    valor_pedido: float = quantidade * preco
    print(f"\nValor total do pedido ({nome}): R$ {valor_pedido:.2f}")

    if pedido_fechado:
        valor_pagamento = solicitar_valor_pagamento()
        if valor_pagamento > valor_pedido:
            valor_troco = valor_pagamento - valor_pedido
            print(f"Troco: R$ {valor_troco:.2f}")
            print("Status: Pedido realizado")
        elif valor_pagamento == valor_pedido:
            print("Pedido sem troco")
            print("Status: Pedido realizado")
        else:
            valor_faltante = valor_pedido - valor_pagamento
            print(f"Valor faltante: R$ {valor_faltante:.2f}")
            print("Status: Pedido cancelado")


# ---------------------- Compra no Paraguai ----------------------

def solicitar_cotacao_dolar() -> float:
    cotacao: float = float(input("Digite a cotação do dólar hoje: ").replace(",", "."))
    return cotacao


def solicitar_nome_produto() -> str:
    nome: str = input("Digite o nome do produto: ")
    return nome


def solicitar_valor_produto_dolar() -> float:
    valor_produto: float = float(input("Digite o valor do produto em dólar: ").replace(",", "."))
    return valor_produto


def solicitar_se_pagara_imposto() -> bool:
    pagara_imposto: str = input("Você pagará imposto? [s/n]: ").lower().strip()
    return pagara_imposto == "s"


def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    cota_mensal: str = input("Você utilizará a cota mensal? [s/n]: ").lower().strip()
    return cota_mensal == "s"


def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float,
):
    cota_mensal = 500.00
    valor_imposto_dolar = (valor_produto_dolar - cota_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"Valor total do produto com imposto (usando cota): R$ {valor_total_produto_reais:.2f}")


def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float,
):
    valor_imposto_dolar = valor_produto_dolar / 2  # 50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""
Valor total do produto: $ {valor_produto_dolar:.2f}
Valor em reais (sem imposto): R$ {valor_produto_reais:.2f}
Valor do imposto: R$ {valor_imposto_reais:.2f}
Valor total com imposto: R$ {valor_total_produto_reais:.2f}
""")


def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar()
    nome_produto: str = solicitar_nome_produto()
    valor_produto_dolar: float = solicitar_valor_produto_dolar()
    pagara_imposto: bool = solicitar_se_pagara_imposto()

    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    if pagara_imposto:
        utilizar_cota = solicitar_deseja_utilizar_cota_dolar_mensal()
        if utilizar_cota:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais
            )
    else:
        print(f"Valor do produto sem pagar imposto: R$ {valor_produto_reais:.2f}")


# ---------------------- Exercício do Aluno ----------------------

def solicitar_nome_aluno() -> str:
    return input("Digite o nome do aluno: ")


def solicitar_primeira_nota() -> float:
    return float(input("Digite a primeira nota do aluno: ").replace(",", "."))


def solicitar_segunda_nota() -> float:
    return float(input("Digite a segunda nota do aluno: ").replace(",", "."))


def solicitar_terceira_nota() -> float:
    return float(input("Digite a terceira nota do aluno: ").replace(",", "."))


def calcular_media_aluno(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3) / 3


def verificar_se_aluno_passou(media: float) -> bool:
    return media >= 7


def solicitar_idade_aluno() -> int:
    return int(input("Digite a idade do aluno: "))


def solicitar_peso_aluno() -> float:
    return float(input("Digite o peso do aluno (kg): ").replace(",", "."))


def solicitar_altura_aluno() -> float:
    return float(input("Digite a altura do aluno (m): ").replace(",", "."))


def calcular_imc_aluno(peso: float, altura: float) -> float:
    return peso / (altura ** 2)


def verificar_status_imc_aluno(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 39.9:
        return "Obesidade"
    else:
        return "Obesidade grave"


def validar_geracao_aluno(idade: int) -> str:
    ano_atual = 2025
    ano_nascimento = ano_atual - idade

    if 1946 <= ano_nascimento <= 1964:
        return "Geração Baby Boomer"
    elif 1965 <= ano_nascimento <= 1980:
        return "Geração X"
    elif 1981 <= ano_nascimento <= 1996:
        return "Geração Y (Millennial)"
    else:
        return "Geração Z"
    


def solicitar_cargo_aluno() -> str:
    cargo = input("Qual o cargo do aluno? [Estagiário / Junior / Pleno / Senior]: ").lower().strip()
    while cargo not in ["estagiário", "junior", "pleno", "senior"]:
        cargo = input("Cargo inválido. Escolha entre [Estagiário / Junior / Pleno / Senior]: ").lower().strip()
    return cargo


def validar_salario_aluno_atraves_do_cargo(cargo: str) -> float:
    if cargo == "estagiário":
        return 850.00
    elif cargo == "junior":
        return 1800.00
    elif cargo == "pleno":
        return 4000.00
    else:
        return 6000.00


def solicitar_dados_aluno():
    nome = solicitar_nome_aluno()
    n1 = solicitar_primeira_nota()
    n2 = solicitar_segunda_nota()
    n3 = solicitar_terceira_nota()
    media = calcular_media_aluno(n1, n2, n3)
    aprovado = verificar_se_aluno_passou(media)
    idade = solicitar_idade_aluno()
    geracao = validar_geracao_aluno(idade)
    peso = solicitar_peso_aluno()
    altura = solicitar_altura_aluno()
    imc = calcular_imc_aluno(peso, altura)
    status_imc = verificar_status_imc_aluno(imc)
    cargo = solicitar_cargo_aluno()
    salario = validar_salario_aluno_atraves_do_cargo(cargo)

    print(f"""
--- DADOS DO ALUNO ---
Nome: {nome}
Média final: {media:.2f} -> {'Aprovado' if aprovado else 'Reprovado'}
Idade: {idade} anos ({geracao})
IMC: {imc:.2f} -> {status_imc}
Cargo: {cargo.capitalize()} -> Salário: R$ {salario:.2f}
""")




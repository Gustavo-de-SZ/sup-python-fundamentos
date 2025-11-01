

def solicitar_cotacao_dolar() -> float:
    cotaocao: float = float(input("digite valor cotacao atual").replace(",", "."))
    return cotaocao


def solicitar_nome_produto() -> str:
    nome: str = input("digite nome produto")
    return nome


def solicitar_valor_produto_dolar() -> float:
    valor_dolar:float = float(input("digite valor em dolar"))
    return valor_dolar


def solicitar_se_pagara_imposto() -> bool:
    pagar_imposto = input(" pagar impost?")
    if pagar_imposto == "s":
        return True
    else: 
        return False



def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    cota_mensal = input("deseja utilizar cota mensal?")
    if cota_mensal == "s":
        return True
    else: 
        return False

def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
        valor_produto_dolar: float,
        cotacao_dolar: float,
        valor_produto_reais: float,
):
    cotacao_mensal = 500
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""valor total do produto: $ " {valor_produto_dolar}
valor total do produto: R$ {valor_produto_reais}
valor imposto: R$ {valor_imposto_reais}

valor total com imposto: R$ {valor_total_produto_reais} """)


def calcular_valor_produto_acrescentando_imposto(
        valor_produto_dolar: float,
          cotacao_dolar: float,
        valor_produto_reais: float,
):
    valor_imposto_dolar = valor_produto_dolar / 2 
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar
    
    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("valor total com imposto" + str(valor_total_produto_reais))


def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar()
    nome_produto: str =solicitar_nome_produto()
    valor_produto_dolar : float = solicitar_valor_produto_dolar()
    pagara_imposto :bool = solicitar_se_pagara_imposto()
    valor_produto_reais = valor_produto_dolar * cotacao_dolar
    if pagara_imposto == True:
       utilizar_cota_dolar_mensal = solicitar_deseja_utilizar_cota_dolar_mensal()

       if utilizar_cota_dolar_mensal == True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
               valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
       else:
            calcular_valor_produto_acrescentando_imposto(
               valor_produto_dolar, cotacao_dolar, valor_produto_reais,
               )
    else:
        print("valor produto sem pagar" + str(valor_produto_reais))



def exercicio_aluno():
    solicitar_nome_aluno()
    solicitar_nota_1()
    solicitar_nota_2()
    solicitar_nota_3()
    calcular_media_e_apresentar()
    verificar_aprovacao_aluno()

def solicitar_nome_aluno() -> str:
    nome = str(input("digite o nome"))
    return nome

def solicitar_nota_1() -> float:
    nota_1:float = float(input("digite nota 1"))
    return nota_1


def solicitar_nota_2() -> float:
    nota_2:float = float(input("digite nota 2"))
    return nota_2


def solicitar_nota_3() -> float:
    nota_3:float = float(input("digite nota 3"))
    return nota_3


def calcular_media_e_apresentar():
    nota_1: float = solicitar_nota_1()
    nota_2: float = solicitar_nota_2()
    nota_3: float = solicitar_nota_3()
    media_notas: float = (nota_1 + nota_2 + nota_3) /3
    
    print("media" + str(media_notas))
    return media_notas


def verificar_aprovacao_aluno():
    media_final = calcular_media_e_apresentar()
    if media_final > 7:
        print("aprovado")
    else:
        print("reprovado")


def solicitar_idade() -> int:
    idade: int = int(input("idade"))
    return idade


def solicitar_peso() -> float:
    peso: float = float(input("peso"))
    return peso


def solicitar_altura() -> float:
    altura: float = float(input("altura"))
    return altura


# def calcular_imc() -> float:


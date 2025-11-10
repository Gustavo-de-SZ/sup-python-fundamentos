# from questionary import text, password, select, checkbox, confirm
# import datetime

# def exercicios_dados_produto():
#     nome_produto = input("Nome do produto: ")
#     quantidade_produto = int(input("Quantidade do produto: "))
#     preco_produto = float(input("Preço do produto: "))
#     valor_total_compra: float = quantidade_produto * preco_produto
#     categorias_produto = ["Esportes","Roupas Esportivas","Calçados","Acessórios","Equipamentos","Suplementos e Nutrição","Marcas","Ofertas"]
#     categoria_escolhida = select("escolha a categoria", choices=categorias_produto).ask()
#     desconto = 0
#     if categoria_escolhida == "Esportes":
#         desconto = desconto + 0.1
#     if categoria_escolhida == "Roupas Esportivas":
#         desconto = desconto + 0.15
#     if categoria_escolhida == "Calçados":
#         desconto = desconto + 0.2
#     if categoria_escolhida == "Acessórios":
#         desconto = desconto + 0.12
#     if categoria_escolhida == "Equipamentos":
#         desconto = desconto + 0.08
#     if categoria_escolhida == "Suplementos e Nutrição":
#         desconto = desconto +  0.05
#     if categoria_escolhida == "Marcas":
#         desconto =  desconto + 0.07
#     if categoria_escolhida == "Ofertas":
#         desconto = desconto + 0.25

    
#     data_vencimento_produto : str = text("Digite a data de vencimento do produto no formato: dd-mm-aaaa").ask()

#     data_vencimento_formatada = datetime.datetime.strptime(data_vencimento_produto, '%d-%m-%Y').date().strftime('%d-%m-%Y')

#     dia_vencimento = data_vencimento_formatada.split("-")[0]

#     mes_vencimento = data_vencimento_formatada.split("-")[1]

#     ano_vencimento = data_vencimento_formatada.split("-")[2]

#     data_atual = datetime.datetime.now().strftime('%d-%m-%Y')

#     dia_atual = data_atual.split("-")[0]

#     mes_atual = data_atual.split("-")[1]

#     ano_atual = data_atual.split("-")[2]

#     if mes_vencimento < mes_atual or ano_vencimento < ano_atual:
#         print(f"""🛑Produto vencido! Compra não permitida.""")
#         return print
    
    
    
#     regiões: list = ["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"]
#     regiao_escolhida = select("escolha a categoria", choices=regiões).ask()
#     frete: int = 0
#     if regiao_escolhida == "Sul":
#         frete = frete + 25
#     if regiao_escolhida == "Sudeste":
#         frete = frete + 35
#     if regiao_escolhida == "Centro-Oeste":
#         frete = frete + 45
#     if regiao_escolhida == "Norte":
#         frete = frete + 55 
#     if regiao_escolhida == "Nordeste":
#         frete = frete + 50
    
    
    
#     cupom_desconto: list = ["Sem cupom", "SUPER-10", "FRETEGRATIS", "PRIME20", "CLIENTEVIP"]
#     cupom_desconto_escolhido = select("Possui cupom? se sim, qual?", choices=cupom_desconto).ask()
#     desconto_cupom: float = 0
#     if cupom_desconto_escolhido == "SUPER-10":
#         desconto_cupom = desconto_cupom + 0.1
#     if cupom_desconto_escolhido == "FRETEGRATIS":
#         frete = 0
#     if cupom_desconto_escolhido == "PRIME20":
#         desconto_cupom = desconto_cupom + 0.2
#     if cupom_desconto_escolhido == "CLIENTEVIP":
#         desconto_cupom = desconto_cupom + 0.25
#     if cupom_desconto_escolhido == "Sem cupom":
#         desconto_cupom = desconto_cupom + 0
    
#     valor_compra: float = (quantidade_produto * preco_produto)    
#     valor_com_desconto: float = (quantidade_produto * preco_produto) * (1 - desconto)
#     valor_do_desconto: float = valor_compra - valor_com_desconto
#     valor_pre_frete: float = (valor_com_desconto * (1 - desconto_cupom))
    
    
    
#     if valor_pre_frete > 500:
#         frete = frete + 0
#     valor_total: float = valor_pre_frete + frete 
    
#     print(f"""Dados do produto: {nome_produto}
# Quantidade: {quantidade_produto}
# Preço: R${preco_produto:.2f}
# Categoria: {categoria_escolhida}
# Desconto: {desconto}
# Valor do desconto:{valor_do_desconto}
# Frete: R$ {frete}
# ------------------------
# Total: R${valor_total:.2f}
# Região: {regiao_escolhida}
# ------------------------
# Obrigado por comprar conosco
# """)
    
    
# gostaria_salvar_pedido_txt = confirm("Gostaria de salvar o pedido?").ask()

# if gostaria_salvar_pedido_txt == True:
#     caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")

#     nome_arquivo = "resumo_pedido.txt"

#     caminho_desktop_com_arquivo = os.path.join(caminho_desktop, nome_arquivo)

#     with open(caminho_desktop_com_arquivo, "w", encoding="utf-8") as resumo:
#             resumo.write(pedido_produto)

#         print("Pedido salvo com sucesso no seu Desktop! Obrigado por usar nosso sistema!")
#     else:
#         print("O pedido não foi salvo. Obrigado por usar o nosso sistema!")           

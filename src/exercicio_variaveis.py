from questionary import text, password, select, checkbox, confirm
import datetime

def exercicios_dados_produto():
    nome_produto = input("Nome do produto: ")
    quantidade_produto = int(input("Quantidade do produto: "))
    preco_produto = float(input("Preço do produto: "))
    valor_total_compra: float = quantidade_produto * preco_produto
    categorias_produto = ["Esportes","Roupas Esportivas","Calçados","Acessórios","Equipamentos","Suplementos e Nutrição","Marcas","Ofertas"]
    categoria_escolhida = select("escolha a categoria", choices=categorias_produto).ask()
    desconto = 0
    if categoria_escolhida == "Esportes":
        desconto = desconto + 0.1
    if categoria_escolhida == "Roupas Esportivas":
        desconto = desconto + 0.15
    if categoria_escolhida == "Calçados":
        desconto = desconto + 0.2
    if categoria_escolhida == "Acessórios":
        desconto = desconto + 0.12
    if categoria_escolhida == "Equipamentos":
        desconto = desconto + 0.08
    if categoria_escolhida == "Suplementos e Nutrição":
        desconto = desconto +  0.05
    if categoria_escolhida == "Marcas":
        desconto =  desconto + 0.07
    if categoria_escolhida == "Ofertas":
        desconto = desconto + 0.25

    
    # data_vencimento = str(input("data de vencimento"))
    
    
    
    regiões: list = ["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"]
    regiao_escolhida = select("escolha a categoria", choices=regiões).ask()
    frete: int = 0
    if regiao_escolhida == "Sul":
        frete = frete + 25
    if regiao_escolhida == "Sudeste":
        frete = frete + 35
    if regiao_escolhida == "Centro-Oeste":
        frete = frete + 45
    if regiao_escolhida == "Norte":
        frete = frete + 55 
    if regiao_escolhida == "Nordeste":
        frete = frete + 50
    
    
    
    cupom_desconto: list = ["Sem cupom", "SUPER-10", "FRETEGRATIS", "PRIME20", "CLIENTEVIP"]
    cupom_desconto_escolhido = select("Possui cupom? se sim, qual?", choices=cupom_desconto).ask()
    desconto_cupom: float = 0
    if cupom_desconto_escolhido == "SUPER-10":
        desconto_cupom = desconto_cupom + 0.1
    if cupom_desconto_escolhido == "FRETEGRATIS":
        frete = 0
    if cupom_desconto_escolhido == "PRIME20":
        desconto_cupom = desconto_cupom + 0.2
    if cupom_desconto_escolhido == "CLIENTEVIP":
        desconto_cupom = desconto_cupom + 0.25
    if cupom_desconto_escolhido == "Sem cupom":
        desconto_cupom = desconto_cupom + 0
    
    valor_compra: float = (quantidade_produto * preco_produto)    
    valor_com_desconto: float = (quantidade_produto * preco_produto) * (1 - desconto)
    valor_do_desconto: float = valor_compra - valor_com_desconto
    valor_pre_frete: float = (valor_com_desconto * (1 - desconto_cupom))
    
    
    
    if valor_pre_frete > 500:
        frete = frete + 0
    valor_total: float = valor_pre_frete + frete 
    
    print(f"""Dados do produto: {nome_produto}
Quantidade: {quantidade_produto}
Preço: R${preco_produto:.2f}
Categoria: {categoria_escolhida}
Desconto: {desconto}
Valor do desconto:{valor_do_desconto}
Frete: R$ {frete}
------------------------
Total: R${valor_total:.2f}
Região: {regiao_escolhida}
------------------------
Obrigado por comprar conosco
""")
    
    

        

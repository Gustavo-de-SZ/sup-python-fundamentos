from typing import Dict, Union


def exemplo_dicionario_basico():
    # Dicionário é uma forma de armazenar chaves e valores
    # Cada chave está atrelado a um valor

    # Dicionário terá uma chave do tipo string
    # Pode armazenar string, int ou bool
    # Criamos um dicionário com 2 chaves (apelido, idade)
    cachorro: Dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True,
        "peso": 22.5
    }

    # Acrescentar uma nova chave com um valor
    cachorro["raca"] = "Pastor Alemão"

    cachorro["cor"] = "Caramelo"
    # alterar o valor de uma chave existente
    cachorro["idade"] = 5
    
    # remover uma chave do dicionário
    cachorro.pop("abandonado")
    
    # print("cachorro"", cachorro["apelido"])
    print(f"""
Cachorro: {cachorro.get("apelido")}
Raça: {cachorro.get("raca")}
Idade: {cachorro.get("idade")}
Cor: {cachorro.get("cor")}
Abandonado: {cachorro.get("abandonado")}
Peso: {cachorro.get("peso")})
""")
    



def exemplo_dicionario_aluno():
    # Dicionário é uma forma de armazenar chaves e valores
    # Cada chave está atrelada a um valor

    # Criar um dicionário chamado aluno com os seguintes dados
    aluno: Dict[str, Union[str, int, bool]] = {
        "nome_completo": "Gustavo Silva",
        "nome_mae": "Mariana Silva",
        "nome_pai": "João Silva",
        "jogar": True
    }

    # Apresentar os dados iniciais
    print(">>> Dados iniciais do aluno:")
    print(aluno)

    # Adicionar a chave 'idade' ao dicionário
    aluno["idade"] = 17

    # Apresentar a idade do aluno
    print(f"\nIdade do aluno: {aluno.get('idade')} anos")

    # Alterar a idade do aluno para +1
    aluno["idade"] += 1

    # Remover a chave 'jogar' do dicionário
    aluno.pop("jogar")

    # Apresentar os dados finais formatados
    print(f"""
==============================
Nome completo: {aluno.get("nome_completo")}
Nome da mãe:  {aluno.get("nome_mae")}
Nome do pai:  {aluno.get("nome_pai")}
Idade:        {aluno.get("idade")}
Jogar:        {aluno.get("jogar")}
==============================
""")




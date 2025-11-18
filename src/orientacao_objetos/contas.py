import questionary

class Conta:
    def __init__(self, titular: str, saldo_inicial: float):
        """construtor da classe. inicializa o titular e o saldo"""
        self.titular = titular
        self.saldo = saldo_inicial
        
    
    def depositar(self, valor_deposito: float):
        """Adiciona um valor ao saldo da conta"""
        if valor_deposito <= 0:
            print(f"deposito: valor de deposito invalido{valor_deposito:.2f}")
            return
        self.saldo = self.saldo + valor_deposito    
        
    def sacar(self, valor_saque: float):
        """remove um valor da conta"""
        if valor_saque > self.saldo:
            print(f"saque saçdo insuficiente{valor_saque:.2f}")
        else: 
            self.saldo = self.saldo - valor_saque
            print(f"saque de {valor_saque:.2f}")
    
    def exibir_saldo(self):
        """mostra valor saldo"""
        print(f"extrate saldo atual {self.saldo:.2f}")


def exemplo_conta():
    """metodo para testar a funcionalidade da conta"""
    conta_bradesco = Conta("vitor", 3900.22)
    
    conta_bradesco.exibir_saldo()
    conta_bradesco.sacar(800)
    
    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78)
    conta_bradesco.exibir_saldo()



class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []
    
    def adicionar(self, nota: float):
        self.nota = self.notas.append(nota)
        
        
    def apresentar_notas(self):
        print(self.notas)
        
    def calcular_media_notas(self, nota:float, notas:list, media_nota: float):
        for nota in notas:
            

def exemplo_aluno():
    aluno1 = Aluno("gustavo")
    
    aluno1.adicionar(10)
    aluno1.adicionar(8)
    aluno1.adicionar(9)
    
    aluno1.apresentar_notas()
    
exemplo_aluno()
from enum import Enum


class MarcaEnum(Enum):
    SONY = "Sony"
    MICROSOFT = "Microsoft"
    


class Console:
    def __init__(self):
        self.marca: MarcaEnum
        self.modelo: str = ""



def exemplo_consoles():
    play_station = Console()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "ps1"
    
    xbox = Console()
    xbox.marca = MarcaEnum.MICROSOFT
    

class PessoaTipo(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"


class Pessoa:
    def __init__(self):
        self.nome: str
        self.cpf_cnpj: str
        self.tipo: PessoaTipo
        
def exemplo_pessoas():
    cleber = Pessoa()
    cleber.nome = "osvaldo"
    cleber.tipo = PessoaTipo.JURIDICA
    cleber.cpf_cnpj = "01.000.000/0001-00"
    
    print(
        "pessoa",
        cleber.nome,
        "tipo",
        cleber.tipo.value
    )
    
    
 
    

class NomePersonagem(Enum):
    BATMAN = "Batman"
    SUPERMMAN = "Superman"
    BUZZLIGHTYEAR = "Buzz lightyear"
    HOMEMFORMIGA = "Homem formiga"
    BOBESPONJA = "Bob esponja"
    CATDOG = "Catdog"


class StatusJob(Enum):
    PENDENTE = "Pendente"
    EMANDAMENTO = "Em andamento"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"


class Job():
    def __init__(self):
        self.personagem: NomePersonagem
        self.valor: float 
        self.local: str 
        self.status: StatusJob

def exemplo_job():

    batman = Job()
    batman.personagem = NomePersonagem.BATMAN
    batman.status = StatusJob.CANCELADO
    batman.valor = 2302.20
    batman.local = "blu"

    bob_esponja = Job()
    bob_esponja.personagem = NomePersonagem.BOBESPONJA
    bob_esponja.status = StatusJob.FINALIZADO
    bob_esponja.valor = 20303
    bob_esponja.local = "gaspar"
    
    print(
        "herois",
        batman.personagem.value,
        bob_esponja.personagem.value,
        "status",
        batman.status.value,
        bob_esponja.status.value,
    )
if __name__ == "__main__":
    exemplo_job()  
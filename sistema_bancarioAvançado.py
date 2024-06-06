from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self,endereco): #Passando endereço como argumento
        self.endereço = endereco #Criando o endereço na classe Cliente
        self.contas = [] #Criando o atributo conta, sem iniciar ele no construtor (Por que eu não preciso referenciar contas no init?)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    #adiciona a conta recebida como parâmetro para a lista contas
    def adiciona_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) #Chamando o construtor da classe pai 
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._hisorico = Historico()

    @classmethod
    def nova_cona(cls, cliente, numero):
        return cls(numero, cliente)

    #Mapeando metodos para acessar as propriedade sporque são atributos privados
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente. ")

        elif valor > 0:
            self.saldo -= valor
            print("\n Saque realizado com sucesso!")
            return True
        else:
            print("\n Operação falhou! O valor informado é invalido!")
        
        return False
    
    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n Depósito realizado com sucesso!")
        
        else:
            print("\n Operação fahou! O valor informado é inválido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """    
   
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao._class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def valor(self):
        return self._valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)
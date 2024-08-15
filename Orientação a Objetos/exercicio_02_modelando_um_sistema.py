'''
modele um sistema orientado a objetos que represente contas correntes do Banco Delas seguindo os seguintes requisitos:
cada conta corrente pode ter um ou mais clientes como titular.
o banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
a conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
quando a clientefizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam sua conta com valor negativo até renda_mensal.
clientes homens por enquanto não tem direito a cheque especial.
para modelar o sistema, utilize obrigatóriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
'''
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def renda_mensal(self):
        return self._renda_mensal


class ContaCorrente(ABC):
    def __init__(self, numero, clientes, saldo_inicial=0):
        self._numero = numero
        self._clientes = clientes
        self._saldo = saldo_inicial
        self._operacoes = []

    @property
    def numero(self):
        return self._numero

    @property
    def clientes(self):
        return self._clientes

    @property
    def saldo(self):
        return self._saldo

    @property
    def operacoes(self):
        return self._operacoes

    @abstractmethod
    def tem_cheque_especial(self):
        pass

    def sacar(self, valor):
        limite = self.saldo
        if self.tem_cheque_especial():
            limite += self.clientes[0].renda_mensal 

        if valor <= limite:
            self._saldo -= valor
            self.operacoes.append(("saque", valor))
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self._saldo += valor
        self.operacoes.append(("deposito", valor))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")


class ContaCorrenteMulher(ContaCorrente):
    def tem_cheque_especial(self):
        return self.clientes[0].renda_mensal > 0


class ContaCorrenteHomem(ContaCorrente):
    def tem_cheque_especial(self):
        return False
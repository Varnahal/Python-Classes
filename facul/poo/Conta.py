from datetime import date
from Extrato import Extrato
class Conta:
    def __init__(self,id, nome, cpf, saldo):
        self.__id = id
        self.__name = nome
        self.__cpf = cpf
        self.__balance = saldo
        self.__transacao = Extrato(id)
    
    def showBalance(self):
        return self.__balance

    def withdraw(self, value):
        if self.__balance < value:
            return False
        else:
            self.__balance -= value
            self.__transacao.addTransacao(f"Ocorreu um saque no valor de: {value} na data: {date.today()}")
            return True
        
    def deposit(self, value):
        self.__balance += value
        self.__transacao.addTransacao(f"Ocorreu um deposito no valor de: {value} na data: {date.today()}")

    def transf(self, destinationaccount, value):
        if self.__balance < value:
            return False
        else:
            destinationaccount.deposit(value)
            self.__balance -= value
            self.__transacao.addTransacao(f"Ocorreu uma transferência no valor de: {value} para a conta de: {destinationaccount.__name} na data: {date.today()}")
            return True
        
    def extrato(self):
        self.__transacao.mostrarExtrato()


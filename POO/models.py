class Conta(object):
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        self.__saldo -= valor
        print(f"Sacado {valor} da conta {self.numero}. Saldo: {self.__saldo}")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depositado {valor} na conta {self.numero}. Saldo: {self.__saldo}")
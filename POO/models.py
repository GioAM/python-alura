class Conta(object):
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def sacar(self, valor):
        self.__saldo -= valor
        print(f"Sacado {valor} da conta {self.numero}. Saldo: {self.__saldo}")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depositado {valor} na conta {self.numero}. Saldo: {self.__saldo}")

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


class Cliente:

   def __init__(self, nome):
       self.__nome = nome

   @property
   def nome(self):
       print("chamando @property nome()")
       return self .__nome.title()

   @nome.setter
   def nome(self, nome):
       print("chamando setter nome()")
       self.__nome = nome
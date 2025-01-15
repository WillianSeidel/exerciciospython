#proteção de acesso aos dados de um objeto
class conta:
    def __init__(self, n_agencia, saldo = 0):
        self._saldo = saldo
        self.n_agencia = n_agencia
    def depositar (self, valor):
        self._saldo += valor
    def sacar (self, valor):
        self._saldo -= valor


    def mostrar_saldo(self):
        return self._saldo

conta = conta("2001", 100)
conta.depositar(100)
print(conta.n_agencia)
print(conta.mostrar_saldo())
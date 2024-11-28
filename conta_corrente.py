from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, banco, agencia, saldo, data_saldo, limite_credito=0):
        super().__init__(numero, cliente, banco, agencia, saldo, data_saldo, limite_credito)

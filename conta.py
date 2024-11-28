class Conta:
    def __init__(self, numero, cliente, banco, agencia, saldo, data_saldo, limite_credito=0):
        self.numero = numero
        self.cliente = cliente
        self.banco = banco
        self.agencia = agencia
        self.saldo = saldo
        self.data_saldo = data_saldo
        self.limite_credito = limite_credito

    def atualizar_saldo(self, valor):
        self.saldo += valor
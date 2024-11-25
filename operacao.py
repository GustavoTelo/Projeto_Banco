class Operacao:
    ENTRADA = 'entrada'
    SAIDA = 'saida'

    def __init__(self, cliente, banco, agencia, data_movi, tipo_operacao, valor):
        self.cliente = cliente
        self.banco = banco
        self.agencia = agencia
        self.data_movi = data_movi
        self.tipo_operacao = tipo_operacao
        self.valor = valor

    def executar_operacao(self):
        conta = next((c for c in self.cliente.contas if c.banco == self.banco and c.agencia == self.agencia), None)
        if conta:
            if self.tipo_operacao == self.ENTRADA:
                conta.atualizar_saldo(self.valor)
                print(f"Depósito de {self.valor} realizado. Novo saldo: R${conta.saldo}")
            elif self.tipo_operacao == self.SAIDA:
                if conta.saldo + conta.limite_credito >= self.valor:
                    conta.atualizar_saldo(-self.valor)
                    print(f"Saque de {self.valor} realizado. Novo saldo: R${conta.saldo}")
                else:
                    print("Saldo insuficiente para realizar o saque.")
        else:
            print("Conta não encontrada.")

class Agencia:
    def __init__(self, codigo, nome, banco):
        self.codigo = codigo
        self.nome = nome
        self.banco = banco
        self.contas = []


    def adicionar_conta(self, conta):
        self.contas.append(conta)
        

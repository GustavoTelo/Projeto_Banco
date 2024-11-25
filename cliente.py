class Cliente:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome  
        self.contas = []

    def adicionar_conta(self, conta):  # Corrigir aqui
        self.contas.append(conta)

class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.agencias = []

    def adicionar_agencia(self, agencia):
        self.agencias.append(agencia)


    
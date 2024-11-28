import os
from cliente import Cliente
from banco import Banco
from agencia import Agencia
from conta_corrente import ContaCorrente
from operacao import Operacao


def menu():
    print("----------MENU PRINCIPAL!----------")
    print("1. Criar Bancos")
    print("2. Criar Agência")
    print("3. Criar Cliente")
    print("4. Criar Conta Corrente")
    print("5. Operações")
    print("6. Listar Extrato")
    print("7. Sair")
    return int(input("Escolha uma opção: "))


def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(dados + "\n")


def listar_extrato():
    if not os.path.exists("extrato.txt"):
        print("Nenhuma operação registrada.")
        return

    print("---------- EXTRATO DE OPERAÇÕES ----------")
    with open("extrato.txt", "r") as arquivo:
        print(arquivo.read())


def cadastrar_banco():
    codigo = int(input("Digite o código do banco: "))
    nome = input("Digite o nome do banco: ")
    banco = Banco(codigo, nome)
    salvar_dados("bancos.txt", f"{codigo},{nome}")
    return banco


def cadastrar_agencia(banco):
    codigo = int(input("Digite o código da agência: "))
    nome = input("Digite o nome da agência: ")
    agencia = Agencia(codigo, nome, banco)
    salvar_dados("agencias.txt", f"{codigo},{nome},{banco.codigo}")
    return agencia


def cadastrar_cliente():
    codigo = int(input("Digite o código do cliente: "))
    nome = input("Digite o nome do cliente: ")
    cliente = Cliente(codigo, nome)
    salvar_dados("clientes.txt", f"{codigo},{nome}")
    return cliente


def cadastrar_conta(cliente, banco, agencia):
    numero = int(input("Digite o número da conta: "))
    saldo = float(input("Digite o saldo inicial: "))
    data_saldo = input("Digite a data do saldo inicial: ")
    limite_credito = float(input("Digite o limite de crédito: "))
    conta = ContaCorrente(numero, cliente, banco, agencia, saldo, data_saldo, limite_credito)
    salvar_dados(
        "contas.txt",
        f"{numero},{cliente.codigo},{banco.codigo},{agencia.codigo},{saldo},{data_saldo},{limite_credito}",
    )
    return conta


def realizar_operacao(cliente, banco, agencia):
    tipo = input("Digite o tipo de operação (entrada/saída): ").lower()
    valor = float(input("Digite o valor da operação: "))
    data_movi = input("Digite a data da operação: ")

    operacao = Operacao(cliente, banco, agencia, data_movi, tipo, valor)
    operacao.executar_operacao()

    salvar_dados(
        "extrato.txt",
        f"Cliente: {cliente.nome}, Banco: {banco.nome}, Agência: {agencia.nome}, "
        f"Data: {data_movi}, Tipo: {tipo}, Valor: R${valor:.2f}",
    )


def main():
    bancos = []
    clientes = []

    while True:
        opcao = menu()
        if opcao == 1:
            banco = cadastrar_banco()
            bancos.append(banco)
        elif opcao == 2:
            banco_codigo = int(input("Digite o código do banco para vincular a agência: "))
            banco = next((b for b in bancos if b.codigo == banco_codigo), None)
            if banco:
                agencia = cadastrar_agencia(banco)
                banco.adicionar_agencia(agencia)
            else:
                print("Banco não encontrado.")
        elif opcao == 3:
            cliente = cadastrar_cliente()
            clientes.append(cliente)
        elif opcao == 4:
            cliente_codigo = int(input("Digite o código do cliente: "))
            cliente = next((c for c in clientes if c.codigo == cliente_codigo), None)
            if cliente:
                banco_codigo = int(input("Digite o código do banco: "))
                banco = next((b for b in bancos if b.codigo == banco_codigo), None)
                if banco:
                    agencia_codigo = int(input("Digite o código da agência: "))
                    agencia = next((a for a in banco.agencias if a.codigo == agencia_codigo), None)
                    if agencia:
                        conta = cadastrar_conta(cliente, banco, agencia)
                        cliente.adicionar_conta(conta)
                        agencia.adicionar_conta(conta)
                    else:
                        print("Agência não encontrada.")
                else:
                    print("Banco não encontrado.")
            else:
                print("Cliente não encontrado.")
        elif opcao == 5:
            cliente_codigo = int(input("Digite o código do cliente: "))
            cliente = next((c for c in clientes if c.codigo == cliente_codigo), None)
            if cliente:
                banco_codigo = int(input("Digite o código do banco: "))
                banco = next((b for b in bancos if b.codigo == banco_codigo), None)
                if banco:
                    agencia_codigo = int(input("Digite o código da agência: "))
                    agencia = next((a for a in banco.agencias if a.codigo == agencia_codigo), None)
                    if agencia:
                        realizar_operacao(cliente, banco, agencia)
                    else:
                        print("Agência não encontrada.")
                else:
                    print("Banco não encontrado.")
            else:
                print("Cliente não encontrado.")
        elif opcao == 6:
            listar_extrato()
        elif opcao == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

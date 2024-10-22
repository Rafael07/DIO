""" Seguindo o módulo "Sintaxe básica com Python", adotamos o paradigma procedural para entregar o sistema bancário requisitado
    pela atividade, entregando as funcionalidades de maneira que o programa funcione conforme o esperado. Os nomes das funções são 
    autoexplicativos quanto a suas funcionalidades e, de maneira muito simples, executam as movimentações realizadas pelo usuário.
    """
from datetime import date, datetime


def menu_transacoes():
    return """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Cadastrar Conta
    [6] Listar Conta

    [0] Sair

    =>  """


def data_hora_atual():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES):
    print('\nDepósito\n')
    deposito = float(input("Insira o valor a depositar: R$ "))
    
    if numero_transacoes >= LIMITE_TRANSACOES:
        print(f'Limite de transações permitidas em {date.today().strftime('%d/%m/%Y')} excedidas.')
    elif deposito > 0:
        saldo += deposito
        extrato += f'{data_hora_atual()} - Depósito: R$ {deposito:.2f}\n'
        numero_transacoes += 1
    else:
        print('O valor para depósito informado não é válido.')
    
    return saldo, extrato, numero_transacoes


def sacar(saldo, extrato, numero_saques, numero_transacoes, LIMITE_SAQUES, LIMITE_TRANSACOES, LIMITE):
    print('\nSaque\n')
    saque = float(input("Insira o valor a sacar: R$ "))

    if saque > saldo:
        print('O valor solicitado é maior que seu saldo atual.')
    elif saque > LIMITE:
        print(f'O valor limite para saques é de R$ {LIMITE:.2f}.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Limite de saques diários excedidos.')
    elif numero_transacoes >= LIMITE_TRANSACOES:
        print('Limite de transações diárias excedidas.')
    elif saque > 0:
        saldo -= saque
        extrato += f'{data_hora_atual()} - Saque: R$ {saque:.2f}\n'
        numero_saques += 1
        numero_transacoes += 1
    else:
        print('\nO valor para saque informado não é válido.\n')

    return saldo, extrato, numero_transacoes, numero_saques

def exibir_extrato(saldo, extrato):
    print('\nExtrato\n')
    print(extrato if extrato else 'Nenhuma movimentação realizada.')
    print(f'Saldo atual: R$ {saldo:.2f}\n')

def cadastrar_usuario(usuarios):
    cpf =input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ O CPF informado já foi vinculado a outro usuário! @@@\n")

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento no formato dia-mês-ano: ')
    endereco = input('Informe endereço com formato: logradouro, nº - bairro - cidade/sigla do estado: ')

    usuarios.append({'nome': nome, "data_nascimento":data_nascimento, 'cpf': cpf, 'endereço': endereco})

    print("\n==== Cliente cadastrado com sucesso! ====\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        
        print("\n==== Conta criada com sucesso! ====\n")
        return {'agencia': agencia, 'numero_conta':numero_conta, "usuario":usuario}
    
    print('\n==== Usuário não encontrado! ====\n')

def listar_contas(contas):
    for conta in contas:
        print(f'------------------------------\nAgência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n')

def main():
    LIMITE = 500
    LIMITE_SAQUES = 3
    LIMITE_TRANSACOES = 10
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_transacoes = 0
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu_transacoes())

        if opcao == '1':
            saldo, extrato, numero_transacoes = depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES)

        elif opcao == '2':
            saldo, extrato, numero_transacoes, numero_saques = sacar(saldo, extrato, numero_saques, numero_transacoes, LIMITE_SAQUES, LIMITE_TRANSACOES, LIMITE)
        
        elif opcao == '3':
            exibir_extrato(saldo, extrato)
        
        elif opcao =='4':
            cadastrar_usuario(usuarios)
        
        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =='6':
            listar_contas(contas)
       
        elif opcao == '0':
            break
        
        else:
            print('\nOperação inválida, selecione atentamente uma das opções mostradas.\n')

main()

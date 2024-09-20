""" Seguindo o módulo "Sintaxe básica com Python", adotamos o paradigma procedural para entregar o sistema bancário requisitado
    pela atividade, entregando as funcionalidades de maneira que o programa funcione conforme o esperado. Os nomes das funções são 
    autoexplicativos quanto a suas funcionalidades e, de maneira muito simples, executam as movimentações realizadas pelo usuário.
    """

def menu():
    return """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    =>  """

def depositar(saldo, extrato):
    print('\nDepósito\n')
    deposito = float(input("Insira o valor a depositar: R$ "))
    
    if deposito > 0:
        saldo += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'
    else:
        print('O valor para depósito informado não é válido.')
    
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, LIMITE):
    print('\nSaque\n')
    saque = float(input("Insira o valor a sacar: R$ "))

    if saque > saldo:
        print('O valor solicitado é maior que seu saldo atual.')
    elif saque > LIMITE:
        print(f'O valor limite para saques é de R$ {LIMITE:.2f}.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Limite de saques diários excedidos.')
    elif saque > 0:
        saldo -= saque
        extrato += f'Saque: R$ {saque:.2f}\n'
        numero_saques += 1
    else:
        print('O valor para saque informado não é válido.')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print('\nExtrato\n')
    print(extrato if extrato else 'Nenhuma movimentação realizada.')
    print(f'Saldo atual: R$ {saldo:.2f}\n')

def main():
    saldo = 0
    LIMITE = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu())

        if opcao == '1':
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == '2':
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, LIMITE)
        elif opcao == '3':
            exibir_extrato(saldo, extrato)
        elif opcao == '0':
            break
        else:
            print('Operação inválida, selecione atentamente uma das opções mostradas.')

# Chamar a função principal para iniciar o programa
main()

def sacar(saldo, solicitacao, extrato):
    if solicitacao > saldo:
        print("Saldo insuficiênte.")
    elif solicitacao > 500:
        print("Limite de saque excedido.")
    else:
        saldo -= solicitacao
        extrato += f"\nSacado: R${solicitacao}"
    
    return saldo, extrato

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepositado: R${valor}"
        
    else:
        print("Valor inválido. Por favor, tente novamente.")
    
    return saldo, extrato


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Quanto deseja depositar? "))
        saldo, extrato = depositar(saldo, valor, extrato)
        

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            solicitacao = int(input("Quanto deseja sacar? "))
            saldo, extrato = sacar(saldo, solicitacao, extrato)
            numero_saques+=1
        else:
            print("Limite de saques excedido.")
        
    elif opcao == "e":
        if extrato == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
            print(f"Saldo: R${saldo}")
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
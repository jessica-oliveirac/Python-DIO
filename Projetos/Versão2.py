menu = """
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Vizualizar extrato
    [4] Sair
    ==========================
    => """
saldo = 0
limite = 500
qtdSaques = 0
LIMITE_SAQUES = 3
deposito = 0
saque = 0
while True:
    opcao = input(menu)
    if opcao == 1:
        print("Deposito")
        valor = float(input("Deposito: "))
        if valor>0:
            deposito = valor
            saldo += deposito
    elif opcao == 2:
        print("Sacar: ")
        if valor>0 and valor<=limite or qtdSaques<=LIMITE_SAQUES :
            saldo -= valor
            saque = saldo
        else:
            print("Não será possível sacar o dinheiro por falta de saldo!")
    elif opcao == 3:
        print(f"Visualização")
        print("--------------------")
        print(f"Depósito: {deposito}")
        print(f"Saque: {saque}")
        print("--------------------")
        print(f"Saldo: R$ {valor}")
    elif opcao == 4:
        break
    else:
        print("Obrigado por utilizar o nosso sistema bancário, até logo!")
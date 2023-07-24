print(
    """
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Vizualizar extrato
    [4] Sair
    ==========================
    """
)
opcao = int(input(""))
opcao = int(input("Escolha uma opção: "))
while opcao !=0:
    if opcao == 1:
        print("Depositar: ")
        valor = float(input("Deposito: "))
        if valor>0 and valor<=500:
            deposito = valor
        else:
            print()
        print (f'Saldo: {depositar}')
    elif opcao == 2:
        print("Sacar: ")
        if valor>0:
            saque -=valor
            valor = saque
        else:
            print("Não será possível sacar o dinheiro por falta de saldo!")
    elif opcao == 3:
        print(f"Visualização")
        print("--------------------")
        print(f"Depósito: {deposito}")
        print(f"Saque: {saque}")
        print("--------------------")
        print(f"Saldo: R$ {valor}")
    else:
        print("Obrigado por utilizar o nosso sistema bancário, até logo!")
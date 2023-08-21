saldo = 0
extrato = ""
qtdSaques = 0
opcao = 1
deposito = 0
VALOR_LIMITE = 500
SAQUE_LIMITE = 3
while opcao !=0:
    print( 
    """   
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Vizualizar Extrato
    [4] Sair
    ==========================
    """) 
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        valor = float(input("Deposite um valor: "))
        if valor>0:
            saldo += valor
            extrato += f" Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor inválido.")
    elif opcao == 2:
        valor = float(input("Saque um valor: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > VALOR_LIMITE 
        excedeu_saques = qtdSaques >= SAQUE_LIMITE 
        if excedeu_saldo:
            print("ERRO! Saldo insuficiente.")
        elif excedeu_limite:
            print("ERRO! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("ERRO! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R$ {valor:.2f}\n"
            qtdSaques += 1
        else:
            print("ERRO! O valor informado é inválido.")
    elif opcao == 3:
        print("\n======== VIZUALIZAÇÃO DE EXTRATO ==========")
        print(" Nenhuma movimentação realizada na conta." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===========================================")
    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

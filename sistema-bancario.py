menu = '''
    [0] Extrato
    [1] Depósito
    [2] Saque
    [3] Sair

-- '''


saldo = 0
limite = 500
extrato = "----------------------------------------"
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 0:
        print(saldo)
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("----------------------------------------\n")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    elif opcao == 1:
        valor = float(input("Informe o valor a ser dpositado: "))
        if valor > 0:
            saldo += valor
            print(saldo)
            extrato += f"""
    Depósito: R$ {valor:.2f}
    """
        else:
            print("O Valor informado é inválido")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:    
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saque >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"""
    Saque: R$ {valor:.2f}
    """
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == 3:
        break
    else:
        print("""
              =========================
              Digite uma opção valida!
              =========================
              """)
    
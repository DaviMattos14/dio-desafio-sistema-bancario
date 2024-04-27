def menu():
    menu ='''
    [0] Extrato
    [1] Depósito
    [2] Saque
    [3] Criar conta
    [4] Listar contas
    [5] Cadastrar Cliente
    [6] Sair

-- '''
    return int(input(menu))


def filtrar_clientes(ls_clientes, cpf):
    for i in ls_clientes:
        if cpf in i: 
            return i
        
def cadastrar_cliente(ls_clientes):
    cpf = input("Informe o CPF (somente número): ")
    for i in ls_clientes:
        if cpf in i: return print("Cliente já cadastrado")
    
    nome = input("Informe o nome : ")
    data_nasc = str(input("Informe a data de nascimento (dd/mm/aaaa): "))
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    ls_clientes.append([nome, data_nasc, cpf, endereco])
    print("\nCadastro Concluido com Sucesso!\n")

def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor a ser dpositado: "))
    if valor > 0:
        saldo += valor
        extrato += f"""
    Depósito: R$ {valor:.2f}
        """
        print("Deposito realizado com sucesso!")
    else:
        print("O Valor informado é inválido")
    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:    
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"""
Saque: R$ {valor:.2f}
"""
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def criar_conta(clientes, numero_conta, agencia):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_clientes(clientes, cpf)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\nCliente não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            Nº Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente'][0]}
        """
        print("=" * 100)
        print(f"\n {linha}")

def imprimi_extrato(extrato, saldo):
    print(saldo)
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("----------------------------------------\n")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")
    

def main():
    clientes = []
    contas_clientes=[]
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = "----------------------------------------"
    numero_saque = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == 0:
            imprimi_extrato(extrato, saldo)
        elif opcao == 1:
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 2:
            saldo, extrato, numero_saque = saque(saldo=saldo, extrato= extrato, limite= limite, numero_saques=numero_saque, limite_saques=LIMITE_SAQUES)
        elif opcao == 3:
            n_contas = len(contas_clientes) + 1
            conta = criar_conta(clientes,n_contas, AGENCIA)

            if conta:
                contas_clientes.append(conta)
        elif opcao == 4:
            listar_contas(contas_clientes)
        elif opcao == 5:
            cadastrar_cliente(clientes)
        elif opcao == 6:
            break
        else:
            print("""
                =========================
                Digite uma opção valida!
                =========================
                """)
            
main()
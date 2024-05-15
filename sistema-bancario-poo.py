
class Cliente:
    def __init__(self, cpf, nome, data_nasc, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.contas = []

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        extrato = "----------------------------------------"
        self._historico = extrato
    
    def getNumConta(self):
        return self._numero
    def getAgencia(self):
        return self._agencia
    def getCliente(self):
        return self._cliente.nome

    def imprimir_extrato(self):
        print(self._saldo)
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self._historico else self._historico)
        print("----------------------------------------\n")
        print(f"\nSaldo: R$ {self._saldo:.2f}")
        print("===========================================")

    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico += f"""
        Depósito: R$ {valor:.2f}
            """
            print("===== Deposito realizado com sucesso! =====")
        else:
            print("O Valor informado é inválido")

    def saque(self, valor):
        if valor > self._saldo:
            print("Você não tem saldo suficiente!")
        elif valor <= self._saldo:
            self._saldo -= valor
            self._historico += f"""
        Saque: R$ {valor:.2f}
            """
            print("===== Saque realizado com sucesso =====")
        else:
            print("Operação falhou!")

def filtrar_clientes(ls_clientes, cpf):
    for i in ls_clientes:
        if i.cpf == cpf: 
            return i
        
def cadastrar_cliente(ls_clientes):
    cpf = input("Informe o CPF (somente número): ")
    for i in ls_clientes:
        if i.cpf == cpf: return print("Cliente já cadastrado")
    
    nome = input("Informe o nome : ")
    data_nasc = str(input("Informe a data de nascimento (dd/mm/aaaa): "))
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = Cliente(cpf=cpf, nome=nome, data_nasc=data_nasc,endereco=endereco)    

    ls_clientes.append(cliente)
    print("\nCadastro Concluido com Sucesso!\n")

def criar_conta(num_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return 
    conta = Conta(num_conta, cliente)
    contas.append(conta)
    cliente.contas.append(conta)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta.getAgencia()}
            Nº Conta:\t\t{conta.getNumConta()}
            Titular:\t{conta.getCliente()}
        """
        print("=" * 100)
        print(f"\n {linha}")

def sacar(ls_cliente):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(ls_cliente, cpf)
    if not cliente: 
        print("Cliente não encontrado")
        return
    
    num_conta = int(input("Digite o numero da conta: "))
    for conta in cliente.contas:
        if num_conta == conta.getNumConta():
            valor = float(input("Valor: R$ "))
            conta.saque(valor)
    
def depositar(ls_cliente):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(ls_cliente, cpf)
    if not cliente: 
        print("Cliente não encontrado")
        return
    
    num_conta = int(input("Digite o numero da conta: "))
    for conta in cliente.contas:
        if num_conta == conta.getNumConta():
            valor = float(input("Valor: R$ "))
            conta.deposito(valor)

def extrato(ls_cliente):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(ls_cliente, cpf)
    if not cliente: 
        print("Cliente não encontrado")
        return
    
    num_conta = int(input("Digite o numero da conta: "))
    for conta in cliente.contas:
        if num_conta == conta.getNumConta():
            conta.imprimir_extrato()

def menu():
    menu ='''
    [0] Extrato
    [1] Depósito
    [2] Saque
    [3] Listar contas
    [4] Criar conta
    [5] Cadastrar Cliente
    [6] Sair

-- '''
    return int(input(menu))

def main():
    clientes = []
    contas_clientes=[]

    while True:
        opcao = menu()
        if opcao == 6:
            break
        elif opcao == 5:
            cadastrar_cliente(clientes)
        elif opcao == 4:
            num_conta = len(contas_clientes) + 1
            criar_conta(num_conta, clientes, contas_clientes)
        elif opcao == 3:
            listar_contas(contas_clientes)
        elif opcao == 2:
            sacar(clientes)
        elif opcao == 1:
            depositar(clientes)
        elif opcao == 0:
            extrato(clientes)
        else:
            print("""
                =========================
                Digite uma opção valida!
                =========================
                """)
            
main()
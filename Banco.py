menu = """

[0] Criar usuário
[1] Criar conta
[2] Depositar
[3] Sacar
[4] Extrato
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuario = {
    "nome": [],
    "Data_Nascimento": [],
    "cpf": [],
    "endereço": []
}
conta_usuario = {
    "agencia": [],
    "conta": [],
    "usuario": [],
    "saldo": [],
    "limite": [],
    "extrato": [],
    "max_saques": [],
    "numero_saques": []
}
LIMITE_SAQUES = 3


def criar_usuario():
    nome = input("Digite o nome do usuário\n")
    data = input("Digite a data de nascimento\n")

    while True:
        cpf = input("Digite o CPF apenas em números\n")
        if "." in str(cpf):
            print("Apenas números devem ser digitados no CPF")
        else:
            break
    rua = input("Digite sua rua e número\n")
    bairro = input("Digite seu bairro\n")
    sigla = input("Digite a cidade e a sigla do estado que você mora\n")

    usuario["nome"].append(nome)
    usuario["Data_Nascimento"].append(data)
    usuario["cpf"].append(cpf)
    usuario["endereço"].append(f"{rua} - {bairro} - {sigla}")


def criar_conta(nome):
    i = 1
    if nome in usuario["nome"]:
        conta_usuario["agencia"].append("%04d" % 1)
        conta_usuario["conta"].append(i)
        conta_usuario["extrato"].append("Seu extrato é:")
        conta_usuario["limite"].append(500)
        conta_usuario["numero_saques"].append(0)
        conta_usuario["max_saques"].append(3)
        conta_usuario["saldo"].append(0)
        conta_usuario["usuario"].append(nome)
        print("Conta criada com sucesso")
        print(f"O numero da sua conta é {conta_usuario['conta'][i-1]}")
        i = +1
    else:
        print("Você não possui uma conta cadastrada")


def depositar(conta):
    if conta in conta_usuario["conta"]:
        print(f"Bem vindo,{conta_usuario['usuario'][conta-1]}")
        print("Deposito")
        print("-------------------------")
        deposito = (input("Digite o valor que queira depositar\n"))
        deposit_num = float(deposito)
        if deposit_num > 0:
            conta_usuario["saldo"][conta-1] = + deposit_num
            conta_usuario["extrato"][conta-1] = conta_usuario["extrato"][conta-1]+"Você depositou R$" + deposito
            print(f"Você depositou R${deposito}")

        else:
            print("Não foi possível depositar")
    else:
        print("Você não possui uma conta cadastrada")


def sacar(conta):
    if conta in conta_usuario["conta"]:
        print(f"Bem vindo,{conta_usuario['usuario'][conta-1]}")
        print("Saque")
        print("-------------------------")
        saque = (input("Digite o valor que queira sacar\n"))
        saque_num = float(saque)
        if saque_num > 0:
            conta_usuario["saldo"][conta-1] = - saque_num
            conta_usuario["numero_saques"][conta-1] = +1
            conta_usuario["extrato"][conta-1] = conta_usuario["extrato"][conta-1] + "Você sacou R$" + saque
            print(f"Você sacou R${saque}")
        elif saque > conta_usuario["limite"][conta-1]:
            print(
                f"Você não pode sacar mais que o seu limite de R${conta_usuario['limite'][conta-1]}")
        elif conta_usuario["numero_saques"][conta-1] > conta_usuario["max_saques"][conta-1]:
            print(
                f"Você já atingiu seu limite de saques de {conta_usuario['max_saques'][conta-1]} saques por dia")
        else:
            print("Digite um valor válido")
    else:
        print("Você não possui uma conta cadastrada")


def retirar_extrato(conta):
    if conta in conta_usuario["conta"]:
        print(f"Bem vindo,{conta_usuario['usuario'][conta-1]}")
        print("Extrato")
        print("-------------------------")
        print(f"{conta_usuario['extrato'][conta-1]}")
        print(f"Seu saldo atual é de R${conta_usuario['saldo'][conta-1]}")
        print("-------------------------")
    else:
        print("Você não possui uma conta cadastrada")


while True:

    opcao = input(menu)

    if opcao == "0":
        criar_usuario()

    elif opcao == "1":
        user = input("Digite o nome do seu usuario\n")
        criar_conta(user)

    elif opcao == "2":
        number = int(input("Digite o numero da sua conta\n"))
        depositar(number)

    elif opcao == "3":
        number = int(input("Digite o numero da sua conta\n"))
        sacar(conta=number)

    elif opcao == "4":
        number = int(input("Digite o numero da sua conta\n"))
        retirar_extrato(number)

    elif opcao == "5":
        break
    else:
        print("Digite um comando válido.")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        print("-------------------------")
        deposito = input("Digite o valor de depósito:\n")
        deposito_int = int(deposito)
        if deposito_int < 0:
            print("Não foi possível realizar o depósito.")
        else:
            saldo = saldo+deposito_int
            print("Você depositou" + " R$" + deposito)
            extrato = extrato + "Deposito de R$" + deposito + "\n"

    elif opcao == "s":
        print("Saque")
        print("-------------------------")
        saque = input("Digite o valor do saque:\n")
        saque_int = int(saque)
        if saque_int > limite:
            print("Não é possível sacar mais que o limite")
        elif saque_int > saldo:
            print("Saldo insuficiente")
        elif LIMITE_SAQUES == 0:
            print("Você alcançou seu limite diário de saque")
        else:
            LIMITE_SAQUES =-1
            print ("Você sacou R$" + saque)
            saldo = saldo - saque_int
            extrato = extrato + ("Saque de R$ " + saque + "\n")
            
    elif opcao == "e":
        print("Extrato")
        print("-------------------------")
        if extrato == "":
            print("Não foram realizados movimentações")
            print("Seu saldo atual é R$" + str(saldo))
        else:
            print(extrato)
            print("Seu saldo atual é R$" + str(saldo))
    elif opcao == "q":
        break
    else:
        print("Digite um comando válido.")
def menu():
    saldo= 10500.0

    while True:
        print("\n Menu:  ")
        print("1 - Saldo")
        print("2 - Depósito")
        print("3 - Saque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
              print(f"Seu saldo é R$ {saldo:.2f}")
            case "2":
                valor = float(input("Digite o valor para depósito: R$"))
                
                if valor > 0:
                    saldo += valor
                    print(f"Despósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Valor inválido para depósito.")
            case "3":
                valor = float(input("Digite o valor para saque:  "))
                if 0 < valor <= saldo:
                    saldo -=valor
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Saldo insuficiente ou valor inválido") 
            case "0":
                print("Saindo...Obrigado por usar o sistema.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
#FORA DA FUNÇÃO
menu()
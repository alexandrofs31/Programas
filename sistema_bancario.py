"""
Este módulo implementa um programa simples para operações bancárias.

"""

MENU = """
[d] Depositar
[s] Sacar
[e] EXTRATO
[q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            SALDO += valor
            EXTRATO += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido. O valor do depósito deve ser positivo.")

    elif opcao == "s":

        if NUMERO_SAQUES < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))

            if valor > 0 and valor <= LIMITE and valor <= SALDO:
                SALDO -= valor
                EXTRATO += f"Saque: R$ {valor:.2f}\n"
                NUMERO_SAQUES += 1

            elif valor > LIMITE:
                print(f"Limite máximo de saque é de R$ {LIMITE:.2f}.")

            elif valor > SALDO:
                print("Saldo insuficiente.")

            else:
                print("Valor inválido. O valor do saque deve ser positivo.")

        else:
            print("Limite diário de saques atingido.")

    elif opcao == "e":
        print("\n============== Extrato ============== ")
        print("Não foram realizadas movimentações. " if not EXTRATO else EXTRATO)
        print(f"Saldo atual: R$ {SALDO:.2f}")
        print("\n===================================== ")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(conta_bancaria):
    try:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito >= 0:
            print("Depósito realizado com sucesso!")
            return deposito, conta_bancaria + deposito
        else:
            print("Só aceitamos depósito com valores positivos.")
            return None, conta_bancaria
    except ValueError:
        print("Valor inválido! Digite um número.")
        return None, conta_bancaria

def sacar(conta_bancaria, limite_saque):
    try:
        if limite_saque > 0:
            saque = float(input("Digite o valor para o saque: "))
            if 0 < saque <= 500:
                if saque > conta_bancaria:
                    print("Saque inválido, valor do saque é maior que o valor da conta bancária")
                    return None, conta_bancaria, limite_saque
                else:
                    print("Saque realizado com sucesso!")
                    return saque, conta_bancaria - saque, limite_saque - 1
            elif saque > 500:
                print("Não é permitido saque acima de R$500,00")
                return None, conta_bancaria, limite_saque
            else:
                print("Não é permitido saque com valores negativos.")
                return None, conta_bancaria, limite_saque
        else:
            print("Limite diário de saque diário atingido! Favor retornar amanhã")
            return None, conta_bancaria, limite_saque
    except ValueError:
        print("Valor inválido! Digite um número.")
        return None, conta_bancaria, limite_saque

def extrato(lista_extrato, conta_bancaria):
    if lista_extrato:
        print("Extrato:")
        for operacao in lista_extrato:
            print(operacao)
        print(f"Valor atual da conta bancária: R${conta_bancaria:.2f}")
    else:
        print("Não foram realizadas movimentações.")

def formatar_valor(valor):
    return f"{valor:.2f}".replace(',', '_').replace('.', ',').replace('_', '.')

def main():
    lista_extrato = []
    conta_bancaria = 0
    limite_saque = 3
    opcao = "Sim"

    print("Olá, seja bem vindo ao sistema bancário! \nEscolha o número correspondente a ação que deseja:")

    while opcao.lower() in ["s", "sim"]:
        print("\n 1 - Depósito\n 2 - Saque\n 3 - Extrato\n 4 - Sair\n")
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            continue

        if escolha == 1:
            deposito, conta_bancaria = depositar(conta_bancaria)
            if deposito is not None:
                lista_extrato.append(f"Depósito realizado no valor de R${formatar_valor(deposito)}")

        elif escolha == 2:
            saque, conta_bancaria, limite_saque = sacar(conta_bancaria, limite_saque)
            if saque is not None:
                lista_extrato.append(f"Saque realizado no valor de R${formatar_valor(saque)}")

        elif escolha == 3:
            extrato(lista_extrato, conta_bancaria)

        elif escolha == 4:
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

        opcao = input("Deseja realizar outra operação? S/N\n")

if __name__ == "__main__":
    main()

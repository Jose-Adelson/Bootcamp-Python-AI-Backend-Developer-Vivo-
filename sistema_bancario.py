extrato=[] #Essa operação deve listar todos os depósitos e saques realizados na conta.
conta_bancaria = 0
limite_saque = 3
opcao = "S"

#Os valores devem ser exibidos utilizando o formato R$ xxx,xx
while opcao in ["S", "s", "Sim", "sim"]:
    print("Olá, seja bem vindo ao sistema bancário! \nEscolha o número correspondente a ação que deseja:")
    print("\n 1 - Depósito\n 2 - Saque\n 3 - Extrato\n 4 - Sair\n")
    escolha = int(input())
    if escolha == 1:
        #Deve ser possível depositar apenas valores possitivos na conta bancária
        deposito=float(input("Digite o valor do depósito: "))
        

        if deposito >= 0:
            conta_bancaria = conta_bancaria + deposito
            print("Depósito realizado com sucesso!")
            deposito= f"{deposito:.2f}".replace(',','_').replace('.',',').replace('_','.')
            #Todos os depósitos devem ser armazenados em uma váriavel e exibidos na operação de extrato
            extrato.append(f"Depósito realizado no valor de R${deposito}")
            

        else:
            print("Só aceitamos depósito com valores positivos.")

    elif escolha == 2:
        if limite_saque > 0:
            saque=float(input("Digite o valor para o saque: "))
            #O sistema deve permitir realizar apenas 3 saques diários com limite de R$500,00 cada.
            if saque >0 and saque <= 500:
                if saque > conta_bancaria:
                    #Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será 
                    #possível sacar o dinheiro por falta de saldo. 
                    print("Saque inválido, valor do saque é maior que o valor da conta bancária")
                else:
                    conta_bancaria = conta_bancaria - saque
                    limite_saque = limite_saque - 1
                    saque= f"{saque:.2f}".replace(',','_').replace('.',',').replace('_','.')
                    #Todos os saques devem ser armazenados em uma váriavel e exibidos na operação de extrato
                    extrato.append(f"Saque realizado no valor de R${saque}")
            elif saque > 500:
                print("Não é permitido saque acima de R$500,00")
            else:
                print("Não é permitido saque com valores negativos.")
        else:
            print("Limite diário de saque diário atingido! favor retornar amanhã")

    #No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram 
    #realizadas movimentações. 

    elif escolha == 3:
        if extrato == []:
            print("Não foram realizadas movimentações.")
        else:
            print("extrato:")
            for operacao in extrato:
                print(operacao, end="\n")

            conta_bancaria= f"{conta_bancaria:.2f}".replace(',','_').replace('.',',').replace('_','.')
            print(f"Valor atual da conta bancária: R${conta_bancaria} \n")

    elif escolha == 4:
        break

    opcao = input("Deseja realizar outra operação? S/N\n")



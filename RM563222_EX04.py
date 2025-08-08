opcao = 0

while opcao != 4:
    print("1. CDB")
    print("2. LCI")
    print("3. LCA")
    print("4. Sair")

    opcao = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

    if opcao == 4:
        print("Saindo do programa...")
        break

    if opcao == 1 or opcao == 2 or opcao == 3:
        valor = float(input("Digite o valor a ser resgatado: "))
        dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

        if opcao == 1:
            if dias <= 180:
                aliquota = 22.5
            elif dias <= 360:
                aliquota = 20
            elif dias <= 720:
                aliquota = 17.5
            else:
                aliquota = 15

            imposto = valor * (aliquota / 100)
            print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
        else:
            print("Esse tipo de investimento é isento de imposto de renda.")
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
valorDivida = float(input("Digite o valor da dívida: "))
taxaJuros = [0, 10, 15, 20, 25]
numeroParcelas = [1, 3, 6, 9, 12]

for x in range(len(numeroParcelas)):
    parcelas = numeroParcelas[x]
    juros = taxaJuros[x]

    valorJuros = valorDivida * juros / 100
    valorTotal = valorDivida + valorJuros
    valorParcelas = valorTotal / parcelas

    print(f"Total: R${valorTotal:.2f} Juros: R${valorJuros:.2f} Número de parcelas:{parcelas} Valor da parcela: R${valorParcelas:.2f}")
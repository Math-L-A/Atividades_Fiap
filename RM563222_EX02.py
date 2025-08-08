precoVeiculo = int(input("Digite o valor do veículo: "))
precoAVista = (precoVeiculo * 0.80)

print(f"O preço final à vista com desconto de 20% é: {precoAVista:.2f}")

percentualAcrescimo = 3

for parcelas in range (6, 61, 6):
    somaTotal = precoVeiculo * (percentualAcrescimo / 100) + precoVeiculo
    valorParcelas = somaTotal / parcelas
    print(f"O preço final parcelado em {parcelas}X é de R${somaTotal:.2f} com parcelas de R${valorParcelas:.2f}")
    percentualAcrescimo += 3
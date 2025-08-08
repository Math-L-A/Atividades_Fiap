colaboradores = int(input("Informe o número de colaboradores: "))

votos = {
"segunda-feira" : 0,
"terça-feira" : 0,
"quarta-feira" : 0,
"quinta-feira" : 0,
"sexta-feira" : 0
}

for numeroPerguntas in range (colaboradores):
    dia = input(f"Votação {numeroPerguntas + 1}, Informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar da live: ").lower()

    while dia not in votos:
        print("Dia inválido, escreva novamente :D")
        dia = input(f"Votação {numeroPerguntas + 1}, Informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar da live: ").lower()

    votos[dia] += 1

print("\nResultado da votação: ")
for dia, quantidade in votos.items():
    print(f"{dia}: {quantidade} votos")

resultadoMaisVotado = max(votos, key=votos.get)
maiorVoto = max(votos.values())
diasMaisVotados = list(votos.values()) .count(maiorVoto)

if diasMaisVotados > 1:
    print("\nHouve empate")
    for dia, quantidade in votos.items():
        if quantidade == maiorVoto:
            print(f"{dia} ({quantidade} votos)")
else:
    for dias, quantidade in votos.items():
        if quantidade == maiorVoto:
            print(f"\nO dia escolhido pelos colaboradores é: {resultadoMaisVotado}")
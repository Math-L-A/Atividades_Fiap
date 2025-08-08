batimentos = int(input("informe o seu número de BATIMENTOS POR MINUTO (BPM): "))
idade = int(input("informe o sua IDADE: "))

if idade <= 2 and 120 <= batimentos <= 140:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif idade <= 2 and batimentos < 120:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif idade <= 2 and batimentos > 140:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")

if 8 <= idade <= 17 and 80 <= batimentos <= 100:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif 8 <= idade <= 17 and batimentos < 80:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif 8 <= idade <= 17 and batimentos > 100:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")

if 18 <= idade <= 65 and 70 <= batimentos <= 80:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif 18 <= idade <= 65 and batimentos < 70:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif 18 <= idade <= 65 and batimentos > 80:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")

if idade > 65 and 50 <= batimentos <= 60:
    print("Os batimentos do usuário encontram-se DENTRO da faixa adequada")
elif idade > 65 and batimentos < 50:
    print("Os batimentos do usuário encontram-se ABAIXO da faixa adequada")
elif idade > 65 and batimentos > 60:
    print("Os batimentos do usuário encontram-se ACIMA da faixa adequada")
# Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para adivinhar o número, e então diga se a tentativa
# foi menor, maior ou correta. (Dica: lembre-se de usar o input dos exercícios anteriores). Mantenha o jogo executando até que o
# usuário digite "sair".

import random

while True:

    numero_random = random.randint(1, 9)
    print(numero_random)

    numero_adivinha = int(input("Digite o número que deseja para tentar adivinhar: "))

    if(numero_random == numero_adivinha):
        print("Parabens, você acertou o número!")
    elif(numero_random > numero_adivinha):
        print("O número que você escolheu é menor")
    else:
        print("O número que você escolheu é maior")

    continuar = input("Digite sair para abandonar o jogo: ").lower()
    if continuar == "sair":
        break

print("Obrigado por jogar, até a próxima!")
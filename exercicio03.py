while True:
    escolha1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()

    if escolha1 not in ["pedra", "papel", "tesoura"]:
        print("Jogada inválida. Tente novamente.")
        continue

    escolha2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

    if escolha2 not in ["pedra", "papel", "tesoura"]:
        print("Jogada inválida. Tente novamente.")
        continue

    if escolha1 == escolha2:
        print("Empate!")
    elif (escolha1 == "pedra" and escolha2 == "tesoura") or (escolha1 == "papel" and escolha2 == "pedra") or (escolha1 == "tesoura" and escolha2 == "papel"):
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")

    continuar = input("Deseja continuar jogando? (s/n): ").lower()
    if continuar != "s":
        break

print("Obrigado por jogar!")
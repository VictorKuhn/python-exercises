# Peça ao usuário um número. Retorne a ele se o número é par ou impar.

valor = int(input("Digite o valor desejado: "))

valor_resto = valor % 2

print(valor_resto)

if(valor_resto == 0):
    print("O valor escolhido é par")
else:
    print("O valor escolhido é impar")
# Peça uma string qualquer ao usuário e informe a ele se a string é um palíndromo ou não. (um palíndromo é uma string que pode ser lida da mesma forma, da esquerda para a direita ou vice-versa. Ex.: omo).

palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
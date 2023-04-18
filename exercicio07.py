with open('names.txt', 'r') as lista_nomes:
    conteudo = lista_nomes.read()

lista_nomes.close()

repeticoes = {}

linhas = conteudo.splitlines()

for linha in linhas:
    nome = linha.strip()

    if nome in repeticoes:
        repeticoes[nome] += 1
    else:
        repeticoes[nome] = 1

for nome, repeticao in repeticoes.items():
    print(f'{nome}: {repeticao} repetições')

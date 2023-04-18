from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

artigos = soup.find_all("h2")

nome_arquivo = 'hard-coded.txt'
with open(nome_arquivo, 'w') as file:
    for artigo in artigos:
        file.write(artigo.text + '\n')

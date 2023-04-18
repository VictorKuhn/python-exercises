from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
headlines = soup.find_all("h2")

for headline in headlines:
    print(headline.text.strip())
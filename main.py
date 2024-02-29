from bs4 import BeautifulSoup
import requests

url = 'https://docfish.ru/documents/stihi-na-kazahskom-yazyke-stih-abai-kunanbaev-leto-zhaz-poem-summer'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
olen = soup.find_all("div", "poem-text")

for div in olen:
    for br in div.find_all("br"):
        br.replace_with("")
    div.unwrap()

print(soup.text.strip())

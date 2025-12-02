import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

quotes = [q.text for q in soup.find_all("span", class_="text")]

print(quotes[:5])

import requests
from bs4 import BeautifulSoup

rus_word = "участие"
url = "https://wiktionary.org/wiki/" + rus_word

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

word = soup.find("strong", {"class": "Cyrl headword", "lang": "ru"}).text
russian_section = soup.find("span", {"id": "Russian"})
table = russian_section.find_next("table", {"class": "inflection-table"})
rows = table.find_all("tr")

print(word == "уча́стие")

for row in rows:
    cols = row.find_all("td")
    for col in cols:
        case = col.find("span", {"lang": "ru"})
        if case:
            print(case.text)

rus_word = "стороны"
url = "https://wiktionary.org/wiki/" + rus_word

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.find_all("strong", {"class": "Cyrl headword", "lang": "ru"}))

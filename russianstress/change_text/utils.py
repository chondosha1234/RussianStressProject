import requests
from bs4 import BeautifulSoup
import re

def add_stress(text):

    #word_list = text.split()
    # seperate out words and punctuation
    word_list = re.findall(r'\w+|[^\w\s]+', text)
    result = []

    for word in word_list:
        print(word)
        if not re.match(r'\W', word):   # if it is a word
            url = "https://wiktionary.org/wiki/" + word
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            russian_section = soup.find("span", {"id": "Russian"})
            if russian_section:
                rus_word = russian_section.find_next("strong", {"class": "Cyrl headword", "lang": "ru"})
            if rus_word:
                result.append(rus_word.text)
            else:
                result.append(word)
        else:
            result.append(word) #just punctuation

    print(result)
    return ' '.join(result)

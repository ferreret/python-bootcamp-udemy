from bs4 import BeautifulSoup
from random import choice
import requests


class Quote():
    def __init__(self, text, author, link):
        self.text = text
        self.author = author
        self.link = link

    def __repr__(self):
        return f"{self.text} {self.author}"


url = "http://quotes.toscrape.com"
list_quotes = []

exists_next = True
next_url = url

while(exists_next):

    response = requests.get(next_url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")

    for quote in quotes:
        quote_text = quote.select_one(".text").text
        quote_author = quote.select_one(".author").text
        quote_link = quote.find("a")["href"]
        quote_to_add = Quote(quote_text, quote_author, quote_link)
        # print(quote_to_add)
        list_quotes.append(quote_to_add)

    next_button = soup.select_one(".next")
    if next_button:
        link = next_button.find("a")["href"]
        next_url = url + link
    else:
        exists_next = False

guesses_remaining = 4

guess_quote = choice(list_quotes)

print("Who said this quote?")
print(guess_quote.text)

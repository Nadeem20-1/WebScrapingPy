from bs4 import BeautifulSoup
import urllib.request

website = "https://quotes.toscrape.com/"
bs = BeautifulSoup(urllib.request.urlopen(website), features="html.parser")

allQuotes = []

for quote in bs.find_all(class_="quote"):
    newDict = {}
    newDict.update({"author" : quote.find(class_="author").text})
    newDict.update({"quote" : quote.find(class_="text").text})
    allQuotes.append(newDict)

for quote1 in allQuotes:
    print(quote1)
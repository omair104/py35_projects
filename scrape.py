import requests
from bs4 import BeautifulSoup
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
a = "http://dataquestio.github.io/web-scraping-pages/simple.html"

page = requests.get(a)
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

b= list(soup.children)
print(b)
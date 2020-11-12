import requests
from bs4 import BeautifulSoup

def scraping_data():    
    URL = ""
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())


    
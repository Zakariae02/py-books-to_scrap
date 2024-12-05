# partie_1.py
import requests
from bs4 import BeautifulSoup

def extraire_liens_livres_de_categorie(url_categorie):
    livres_donnees = []
    page_numero = 1
    while True:
        print(f"Scraping page {page_numero}...")
        reponse = requests.get(f'{url_categorie}?page={page_numero}')
        soup = BeautifulSoup(reponse.content, 'html.parser')
        liens_livres = soup.find_all('h3')
        if not liens_livres:
            break
        for livre in liens_livres:
            url_livre = livre.find('a')['href']
            url_complet = f'https://books.toscrape.com/{url_livre}'
            livres_donnees.append(url_complet)
        page_numero += 1
    return livres_donnees

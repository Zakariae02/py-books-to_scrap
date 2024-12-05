# partie_2.py
import requests
from bs4 import BeautifulSoup
import random
import string
import os

def generer_chaine_aleatoire(longueur=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=longueur))

def telecharger_image(url_image, nom_categorie):
    if not url_image.startswith('http'):
        url_image = 'https://books.toscrape.com' + url_image
    chaine_aleatoire = generer_chaine_aleatoire()
    nom_image = f'{nom_categorie}_{chaine_aleatoire}.png'
    chemin_image = os.path.join('images', nom_image)
    img_reponse = requests.get(url_image)
    if img_reponse.status_code == 200:
        with open(chemin_image, 'wb') as img_file:
            img_file.write(img_reponse.content)

def extraire_donnees_livre(url_livre):
    reponse = requests.get(url_livre)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    nom_categorie = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
    url_image = soup.find('img', {'src': True})['src'].strip()
    telecharger_image(url_image, nom_categorie)
    
    return {
        'url_livre': url_livre,
        'nom_categorie': nom_categorie,
        'url_image': url_image
    }

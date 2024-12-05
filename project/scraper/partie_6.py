# partie_6.py
import requests
import os

def telecharger_image_livre(url_image, nom_categorie):
    if not url_image.startswith('http'):
        url_image = 'https://books.toscrape.com' + url_image
    chaine_aleatoire = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    nom_image = f'{nom_categorie}_{chaine_aleatoire}.png'
    chemin_image = os.path.join('images', nom_image)
    reponse = requests.get(url_image)
    if reponse.status_code == 200:
        with open(chemin_image, 'wb') as f:
            f.write(reponse.content)

# partie_3.py
from partie_1 import extraire_liens_livres_de_categorie
from partie_2 import extraire_donnees_livre

def extraire_donnees_de_tous_les_livres():
    categories = ['http://books.toscrape.com/catalogue/category/books/science_22/index.html']
    toutes_les_donnees = []
    for categorie in categories:
        livres_liens = extraire_liens_livres_de_categorie(categorie)
        for lien in livres_liens:
            donnees_livre = extraire_donnees_livre(lien)
            toutes_les_donnees.append(donnees_livre)
    return toutes_les_donnees

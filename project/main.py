# main.py

# Importation de toutes les parties du projet
from scraper.partie_1 import extraire_liens_livres_de_categorie
from scraper.partie_2 import extraire_donnees_livre
from scraper.partie_3 import extraire_donnees_de_tous_les_livres
from scraper.partie_4 import sauvegarder_donnees_livres_csv
from scraper.partie_5 import creer_graphique_circulaire
from scraper.partie_6 import telecharger_image_livre
from scraper.bonus import visualiser_donnees_par_categorie

def main():
    # Partie 1 : Extraire les données d'un livre
    livre_donnees = extraire_liens_livres_de_categorie('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
    print("Données du livre extraites :", livre_donnees)
    
    # Partie 2 : Extraire les données d'une catégorie (par exemple, "Books")
    categorie_donnees = extraire_donnees_livre('http://books.toscrape.com/catalogue/category/books_1/index.html')
    print("Données de la catégorie extraites :", categorie_donnees)
    
    # Partie 3 : Extraire les données de tous les livres du site
    livres_donnees = extraire_donnees_de_tous_les_livres()
    print("Données de tous les livres extraites :", livres_donnees)
    
    # Partie 4 : Sauvegarder les données extraites dans un fichier CSV
    sauvegarder_donnees_livres_csv(livres_donnees)
    print("Données sauvegardées dans le fichier CSV.")
    
    # Partie 5 : Créer un graphique circulaire pour visualiser les données
    creer_graphique_circulaire()
    print("Graphique circulaire créé.")
    
    # Partie 6 : Télécharger les images de tous les livres
    telecharger_image_livre(livres_donnees)
    print("Images téléchargées.")
    
    # Bounus 7 : Visualiser les données par catégorie
    visualiser_donnees_par_categorie()
    print("Visualisation des données par catégorie effectuée.")

# Exécution du script
if __name__ == '__main__':
    main()

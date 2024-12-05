# partie_4.py
import csv

def sauvegarder_donnees_livres_csv(livres_donnees):
    with open('livres_par_categorie.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['url_livre', 'nom_categorie', 'url_image'])
        for livre in livres_donnees:
            writer.writerow([livre['url_livre'], livre['nom_categorie'], livre['url_image']])
    print("Données sauvegardées dans livres_par_categorie.csv")

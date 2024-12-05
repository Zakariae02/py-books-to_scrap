# partie_5.py
import matplotlib.pyplot as plt
import csv

def creer_graphique_circulaire():
    categorie_compte = {}
    
    with open('livres_par_categorie.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categorie = row['nom_categorie']
            if categorie not in categorie_compte:
                categorie_compte[categorie] = 0
            categorie_compte[categorie] += 1
    
    categories = list(categorie_compte.keys())
    comptes = list(categorie_compte.values())
    
    plt.figure(figsize=(10, 6))
    plt.pie(comptes, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Répartition des livres par catégorie')
    plt.show()

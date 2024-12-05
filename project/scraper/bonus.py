# visualisation.py
import csv
import matplotlib.pyplot as plt

def visualiser_donnees_par_categorie():
    categorie_data = {}
    
    with open('livres_par_categorie.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categorie = row['nom_categorie']
            if categorie not in categorie_data:
                categorie_data[categorie] = {'count': 0, 'total_price': 0}
            categorie_data[categorie]['count'] += 1
    
    for categorie, data in categorie_data.items():
        print(f"{categorie}: {data['count']} livres")

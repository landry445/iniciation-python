import csv

# 1. Extraction
def extraire(fichier):
    lignes = []
    with open(fichier, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # On saute l'en-tête
        for ligne in csv_reader:
            lignes.append(ligne)
    return lignes

# 2. Transformation
def transform(lignes_brutes):
    nouvelles_donnees = []
    for ligne in lignes_brutes:
        nom = ligne[0]
        # On calcule, on transforme en entier, puis en texte
        salaire = str(int(float(ligne[1]) * 15))
        nouvelles_donnees.append([nom, salaire])
    return nouvelles_donnees

# 3. Chargement
def load(nom_fichier, donnees_transformees):
    with open(nom_fichier, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Attention : les tests attendent des minuscules !
        writer.writerow(['nom', 'salaire'])
        writer.writerows(donnees_transformees)

# 4. Main
def main():
    nom_entree = 'input.csv'
    nom_sortie = 'output.csv'

    donnees = extraire(nom_entree)
    donnees_pretes = transform(donnees)
    load(nom_sortie, donnees_pretes)

if __name__ == "__main__":
    main()
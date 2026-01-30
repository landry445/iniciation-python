from statistics import mean

nombres = input("liste de nombres séparés par des virgules (par exemple : 1,2,3,4) : ")
print(nombres)

liste_de_nombres = nombres.split(',')

#boucle qui explique la l'index donc "e" et la valeur de l'élément liste_de_nombres
for e in range(len(liste_de_nombres)):
    print("index:", e, "valeur:", liste_de_nombres[e])


liste_entiers = []
for e in range(len(liste_de_nombres)):
  liste_de_nombres_entier = int(liste_de_nombres[e])
  liste_ajouter = liste_entiers.append(liste_de_nombres_entier)
  print(liste_entiers)

print(sum(liste_entiers))

moyenne = mean(liste_entiers)

print(moyenne)

for i in range(len(liste_entiers)):
    if liste_entiers[i] < moyenne:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    compte = i + 1
print(compte)

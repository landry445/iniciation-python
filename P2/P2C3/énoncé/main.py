# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
  resultat_salaire_mensuel = salaire_annuel / 12
  return resultat_salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
  resultat_salaire_hebdomadaire = salaire_mensuel / 4
  return resultat_salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  resultat_salaire_horaire = salaire_hebdomadaire / heures_travaillees
  return resultat_salaire_horaire

salaire_annuels = input("Saisissez votre salaire annuel : ")
resultat_mensuel = salaire_mensuel(float(salaire_annuels))
print(resultat_mensuel)

resultat_hebdomadaire = salaire_hebdomadaire(resultat_mensuel)
print(resultat_hebdomadaire)

heures_travaillees = input("Saisissez le nombre d'heures travaillées par semaine : ")
resultat_horaire = salaire_horaire(resultat_hebdomadaire, float(heures_travaillees))
print(resultat_horaire)





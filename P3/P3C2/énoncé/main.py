from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

title = soup.title.text
titre_h1 = soup.find(id="titre").text
print(title)
print(titre_h1)


catalogue_li = soup.select("li.produit")

produits = {}

def nettoyer_prix(prix):
    prix = prix.lower().split("(")[0]

    garde = ""
    for ch in prix:
        if ch.isdigit() or ch in ",.":
            garde += ch

    garde = garde.replace(",", ".")
    return float(garde) if garde else 0.0



for li in catalogue_li :
   nom_tag = li.select_one("h2.nom")
   prix_tag = li.select_one("p.prix")
   desc_tag = li.select_one("p.desc")
   stock_tag = li.select_one("span.stock")
   note_tag = li.select_one("span.note")

   nom = nom_tag.get_text(strip=True) if nom_tag else "INCONNU"
   prix = prix_tag.get_text(strip=True) if prix_tag else ""
   prix_eur = nettoyer_prix(prix )
   prix_usd = round(prix_eur * 1.2, 2)
   desc = desc_tag.get_text(strip=True) if desc_tag else ""
   stock = stock_tag.get_text(strip=True) if stock_tag else "stock: 0"
   note = note_tag.get_text(strip=True) if note_tag else " "
   categorie = li.get("data-categorie", "")

   produits[nom] = f"Le prix est de {prix_usd}$, {desc},  {stock}, {note}, {categorie}"

print(produits)




qte1 = input("Donner moi une première quantité : ")
qte2 = input("Donner moi une deuxième quantité : ")

if not qte1.isnumeric() or not qte2.isnumeric() :
  print("Ce ne sont pas des nombres entiers.")
  raise SystemExit("Fin du programme")

qte1 = int(qte1)
qte2 = int(qte2)

operation = input("Opération souhaitée (+, -, *, /) : ")

if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

match operation:
    case "+":
        resultat = qte1 + qte2
    case "-":
        resultat = qte1 - qte2
    case "*":
        resultat = qte1 * qte2
    case "/":
        if qte2 == 0 :
            print("Ne peut pas être diviser par 0")
            raise SystemExit("Fin du programme")
        resultat = round(qte1 / qte2, 2)
    case _:
        raise SystemExit("Fin du programme")

print(resultat)
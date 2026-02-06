contact = {"Alice":{"tel": "0612345678", "email": "alice@mail.com", "age": 23}}


def ajouter_contact(contacts, nom, tel, email, age):
  contacts[nom] = {"tel": tel, "email": email, "age": age}
  return contacts
print(ajouter_contact(contact,"Bob","0612345678","alice@mail.com",23))
print(contact)
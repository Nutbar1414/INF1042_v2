import random

def identité(nom, prénom, ville):
    return str(nom + "." + prénom + "@" + ville + ".ca")
print ("Ton identifiant est :" ,identité(nom = input("Nom :" ),
                                         prénom = input("Prénom :" ),
                                         ville = input("Ville :" )))

def passe(a, b, c, d, texte):
    (a, b, c, d) = list()
    random.choices(list())
    return list() + texte
print("ton mots de passe est :" ,passe(a = input("1er digit de ton annés de naissances :"),
                                       b = input("2e digit :"),
                                       c = input("3e digit :"),
                                       d = input("4e digit :"),
                                       texte = input("Svp entrer du texte courte :")))
#J'ai essayer :(




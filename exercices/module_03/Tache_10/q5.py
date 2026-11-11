import random
j_choix = "placeholder"
j_gagne = 0
c_gagne = 0
égalité = 0
totale = 0
choix = ("roche", "ciseaux", "papier")
#Le nombre de gagne, égalité et nombre totale de jeux

print("Bienvenue a roche papier cisseaux contre un ordie! Choisis roche, papier ou cisseaux pour jouer, ou tape quitter pour arreter le jeu.")

while j_choix not in "quitter":
    j_choix = str(input("roche, papier ou ciseaux? :"))
    c_choix = random.choice(choix)
    #Les choix de toi et l'ordi

    if j_choix == c_choix:
        print(f"L'ordi a choisi {c_choix}")
        print("Égalité!")

        égalité += 1
        totale += 1

    #Gére les égalité.

    elif j_choix == "roche" and c_choix == "ciseaux":
        print(f"L'ordi a choisi {c_choix}")
        print("Roche brise ciseaux! Gagner!")

        j_gagne += 1
        totale += 1

    elif j_choix == "roche" and c_choix == "papier":
        print(f"L'ordi a choisi {c_choix}")
        print("Papier couvre roche! Perdue!")

        c_gagne += 1
        totale += 1
    #Roche gagne et perde

    elif j_choix == "papier" and c_choix == "roche":
        print(f"L'ordi a choisi {c_choix}")
        print("Papier couvre roche! Gagner!")

        j_gagne += 1
        totale += 1

    elif j_choix == "papier" and c_choix == "ciseaux":
        print(f"L'ordi a choisi {c_choix}")
        print("Ciseaux coupe papier! Perdue!")

        c_gagne += 1
        totale += 1
    #papier gagne et perde
    #il y a tellement de elif

    elif j_choix == "ciseaux" and c_choix == "roche":
        print(f"L'ordi a choisi {c_choix}")
        print("Roche brise ciseaux! Perdue!")

        c_gagne += 1
        totale += 1

    elif j_choix == "ciseaux" and c_choix == "papier":
        print(f"L'ordi a choisi {c_choix}")
        print("Ciseaux coupe papier! Gagner!")

        j_gagne += 1
        totale += 1
    #Tout les possibilités sont maintenant finit (sauf deux)

    elif j_choix == "quitter":
        print(f"Jeux gagner: {j_gagne}")
        print(f"Jeux perdu: {c_gagne}")
        print(f"Égalité: {égalité}")
        print(f"Totale: {totale}")
        print("Adios!")

    else:
        print("INVALIDE. Essaye encore")
        print(j_choix)
        print(c_choix)
    #Maintenant c'est tout les possibilités
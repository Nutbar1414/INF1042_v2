nom = input("svp entrer votre nom (doit etre entre 8 et 12 caractéres) : ")
nom_len = len(nom)
if 8<=nom_len<=12:
    print(f"votre nom est {nom_len} caractére longue")
else:
    print("wowee votre nom est trop courte ou longue")

#jobnonathan = 11
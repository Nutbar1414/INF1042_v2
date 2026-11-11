prix_initiale = 4.00
prix_avant_rabais = 0
rabais_elec = 0.2 #20%
p_rabais_elec = 0
prix_totale = 0
#Les variables pour les calculs

v_elec = input("As-tu un voiture électrique (oui ou non) :")

temps = float(input("combien d'heure veut tu stationnais :"))
#Les input TM

if v_elec == "oui":
    prix_avant_rabais = prix_initiale + (2.50 * round(temps))

    p_rabais_elec = prix_avant_rabais * rabais_elec

    totale = prix_avant_rabais - p_rabais_elec
    #Les calculs TM

    print("Heures facturé :",round(temps))
    print("Prix avant rabais :",round(prix_avant_rabais, 2),"$")
    print("Rabais électrique :",round(p_rabais_elec, 2),"$")
    print("Totale :",round(totale, 2),"$")

elif v_elec == "non":
    prix_avant_rabais = prix_initiale + (2.50 * round(temps))

    totale = prix_avant_rabais

    print("Heures facturé :", round(temps))
    print("Prix avant rabais :", round(prix_avant_rabais, 2), "$")
    print("Totale :", round(totale, 2), "$")


import random

gagnant_1 = 0
gagnant_2 = 0
gagnant_3 = 0
gagnant_4 = 0

tirages = int(input("combien de tirage souhaite tu faires :"))
#input pour choisir combien de fois tu veux simuler le tirages

for i in range(0, tirages):
    gagnant = random.choice([1,2,3,4])
    if gagnant == 1:
        gagnant_1 += 1

    elif gagnant == 2:
        gagnant_2 += 1

    elif gagnant == 3:
        gagnant_3 += 1

    elif gagnant == 4:
        gagnant_4 += 1
        #Quand le gagnant egale un des nombres, + 1 est ajouter a sa variable respective. GAMBLING

pourcent = tirages / 100
#Divise le nombre de tirage par 100 pour trouver le valeur de 1% pour diviser les gagnant(1,2,3,4)

gagnant_1p = gagnant_1 / pourcent
gagnant_2p = gagnant_2 / pourcent
gagnant_3p = gagnant_3 / pourcent
gagnant_4p = gagnant_4 / pourcent
#calcule les pourcentage de tout les valeurs

print(f"1: {gagnant_1} 2: {gagnant_2} 3: {gagnant_3} 4: {gagnant_4}")
#Print les valeurs.
print(f"pourcentage de: 1: {gagnant_1p}% 2: {gagnant_2p}% 3: {gagnant_3p}% 4: {gagnant_4p}%")
#affiche les pourcentage de tout les gagnants.

if gagnant_1 > gagnant_2 and gagnant_1 > gagnant_3 and gagnant_1 > gagnant_4:
    print(f"1 est le gagnant avec {gagnant_1} tire!")

elif gagnant_2 > gagnant_1 and gagnant_2 > gagnant_3 and gagnant_2 > gagnant_4:
    print(f"2 est le gagnant avec {gagnant_2} tire!")

elif gagnant_3 > gagnant_1 and gagnant_3 > gagnant_2 and gagnant_3 > gagnant_4:
    print(f"3 est le gagnant avec {gagnant_3} tire!")

elif gagnant_4 > gagnant_1 and gagnant_4 > gagnant_2 and gagnant_4 > gagnant_3:
    print(f"4 est le gagnant avec {gagnant_4} tire!")
#Decide le vraie gagnant et montre le nombre de tire encore

#parier sur un des nombres comme un chevaux dans un course de chevaux

math_check = gagnant_1p + gagnant_2p + gagnant_3p + gagnant_4p
if not math_check == 100:
    print("NOOOOOOOOOON! MON PRECIEUSE COOOODE! (EXPLOSION!!!!!!!!) AAAAAAAAAAAAHHHH!")
#Check le math :)


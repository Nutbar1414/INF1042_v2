import random

options = ("roches", "papier", "cisseaux")

choix = random.choice(options)

choix_2 = input("choisis roches, papier ou cisseaux : ")

if (choix_2 == choix):
    print("Égalité!")
else:
    print("Choix différente!")
#J'ai vu quelque pars que les ordinateurs n'aimes pas choisir des option aléatoire

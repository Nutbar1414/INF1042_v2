rabais_1 = 0.05
rabais_texte_1 = "5%"
rabais_2 = 0.10
rabais_texte_2 = "10%"
taxe = 0.13
taxe_texte = "13%"
finale = 0

def montant(initial):

    if initial <= 50 :
        finale = (initial * taxe) + initial
        round(finale, 2)
        #Aucun rabais, just taxe (13%)
        econo = ((initial * taxe) + initial) - finale
        round(econo, 2)
        #Calcule le montant économisé entre le prix finale et le prix initial + taxe
        rabais = "aucun rabais"

    elif 50 < initial < 100 :
        finale = (initial - (initial * rabais_1)) * taxe + (initial - (initial * rabais_1))
        round(finale, 2)
        #Rabais de 5%. what a deal!
        econo = ((initial * taxe) + initial) - finale
        round(econo, 2)

        rabais = rabais_texte_1

    elif 100 < initial :
        finale = (initial - (initial * rabais_2)) * taxe + (initial - (initial * rabais_2))
        round(finale, 2)
        #Rabais de 10% WOWOWOWOW!
        econo = ((initial * taxe) + initial) - finale
        round(econo, 2)

        rabais = rabais_texte_2

    return initial, finale, econo, rabais

print("Le prix initial, le prix finale, le montant économiser et le rabais sont :" ,montant(initial = float(input("Svp entrer le montant payer :"))))

print(f"le taxe payer est {taxe_texte}")



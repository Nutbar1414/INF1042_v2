with open('valeurs.txt', 'r', encoding='utf-8') as f:

    with open('bas.txt', 'w', encoding='utf-8') as f2:
        for ligne in f:
            v = int(ligne)
            if 0 <= v <= 49999:
                f2.write(f'{v}\n')

with open('valeurs.txt', 'r', encoding='utf-8') as f:

    with open('haut.txt', 'w', encoding='utf-8') as f3:
        for ligne in f:
            v = int(ligne)
            if 50000 <= v <= 100000:
                f3.write(f'{v}\n')
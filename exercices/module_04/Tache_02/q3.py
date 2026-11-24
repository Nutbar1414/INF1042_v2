with open('valeurs.txt', 'r', encoding='utf-8') as f:

    for ligne in f:

        v = int(ligne)
        if 0 <= v <= 49999:
            with open('bas.txt', 'w', encoding='utf-8') as b:
                b.write(f'{v}\n')

        if 50000 <= v <= 100000:
            with open('haut.txt', 'w', encoding='utf-8') as c:
                c.write(f'{v}\n')
            
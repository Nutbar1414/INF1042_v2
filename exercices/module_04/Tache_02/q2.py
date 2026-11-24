with open('valeurs.txt', 'r', encoding='utf-8') as f:
    max = (0)
    min = (100000)
    for ligne in f:
        v = float(ligne)
        if v > max:
            max = v
        if v < min:
            min = v
print(f"le max est {max} et le min est {min}")
#Fait amusante: le terme "yo" vient du celebration romain "io saturnalia", le "io" est


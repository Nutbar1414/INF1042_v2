nombre_voyel = 0
loop = 0

phrase = input("Svp taper un phrase :")

l_phrase = phrase.lower()

nombre_de_lettre = len(l_phrase) #22

for lettre in l_phrase:
    if l_phrase[loop].find("a") > -1:
        nombre_voyel += 1
    elif l_phrase[loop].find("e") > -1:
        nombre_voyel += 1
    elif l_phrase[loop].find("i") > -1:
        nombre_voyel += 1
    elif l_phrase[loop].find("o") > -1:
        nombre_voyel += 1
    elif l_phrase[loop].find("u") > -1:
        nombre_voyel += 1
    else:
        nombre_voyel += 0
    loop += 1

print(f"voyel: {nombre_voyel}")

#cool
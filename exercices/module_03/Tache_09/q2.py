import time
import random

i = input("combien de question veut tu répondre :")
score = 0

for i in range(0, int(i)):
    a = random.randint(1, 12)
    b = random.randint(1, 12)

    réponse = a * b
    début = time.time()
    quéstion = int(input(f"{a}x{b} ="))
    fin = time.time()
    temps_finale = fin - début

    if réponse == quéstion:
        print(f"Bonne réponse! le temps pour répondre au question est {temps_finale}")
        score = score + 1

    else:
        print(f"mauvaise réponse, le temps pour répondre au question est {temps_finale}")
        print(réponse)
        score = score - 1


print("Score finale est :" ,score,)

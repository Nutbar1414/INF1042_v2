phrase = input("Svp entrer un phrase :")

s_phrase = phrase.split(" ")
n_phrase = len(s_phrase)
re_phrase = "-".join(s_phrase)

print(f"Le nombre de mot est {n_phrase}.")
print(f"Le liste est {s_phrase}.")
print(f"Le liste recombiner est {re_phrase}.")

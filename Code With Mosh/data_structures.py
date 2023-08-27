"""numbers = [1,2,3,4,4,4,4,9]
first, *other, last = numbers
print(first, last)
print(other)"""


"""numbers = [3,51,2,8,6]
#numbers.sort(reverse=False)
print(sorted(numbers))
print(numbers)"""

"""sentence = "This is a common interview question"
# On transforme la phrase en minuscules pour éviter les problèmes de casse
sentence = sentence.lower()
# On initialise un dictionnaire vide pour stocker les occurrences de chaque lettre
occurrences = {}

# On parcourt chaque caractère de la phrase
for char in sentence:
    # On ne prend en compte que les lettres de l'alphabet
    if char.isalpha():
        # Si la lettre n'a pas encore été rencontrée, on l'ajoute au dictionnaire avec une occurrence de 1
        if char not in occurrences:
            occurrences[char] = 1
        # Sinon, on incrémente le nombre d'occurrences de cette lettre
        else:
            occurrences[char] += 1

# On trouve la lettre la plus utilisée en triant le dictionnaire par ordre décroissant d'occurrences et en prenant la première clé
most_common_letter = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)[0][0]

print("La lettre la plus utilisée est :", most_common_letter)
"""
"""sentence = "This is a common interview question"

# compter les occurrences de chaque lettre
occurrences = {}
for letter in sentence:
    if letter in occurrences:
        occurrences[letter] += 1
    else:
        occurrences[letter] = 1

# trouver la lettre la plus utilisée
most_common_letter = None
max_occurrences = 0
for letter, count in occurrences.items():
    if count > max_occurrences:
        most_common_letter = letter
        max_occurrences = count

# afficher la lettre la plus utilisée et son nombre d'occurrences
print(f"La lettre la plus utilisée dans la phrase est '{most_common_letter}' avec {max_occurrences} occurrences.")
"""

from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse = True)
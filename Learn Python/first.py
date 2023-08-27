"""
import random
chiffre_secret = random.randint(0, 100)
reponse = None
while reponse != chiffre_secret:
    reponse = int(input("Entrez un chiffre entre 0 et 100 🔁 : " ))
    if reponse > chiffre_secret:
        print("❌ Le chiffe secret est plus petit que ça ↘️")
    elif reponse < chiffre_secret:
        print("❌ Le chiffre secret est plus grand que ça ↗️")
    else:
        print("🥳 Bravo 👏 vous avez trouvé 🎉🎉🎉!, le chiffre secret est :", reponse )
"""
"""couleurs = []
reponse = None
while reponse != "stop":
    reponse = input ("Entrez le nom de vos couleurs préférées : ")
    couleurs.append(reponse)
print("Vos couleurs préférées sont :", couleurs)"""

'''year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
'''
n = int(input("Veuillez inserer le numéro"))

i=1

S=0

while i<=n :

    S= float(S + 1/i);

    i=i+1

print(format(S,".2f"))
"""import math
Rayon = float(input("Veuillez saisir la valeur du rayon du cercle : "))
Surface = math.pow(Rayon, Rayon) * 3.14
print("L'aire de cercle est : ", Surface,"Mètre Carré")"""
"""
produit_vendus = int(input("Veuillez saisir la quantité du produit : "))
prix_vente = float(input("Veuillez entrer le prix de vente : "))
CA = produit_vendus * prix_vente
print("Le chiffre d'affaire de l'entreprise est : ",CA, "Francs CFA")"""

"""print("Programme qui détermine la nature d'un nombre.")
n = int(input("Veuillez saisir un nombre : "))
if n > 0:
    print("Ce nombre est positif 🎉🥳")
elif n < 0:
    print("Ce nombre est négatif 🔴😡")
else:
    print("Ce nombre est Nul")"""

"""print("Déterminer la valeur de la temperature 🤒 de l'eau 💧:")
Temperature = int(input("Entrez la valeur de la temperature 🤒 : "))
if Temperature > 100:
    print("L'état de l'eau est VAPEUR 🌨 ")
elif 0 < Temperature < 100:
    print("L'état de l'eau est LIQUIDE 💧 ")
else:
    print("L'état de l'eau est GLACE 🥶 ")"""
    
"""print("Les jours de la semaine entre 1 et 7.")
chiffre = int(input("Veuillez entrer un chiffre correspondant au jour de la semaine 📆 entre 1 et 7 : "))
if chiffre == 1:
    print("1️⃣ - Lundi")
elif chiffre == 2:
    print("2️⃣ - Mardi")
elif chiffre == 3:
    print("3️⃣ - Mercredi")
elif chiffre == 4:
    print("4️⃣ - Jeudi")
elif chiffre == 5:
    print("5️⃣ - Vendredi")
elif chiffre == 6:
    print("6️⃣ - Samedi")
elif chiffre == 7:
    print("7️⃣ - Dimanche")
else:
    print("⚠️Le chiffre que vous avez saisir est incorrect.")"""

"""a = int(input("Veuillez entrer la valeur de a : "))
b = int(input("Veuillez entrer la valeur de b : "))
if a > b:
    max = a
else:
    max = b
print("Le maximun est : ", max)"""
"""
print("La table de multiplication  par 7️⃣.")
for i in range (11):
    multiplication = 7 * i
    print("7 x", i, "=", multiplication)"""
"""n = int(input("Veuillez saisir un nombre : "))
S = 0    
for i in range(1, n + 1):
    S =S + i
print("La somme des 20 premiers entiers positifs est : ",S)"""

"""for i in range(1, 11):
    for j in range(1, 11):   
        multiplication = new_func(i, j) 
    print(i, "x", j, "=", multiplication)"""
    
"""Ligne  = int(input("Veuillez saisir le nombre de lignes : "))
Colonne  = int(input("Veuillez saisir le nombre de colonnes : "))
for i in range(Ligne):
    for j in range(Colonne):
        print("1️⃣ ", "2️⃣", end=" ")
    print()"""

"""nombre = int(input("Veuillez saisir un nombre : "))
while nombre < 1 or nombre > 10:
    nombre = int(input("⚠️ Désolé ce nombre est incorrect, veuillez saisir un nombre correct : "))
i = 0
while i <= 10:
    multiplication = nombre * i
    print(nombre, "x", i, "=", multiplication)
    i = i + 1"""
    
"""nombre = int(input("Veuillez saisir un nombre entre 10 et 20 : "))
while nombre < 10 or nombre > 20:
    if nombre < 10:
        print("Plus petit que", nombre)
    else:
        print("Plus grand que", nombre)
    nombre = int(input("Désolé ⚠️, veuillez entrer un nombre entre 10 et 20 : "))
print("Bravo 🎉! vous avez saisir un nombre compris entre 10 et 20")"""

"""nombre = int(input("Entrez un nombre : "))
while nombre <= 1:
    nombre = int(input("Désolé ⚠️ , veuillez entrer un nombre positif s'il vous plaît : "))
somme = 0
i = 1
while i <= nombre:
    somme = somme + i
    i = i + 1
print("La somme est : ", somme)"""

"""chiffre = 0
for i in range(1,9):
    print("Entrez N", i, " : ", end="")
    nombre = int(input())
    if nombre < 0:
        break
    chiffre = chiffre + nombre
print("La somme est : ", chiffre)"""

"""chiffre = 0
for i in range(1,9):
    print("Entrez N", i, " : ", end="")
    nombre = int(input())
    if nombre < 0:
        continue
    chiffre = chiffre + nombre
print("La somme est : ", chiffre)"""

"""def bonjour(nom):
    nom = input("Veuillez saisir votre nom de famille :")
    print("Bonjour",nom,"!")
bonjour(nom=print)"""

"""def soustraction(A,B):
    C = A - B
    print("A - B =", C)
A = float(input("Saisir la valeur de A : "))
B = float(input("Saisir la valeur de B : "))

soustraction(A,B)"""

"""def signe(A,B):
    if A*B > 0:
        print("Les valeurs de A et B ont le même signe.")
    else:
        print("Les valeurs de A et B ont deux signes differents.")

def maximum(A,B):
    m = 0
    if A > B:
        return A
    else:
        return B

def  minimum(A,B):
    m = 0
    if A < B:
        return A
    else:
        return B

# L'appel des fonctions 

A = int(input("Veuillez saisir la valeur de A : "))
B = int(input("Veuillez saisir la valeur de B : "))
signe(A,B)
print("La valeur minimal est ", minimum (A,B))
c = maximum(A,B)
print("La valeur maximale est ",c)
"""
"""y = 4
def afficher():
    y = 8
    print(y)
afficher()
print(y)
"""
"""def soustraction(A,B):
    C = A - B
    print("le resultat de : A - B =", C)
A = float(input("Saisir la valeur de A : "))
B = float(input("Saisir la valeur de B : "))
soustraction(B,A)"""

import random

options = ("rock", "paper", "scissors")
running = True
playerScore = 0
computerScore = 0

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        #print("Player Score :"+str(playerScore =+ 1))
        #print("Computer Score :"+str(computerScore = computerScore + 1))
        
    elif player == "rock" and computer == "scissors":
        print("You win!")
        print("Player Score :"+str(playerScore = playerScore + 1))
    elif player == "paper" and computer == "rock":
        print("You win!")
        print("Player Score :"+str(playerScore = playerScore + 1))
    elif player == "scissors" and computer == "paper":
        print("You win!")
        print("Player Score :"+str(playerScore = playerScore + 1))
    else:
        print("You lose!")
        print("Player Score :"+str(playerScore = playerScore + 1))
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
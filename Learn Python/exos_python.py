"""def signe(a,b):
    if a * b > 0:
        print("a et b ont le même signe")
    else:
        print("a et b ont deux signes differents")
def maximum(a,b):
    if a > b:
        print("Le maximum est : ", a)
    else:
        print("Le maximum est : ", b)
def minimum(a,b):
    if a < b:
        print("Le maximum est : ", a)
    else:
        print("LE minimum est : ", b)"""
"""N1 = float(input("Veuillez entrer la note N1 : "))
N2 = float(input("Veuillez entrer la note N2 : "))
N3 = float(input("Veuillez entrer la note N3 : "))
N4 = float(input("Veuillez entrer la note N4 : "))
N5 = float(input("Veuillez entrer la note N5 : "))
Sm = N1 + N2 + N3 + N4 + N5
Mo = Sm / 5 
print("La sommes des notes est : ",Sm)
print("La moyenne des notes est : ",Mo)
print(f"La sommes des notes est : {Sm}")
print(f"La moyenne des notes est : ",format(Mo,".2f"))"""
"""R = float(input("Veuillez saisir le Rayon svp : "))
D = 4 * 3.14 * R ** 3
Vo = D / 3
print(format(Vo,".2f"))
"""
"""T = int(input("Veuillez saisir la durée en seconde : "))
H = T // 3600
R = T % 3600
M = R // 60
S = R % 60
print(H,"H:",M,"m:",S,"s")"""
"""import math
Xa = float(input("Veuillez saisir le cordonnée de X de A : "))
Xb = float(input("Veuillez saisir le cordonnée de X de B : "))
Ya = float(input("Veuillez saisir le cordonnée de Y de A : "))
Yb = float(input("Veuillez saisir le cordonnée de Y de B : "))
AB = (Xb-Xa)**2 + (Yb-Ya)**2
AB = math.sqrt(AB)
print("La distance entre les deux points A et B est : ",format(AB,".2f"),"M")"""

#Exos N° 13
"""A = int(input("Entrer la valeur de A : "))
B = int(input("Entrer la valeur de B : "))
if A*B > 0:
    A,B=B,A
else:
    C = A + B
    D = A * B
    A = C
    B = D
print("La nouvelle valeur de A est : ",A)
print("La nouvelle valeur de B est : ",B)"""

#Exos N° 14
"""Np = int(input("Veuillez entrer le nombre de photocopie à éffectuer : "))
if Np < 10:
    Fact = 10 * 15
elif Np < 30:
    Fact = 10 * 0.3 + (Np-10)*25
else:
    Fact = 10 * 0.3 + 20 * 0.25 + (Np-30)*20      
print("Votre facture est : ",Fact,"Frcs CFA")"""

#Exos 15
"""
age = int(input("Veuillez saisir l'âge l'enfant : "))
if age >= 6 and age <= 7:
    print("La catégorie de l'enfant est POUSSIN")
elif age >= 8 and age <= 9:
    print("La catégorie de l'enfant est PUPILLE")
elif age >= 10 and age <= 11:
    print("La catégorie de l'enfant est MINIME")
elif age >= 12 and age <= 16:
    print("La catégorie de l'enfant est CADET")
else:
    print("Désolé,cette catégorie n'est pas referencé")"""
#Exos N° 16
"""N1 = float(input("Veuillez saisir N1 : "))
N2 = float(input("Veuillez saisir N2 : "))
N3 = float(input("Veuillez saisir N3 : "))
Mo = (N1+N2+N3)/3
print("La moyenne de l'étudiant est : ", format(Mo,".2f"))
if Mo < 10:
    print("La mention de l'étudiant est : Insuffisant 😪")
elif Mo >= 10 and Mo < 12:
    print("La mention de l'étudiant est : Passable 😊")
elif Mo >= 12 and Mo < 14:
    print("La mention de l'étudiant est : Assez Bien 😗")
elif Mo >= 14 and Mo < 16:
    print("La mention de l'étudiant est bien : Bien 🥳")
else:
    print("La mention de l'étudiant est : Très Bien 👏")"""
#Exos N° 17
"""import math
a = float(input("Veuillez saisir la valeur de a : "))
b = float(input("Veuillez saisir la valeur de b : "))
c = float(input("Veuillez saisir la valeur de c : "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Pas de solution réelles")
elif delta == 0 :
    x = (-b)/(2*a)
    print("La solution est : ",x)
else:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("Les solutions sont : ",format(x1,".2f"), " et ",format(x1,".2f"))"""
#Exos N° 18
"""sexe = input("Veuillez entrer le sexe de l'habitant (H/F) : ")
age = int(input("Veuillez entrer l'âge de l'habitant : "))
if ((sexe == "H" and age >= 20) or (sexe == "F" and age >= 18 and age <=35)):
    print("L'habitant est imposable 🤑 ")
else:
    print("L'habitant est non imposable 😏 ")"""
#Exos N°19
'''Pr = float(input("Veuillez le prix hors taxe : "))
Ca = input("Veuillez saisir la catégorie : ")
if Ca == "A":
    print("Le prix PTTC de la Catégorie A est : ","Frcs CFA",Pr+Pr*0.07)
elif Ca == "B":
    print("Le prix PTTC de la Catégorie B est : ","Frcs CFA",Pr+Pr+0.2)
elif Ca == "C":
    print("Le prix PTTC de la Catégorie C est : ","Frcs CFA",Pr+Pr+0.25)
else:
    print("Désolé la catégorie n'existe pas")
    '''
#Exos N° 20
'''A = float(input("Veuillez saisir la valeur de A : "))
B = float(input("Veuillez saisir la valeur de B : "))
Op = input("Veuillez saisir l'operateur : ")
if Op == "+":
    print("Le resultat de l'addition 🅰️  ➕ 🅱️  est : ", A+B)
elif Op == "-":
    print("Le resultat de la soustraction 🅰️ ➖ 🅱️  est : ", A-B)
elif Op == "*":
    print("Le resultat de la multiplication 🅰️ ✖️ 🅱️  est : ", A*B)
elif Op == "/":
    if B != 0 :
        print("Le resultat de la division  🅰️  ➗ 🅱️  est : ", A/B)
    else :
        print(" ⚠️ La division par 0 est impossible")'''
#Exos N° 21
'''Nombre = float(input("Veuillez saisir un nombre entre 0️⃣  et  9️⃣  : "))
if Nombre == 6:
    print("Le personnage vas à droite  ➡️  ")
elif Nombre == 4:
    print("Le personnage vas à gauche  ⬅️  ")
elif Nombre == 8:
    print("Le personnage vas en haut  ⬆️  ")
elif Nombre == 2:
    print("Le personnage vas en bas  ⬇️  ")
else:
    print("  ⚠️  Erreur de saisir le personnage ne bouge pas ")'''
#Exos N° 22
'''Nombre = int(input("Veuillez saisir un nombre : "))
reste = Nombre % 2
if reste == 0:
    print(Nombre, "est pair")
else:
    print(Nombre, "est impair")
'''
#Exos N° 23
'''Annee = int(input("Veuillez saisir une année :"))
if (Annee % 4 == 0 or Annee % 400 == 0) and (Annee % 100 != 0):
    print(Annee, "est une Année Bissextile")
else:
    print(Annee, " n'est pas une Année Bissextile")'''
#Exos N°24
'''caractere = input("Veuillez saisir le caractère : ")
if "a"<= caractere <= "z" or "A"<= caractere <= "Z":
    print(caractere," est une lettre de l'alphabet")
elif "0" <= caractere <= "9":
    print(caractere," est un chiffre")
else:
    print(caractere," est un caractere spéciale")'''
#Exos N°25
'''N  = int(input("Veuillez siaisr un nombre : "))
for i in range(N+1, N+11):
    print(i)'''
#Exos N°26
'''N  = int(input("Veuilez saisir un nombre : "))
i = N + 2
while i <= N + 10:
    print(i,end=" ")
    i = i + 2'''
#Exos N°27
'''n =int(input("Veuillez saisir la valeur de n : "))
S = 0
for i in range(1, n+1):
    S = S + 1/i
print("La somme est : ",format(S,".2f"))
i = 1
while i < n + 1:
    S = S + 1/i
    i+=1
print("La somme est : ",format(S,".2f"))'''
#Exos N°28
'''n = int(input("Veuillez saisir la valeur de n : "))
S = 0 
for i in range(0,n+1):
    S = S + (10 ** i)
i = 0
while i < n+1:
    S = S + (10 ** i)
    i+=1
print("La sommes de la serie est : ",S)'''
#Exos N°29
'''n = int(input("Veuillez saisir un nombre : "))
S = 0
J = 1
for i in range(n):
    S = S + (J ** 2)
    J = J + 2
print("La sommes des nombres impaires est : ", S) '''
#Exos N°31
'''n = int(input("Veuillez saisir la valeur de n : "))
while n <= 0:
    n = int(input("Veuillez saisir la valeur de n : "))
print("Les diviseurs de ",n," sont : ")
for i in range(1,n+1):
    if (n % i == 0):
        print(i)'''
#Exos N°32
'''age = int(input("Veuillez saisir l'age d'Amal : "))
S = 0
for i in range(1,age+1):
    S = S + (5000 + (i * 3))
print("Le compte d'Amal au",age,"ième anniversaire est : ",S,"Francs CFA")'''
#Exos N°33
'''nbr_ans = int(input("Veuillez saisir le nombre d'années : "))
p_dla = 500000
p_yde = 1000000
#nbr_ans = 0
while p_yde > p_dla:
    p_dla = p_dla*1.08
    p_yde = p_yde + 50000
    nbr_ans = nbr_ans + 1
    print("Douala dépassera Yaoundé après ",nbr_ans,"ans")'''
'''n = int(input("Veuillez entrer le nombre d'équipes : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            print("Equipe",i,"VS Equipe",j)'''
#Exos N°38
'''import random
n = random.randint(1,30)
nbre_tentatives = 5
while nbre_tentatives > 0:
    nbre_tentatives -= 1
    nbre = int(input("Saisir un nombre magique : "))
    if nbre < n:
        print("Désolé, le nombre magique est grand  😪  que : ",nbre)
    elif nbre > n:
        print("Désolé, Le nombe magique est petit   🙃  que : ",nbre)
    else:
        print("Bravo  🎉  , vous avez trouver le nombre magique : ",nbre)
    
    if nbre != n:
        print("Attention  ⚠️  ! il vous reste ",nbre_tentatives,"essais")
    else:
        print("Oups  🔴  ! vous avez dépassé les 5 tentatives autorisées. Le nombre magique était :",n)    '''
#Exos N°39
'''while True :
    print("-----  ⚙️  Calculatrice  -  MENU  -----")
    print("  1️⃣  - Addition")
    print("  2️⃣  - Soustraction")
    print("  3️⃣  - Multiplication")
    print("  4️⃣  - Division")
    print("  5️⃣  - Reste de la division entiere (Modulo)")
    print("  6️⃣  - Puissance")
    operation = int(input("Quel calcul veux-tu effectuer ? "))
    A = int(input("Saisir le 1er terme : "))
    B = int(input("Saisir le 2e terme : "))
    if operation == 1:
        print("Le resultat est : ",A+B)
    elif operation == 2:
        print("Le resultat est : ",A-B)
    elif operation == 3:
        print("Le resultat est : ",A*B)
    elif operation == 4:
        if B != 0:
            print("Le resultat est : ",A/B)
        else:
            print("La division par 0 est impossible")
    elif operation == 5:
        if B != 0:
            print("Le resultat est : ",A/B)
        else:
            print("Le modulo par 0 est impossible")
    elif operation == 6:
        if B != 0:
            print("Le resultat est : ",A**B)
        else:
            print("Le resultat impossible")
    reponse = input("Veux-tu faire un autre calcul (O/N) ? : ")
    if reponse == "N":
        print("Aurevoir et à bientôt  ✋  ")
        break'''
#Exos N°40
'''import random
nom = input("Veuillez saisir votre nom  : ")
user_victories = 0
pc_victories = 0
nuls = 0
while True:
    coup_joueur = input("Entrez votre coup : (p)ierre,(f)euille,(c)iseaux ou (q)uitter : ")
    if coup_joueur == "q":
        print("Vous avez quittéle jeu, à bientôt  🤚  ")
        break
    if coup_joueur != "p" and coup_joueur != "f" and coup_joueur != "c" :
        continue
    if coup_joueur == "p":
        print("PIERRE 🆚 ... ",end=" ")
    elif coup_joueur == "f":
        print("FEUILLE 🆚 ... ",end=" ")
    else:
        print("CISEAUX 🆚 ... ",end=" ")

randonNombre = random.randint(1, 3)
if randonNombre == 1:
    coupPC = "p"
    print("PIERRE")
elif randonNombre == 2:
    coupPC = "f"
    print("FEUILLE")
else:
    coupPC = "c"
    print("CISEAUX")

if coup_joueur == coupPC:
    print("Partie est nulle !")
    nuls = nuls + 1
elif coup_joueur == "p" and coupPC == "c":
    print("Bravo  🎉  , vous avez gagné !")
    user_victories = user_victories + 1
elif coup_joueur == "f" and coupPC == "p":
    print("Bravo  🎉  , vous avez gagné !")
    user_victories = user_victories + 1
elif coup_joueur == "c" and coupPC == "f":
    print("Bravo  🎉  , vous avez gagné !")
    user_victories = user_victories + 1
#elif coup_joueur == "c" and coupPC == "f":
    print("Bravo  🎉  , vous avez gagné !")
    user_victories = user_victories + 1
elif coup_joueur == "p" and coupPC == "f":
    print("Dommage  🔴  , vous avez perdu !")
    pc_victories = pc_victories + 1
elif coup_joueur == "f" and coupPC == "c":
    print("Dommage  🔴  , vous avez perdu !")
    pc_victories = pc_victories + 1
elif coup_joueur == "c" and coupPC == "p":
    print("Dommage  🔴  , vous avez perdu !")
    pc_victories = pc_victories + 1'''

'''import random
nom = input("Veuillez saisir votre nom : ")
user_victoires = 0
pc_victoires = 0
nuls = 0

while True:
    print(nom," : ",user_victoires,"  égalités : ",nuls,"  PC : ", pc_victoires)
    coupJoueur = input("Entrez votre coup : (p)ierre, (f)euille, (c)iseaux ou (q)uitter : ")
    if coupJoueur == "q":
        print("Vous avez quitté le jeu")
        break
    
    if coupJoueur != "p" and coupJoueur != "f" and coupJoueur != "c" :
        continue
    
    if coupJoueur == "p":
        print("PIERRE contre ...",end=" ")
    elif coupJoueur == "f":
        print("FEUILLE contre ...",end=" ")
    else:
        print("CISEAUX contre ...",end=" ")
    
    randomNombre = random.randint(1,3)
    if randomNombre == 1:
        coupPC = "p"
        print("PIERRE")
    elif randomNombre == 2:
        coupPC = "f"
        print("FEUILLE")
    else:
        coupPC = "c"
        print("CISEAUX")
        
    if coupJoueur == coupPC :
        print("Partie est nulle !")
        nuls = nuls + 1
    elif coupJoueur == "p" and coupPC == "c":
        print("Vous avez gagné !")
        user_victoires = user_victoires + 1
    elif coupJoueur == "f" and coupJoueur == "p":
        print("Vous avez gagné !")
        user_victoires = user_victoires + 1
    elif coupJoueur == "c" and coupJoueur == "f":
        print("Vous avez gagné !")
        user_victoires = user_victoires + 1
    elif coupJoueur == "p" and coupPC == "f":
        print("Vous avez perdu !")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "f" and coupPC == "c":
        print("Vous avez perdu !")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "c" and coupPC == "p":
        print("Vous avez perdu !")
        pc_victoires = pc_victoires + 1'''
#Exos N°46
'''n = int(input("Veuillez saisir un nombre : "))
b = 0
ord = 0
while n != 0 :
    reste = n % 2
    p = 10 ** ord
    b = b + reste * p
    ord = ord + 1
    n =n // 2
print(b)'''
#Exos N°47
'''lignes = int(input("Veuillez saisir le nombre de lignes : "))
for i in range(1,lignes+1):
    for j in range(i):
        print("* ", end="")
    print("")'''
#Exos N°48
'''ligne = int(input("Veuillez saisir le nombre de lignes : "))
colonne = int(input("Veuillez saisir le nombre de colonnes : "))
for i in range(1, ligne+1):
    for j in range(1,colonne+1):
        if i == 1 or i == ligne or j == 1 or j == colonne:
            print("* ",end="")
        else:
            print(" ",end="")
    print()'''
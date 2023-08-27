# Les variables de bases

premier_nombre = 13 # int - nombre entier
deuxieme_nombre = 32.54 # float - nombre decimale

premier_texte = 'Hello world' #str - chaine de caractere
deuxieme_texte = "Aujourd'hui" # str

premier_booleen = True # bool - valeur booléenne qui contiens l'une des deux valeurs vrai/faux
deuxieme_booleen = False # bool

# Les conversions 
nombre_decimal = 12.43
nombre_entier = int(nombre_decimal)
nombre_decimal_2 = float(nombre_entier)

nombre_en_texte = "12"
nombre_entier_2 = int(nombre_en_texte)

nombre_decimal_en_texte = f"{nombre_decimal} est ton nombre"

# Lire une valeur entrée par l'utilisateur
valeur_utilisateur_1 = int(input("Entrez un 1er nombre: "))
valeur_utilisateur_2 = int(input("Entrez un 2e nombre: "))
somme_valeurs = valeur_utilisateur_1 + valeur_utilisateur_2

print(f"{valeur_utilisateur_1} + {valeur_utilisateur_2} = {somme_valeurs}")


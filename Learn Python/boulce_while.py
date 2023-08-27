import random 

# 1. Choisir un nombre au hazar
juste_prix = random.randint(0,100)
estimation = -1
abandon = False

# 2. Tant que l'utilisateur n'a pas trouvé le bon nombre
while estimation != juste_prix:
    
    # 2.1 Demander un nombre a l'utilisateur
    instruction = input("Quelle est votre estimation ou [Q: Quitter] : ")
    if not instruction.isdigit():
        if instruction.upper() == "Q":
            abandon = True
            break
        else:
            print("Veuillez entrer un nombre ou la lettre 'Q' pour quitter!")
            continue
            
    estimation = int(instruction)
    
    # 2.2 Si le nombre est trop petit on vas afficher "c'est grand"
    if estimation < juste_prix:
        print("Ton estimation est petit")
        
    # 2.3 Si le nombre est grand on vas afficher "c'est petit"
    elif estimation > juste_prix:
        print("Ton estimation est grand")
        
# 3. Féliictation à l'utilisateur
if abandon:
    print(f"Dommage 😞 le juste prix était : {juste_prix}")
else:
    print(f"Félicitation 🎉 vous avez trouvé le prix : {juste_prix}")


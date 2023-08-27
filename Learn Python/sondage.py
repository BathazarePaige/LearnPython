stats = {}
reponse = None

while reponse != "":
    reponse = input("Quelle est votre couleur préférée ?\n ")
    
    if reponse:
        if reponse in stats:
            stats[reponse] = stats[reponse] + 1
        else:
            stats[reponse] = 1

print("Vote pour les couleurs :")
for couleur, score in stats.items():
    print("-", couleur, ":",)


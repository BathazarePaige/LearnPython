"""import webbrowser
url = "https://vip-call-center.com"
webbrowser.open(url)"""
"""
import webbrowser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, 
                    webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get("chrome").open("https://vip-call-center.com")"""
"""from forex-python.bitcoin import BtcConverter
bitcoin = BtcConverter
print(bitcoin.get_latest_price("EURO"))
print(bitcoin.get_latest_price("USD"))
"""
"""P=["Cameroun","Jamaique","Canada","UK","USA","Coree"]
p1=input("Veuillez saisir le 1er pays : ")
p2=input("Veuillez saisir le 2e pays : ")
i=P.index(p1)
j=P.index(p2)
print(P)
P[i],P[j]=P[j],P[i]
print(P)"""
"""mot = input("Veuillez saisir un mot : ")
L = list(mot)
P = L.copy()
L.reverse()
print(L)
print(P)
if L==P:
    print(mot, "🥳 est un Palindrome")
else:
    print(mot, " 😠 n'est un Palindrome")"""
"""L = ["C++","PHP","JAVA","PYHTON","C#"]
L.sort(key=len, reverse=True)
print(L[0])"""
"""L =[10,["Math","Chimie"],["Python","C++"]]
L.append("Jamaïque")
print(L)
L.append([2,4])
print(L)
L[1].append("Anglais")
print(L)
L.insert(0,"Canada")
L.insert(1,[15,20])
L[3].insert(1,"Colombie")
print(L)
L.extend([29,8])
print(L)
L[3].extend(["HTML","CSS"])
print(L)
L.remove([2,4])
L[3].remove("HTML")
print(L)
m=L.pop(1)
print(m)
print(L)
L[2].pop(2)
print(L)
Paige = [10,["Math","Chimie"],["Python","C++"]]
print(Paige)
Paige.clear()
print(Paige)
N = [10,["Math","Chimie"],["Python","C++"]]
del N[0]
print(N)
del N[0][1]
print(N)"""
"""Nom = input("Veuillez saisir vore nom : ")
Age = int(input("Veuillez saisir votre âge : "))
print("Bonjour",Nom,", tu as ",Age,"ans bienvenue chez Open4didact")"""

"""A = float(input("Veuillez entrer la valeur de A : "))
B = float(input("Veuillez entrer la valeur de B : "))
So = A + B
Pr = A * B
Df = A - B 
Dv = A / B  
print("La somme est : ", So)
print("Le produit est : ",Pr)
print("La difference est : ",format(Df,".2f"))
print("Le division est : ",format(Dv,".2f"))"""
"""import math
r = float(input("Saisir de le rayon du cercle : "))
So = 4 * math.pi * (r**3)
Vo = So / 3 
print("Le volume de la sphère est : ", format(Vo, ".2f"))"""
"""fruit_list = ["Apple","Banana"]
print(f"Current Fruits list {fruit_list}")
new_fruit = input(f"Please enter a fruit name : \n")
fruit_list.append(new_fruit)
print(f"Updated Fruits List {fruit_list}")"""
"""fruit_list = ["Apple","Banana"]
print("Current Fruits list ",fruit_list)
new_fruit = input("Please enter a fruit name :\n")
fruit_list.append(new_fruit)
print("Updated Fruits List", fruit_list)"""

"""num_list = [1,2,3,4,5]
print(f"Current Number List {num_list}")
num = int(input("Please enter a number to add to list :\n"))
index = int(input(f"Please enter the index between 0 and {len(num_list) - 1} to add the number :\n"))
num_list.insert(index, num)
print(f"Updated Numbers List {num_list}")"""

"""num_list = [1,2,3,4,5]
print("Current Numbers List :",num_list)
num = int(input("Please enter a number to add to list :\n"))
index = int(input("Please enter the index between 0 and " + str(len(num_list)-1) + " to add the number :\n"))
num_list.insert(index, num)
print("Updated Numbers List :",num_list)"""
"""extend_list = []
extend_list.extend([1,2])
print(extend_list)
extend_list.extend((3,4))
print(extend_list)
extend_list.extend("ABC")
print(extend_list)"""
"""programming_lang = ['P','Y','T','H','O','N']
print("Length of List: "+str(len(programming_lang)))"""
"""programming_lang = ["P","Y","T","H","O","N"]
print("Length of list : ",len(programming_lang))"""
"""programming_lang = ['P','Y','T','H','O','N']
print(f"Length of List: {len(programming_lang)}")"""


scores = {}
scores["Bathazare"] = 10
scores["Kenzah"] = 5
scores["Keizyah"] = 7
scores["Charlize"] = 3

name = "Bathazare"
# 1st Method
'''if name in scores:
    print("Yes, the key",name,"exists in the disctionnary")
else:
    print("No, the key",name,"doesn't exist in the disctionnary")'''
    
# 2nd Method

try:
    scores["Bathazare"]
    print(f"Yes, The key {name} exists in the dictionnary")
except KeyError as error:
    print(f"No, The key {name} doesn't exist in the dictionnary")
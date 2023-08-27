#-*-coding: utf-8 -*-
'''scores = {}
scores["Bathazare"] = 10
scores["Kenzah"] = 5
scores["Keizyah"] = 7
scores["Charlize"] = 3
name = "Bathazare"
try:
    scores["Bathazare"]
    print(f"Yes, The key {name} exists in the dictionnary")
except KeyError as error:
    print(f"No, The key {name} doesn't exist in the dictionnary")'''


'''matches = {}
matches["Bathazare"] = [3,4,8]
matches["Kenzah"] = [10,3,2]
matches["Bathazare"].append(19)
for nom, scores in matches.items():
    print(f"{nom} :")
    for score in scores:
        print(f" ➖  {score}")'''
'''couleurs = {}
reponse  = None
while reponse != "":
    reponse = input("Quelle est votre couleur préférée ?\n ")
    if reponse:
        if reponse in couleurs:
            couleurs[reponse] = couleurs[reponse] + 1
        else:
            couleurs[reponse] = 1
            
print("Vote pour les couleurs :")
for couleur, score in couleurs.items():
    print(f"- {couleur} : {score}")'''

'''fichier = open(r"C:\\LearnPython\\fichiers de travail\\chanson.txt")
texte = fichier.read().lower()
ponctuation = (";",",",".",":","<<",">>","'","-","?","!")
for signe in ponctuation:
    texte = texte.replace(signe, "")
mots  = set(texte.split())

for mot in mots:
    print(mot)
'''
'''name = "Bathazare Paige"

print(f"The length of my name is : {len(name)}")
print(f"Let's find the position of the letter  i : {name.find('i')}th position")
print(f"Let's capiltalize my name : {name.capitalize()}")
print(f"Let's see what happens : {name.upper()}")
print(f"Let's see what happens : {name.lower()}")
print(f"Let's see what happens : {name.isdigit()}")
print(f"Let's see what happens : {name.isalpha()}")
print(f"Let's see how many 'a' got my name : {name.count('a')}")'''
'''name  = input("What is your name : ")
age = int(input("How old are you : "))
height = float(input("How tall are you : "))

age += 1
print(f"Yo {name}, you are {age} years old and you are {height}cm")'''

#7 math functions 🧮
'''import math 
x =1
y = 2
z = 3
pi = 3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi)
print(max(x,y,z))
print(min(x,y,z))'''
#8 string slicing ✂️

'''name = "Bathazare Paige"
first_name = name[9:15]

print(first_name)'''

'''website1 = "http://open4didact.co"
website2 = "http://wikipedia.com"

slice = slice(7,-4)
print(website2[slice])'''

#9 if statements 🤔
'''age = int(input("How old are you ? : "))

if age >= 18:
    print("You are an adult!")
elif age == 100:
    print("You are century old!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")'''
#10 logical operators 🔣
'''temp = int(input("What is the temperature outside : "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today! \n go outside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today!\n stay inside!")'''

#11  while loops 🔄
"""name = ""

while len(name) == 0:
    name = input("Enter your name : ")
print(f"Hello {name}")"""
'''
name = None

while not name:
    name = input("Enter your name : ")
print(f"Hello {name}")'''

'''for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")'''

#13 nested loops ➿

'''rows = int(input("How many rows ? : "))
columns = int(input("How many columns ? : "))
symbol = input("Enter a symbol to use: ")

for i in range(rows): 
    for j in range(columns):
        print(symbol, end="")
    print()'''

'''while len(list_language)<longueur:
    item = input("Please enter the language : ")
    if item not in list_language:
        list_language.append(item)
print(list_language, end=" ")'''

'''user_input = ""

while user_input.count(" ") < 2:
    user_input = input("Enter at least 3 space-separated shopping items : ")
    language = user_input.split(" ")
print(language)'''

'''shopList = [] 
maxLengthList = 6
while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopList.append(item)
    print(shopList)
print(f"That's your Shopping List : \n {shopList}")'''
#print(shopList)

'''fruit_list = ["Aplle", "Banana"]

print(f"Current Fruits List 👉   {fruit_list}")
new_fruit = input("Please enter a fruit name: \n")
fruit_list.append(new_fruit)

print(f"Update Fruits List 👉   {fruit_list}")
num_list = [1,2,3,4,5]
print(f"Current Numbers List {num_list}")
num = int(input("Please enter a number to add to list : \n"))
index = int(input(f"Please enter the index between 0 and {len(num_list)-1} to add the number : \n"))
num_list.insert(index, num)
print(f"Updated Numbers List {num_list}")'''

'''extend_list = []

extend_list.extend([1,2])
print(extend_list)
extend_list.extend((3,4))
print(extend_list)
extend_list.extend("ABC")
print(extend_list)'''

'''evens = [2,4,6]
odds = [1,2,3]

nums = odds + evens 
print(nums)'''

'''students = ["Mark","Lindsay","Peter"]
to_remove = input("Enter the name of a student who has handed in their homework : ")

if to_remove in students:
    students.remove(to_remove)
    print("This student's homework has been recorded.")
else:
    print("This student does not appear in your list.")
print(students)'''
#16 2D lists 📜
'''drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]
print(food[1][0])'''
#17 tuples 📄
'''student = ("Paige",24,"Male")
#print(student.count("Paige"))
#print(student.index("Male"))

for x in student:
    print(x)
if "Paige" in student:
    print("Paige is here")'''
#19 dictionaries 📖
'''capitals = {"USA":"Washington DC",
            "Jamaica":"Kingston",
            "Cameroon":"Yaounde",
            "Ghana":"Accra"}
capitals.update({"German":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("Ghana")
capitals.clear()'''
#print(capitals["Ghana"])
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

'''for key, value in capitals.items():
    print(key,value)'''
'''first_name = name[:3].upper()
last_name = name[10:].upper()
print(last_name)'''
#21 functions 📞
'''def multiplier(numero1,numero2):
    result = numero1*numero2
    return result
x = multiplier(6,8)
print(x)'''
'''def add(*fais):
    sum = 0
    fais[0] = 0
    for i in fais:
        sum += i
    return sum
print(add(1,2,3,4,5,6))'''
'''
def multiply(number1, number2):
    return number1 * number2

x = multiply(6,8)
print(x)'''

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(round(abs(float(input("Enter a whole positive number: ")))))
#print(num)

'''def add(*fonction):
    sum = 0
    for i in fonction:
        sum += i
    return sum
print(add(1,2,3,4,5,6))'''
'''def add(*nombres):
    total = 0
    for nomb in nombres:
        total += nomb
    return total 

print(add(2,3))
print(add(2,3,4))
print(add(2,3,4,5))
print(add(2,3,4,5,6))'''
'''def aire_rectangle(a,b):
    return a*b
def aire_rectangle(cote1=0, cote2=0):
    return cote1*cote2

if __name__ == "__main__":
    rec1 = [3,8]
    rec2 = {"cote1":4,"cote2":8}
print(aire_rectangle(*rec1))
print(aire_rectangle(**rec2))'''


#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
'''number = 1986

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))'''

"""name = "Bathazare"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))
print("Hello, my name is {:>10}. Nice to meet you.".format(name))"""
"""number = 1000
print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))"""
"""from datetime import datetime
now = datetime.now().strftime("%A %d %B, %Y - %H:%M:%S")
print(f"date and time: {now =}")"""
"""from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format"""
"""import random
x = random.randint(1,5)
y = random.random()


myList = ["rock","paper","scissors"]
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)"""
"""try:
    numerator = int(input("Enter a number to divide : "))
    denominator = int(input("Enter a number to divide by : "))
    result = numerator / denominator 
    
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("Something weng wrong")
else:
    print(result)
finally:
    print("This will always execute")"""
#31 - file detection 📁
"""import os 
path = "C:\\Users\\Bathazare PAIGE\\Desktop\\03.Formation Digital Marketing"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is directory!")
else:
    print("That location doesn't exists")"""
#32 read a file 🔍
"""try:
    with open("C:\\Users\\Bathazare PAIGE\\Desktop\\tex.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
"""
#33 write a file 📝
"""test = "Yooooo\n This is some text\n Have a good one!\n"
with open("C:\\Users\\Bathazare PAIGE\\Desktop\\text.txt","w") as file:
    file.write(test)"""

#34 copy a file 🖨️

"""import random 
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None
computerScore = 0
playerScore = 0
while player not in choices:
    player = input("rock, paper, or scissors ?: ").lower()

if player == computer:
    print("computer : ", computer)
    print("player : ",player)
    print("Computer Score :", computerScore=+1)
    print("Player Score :", playerScore=+1)
    print("Tie!")

elif player == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
        print("Computer Score : " , computerScore=+1)
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", computer)
        print("You win㊗️!")
        print("Player Score : ", playerScore=+1)
        
elif player == "scissors":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
        print("Computer Score : " , computerScore=+1)
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", computer)
        print("You win㊗️!")
        print("Player Score : ", playerScore=+1)
        
elif player == "paper":
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
        print("Computer Score : " , computerScore=+1)
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", computer)
        print("You win㊗️!")
        #print("Player Score : ", playerScore=+1)"""
"""#--------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
    
#--------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT 🎉 ")
        return 1
    else:
        print("WRONG  😡  ")
        return 0
#--------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------")
    print("RESULTS")
    print("-----------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is : "+str(score)+"%")
#--------------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False
#--------------------------------

questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
        ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
        ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
        ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
print("Byeeeeeee!")"""

"""from car import Car 

car_1 = Car("Chevy","Corvette",2021,"Blue")
car_2 = Car("Ford","Mustang",2022,"Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print()
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print()
car_1.drive()
car_1.stop()
print()
car_2.drive()
car_2.stop()
print()
print(car_1.wheels)
print(car_2.wheels)"""
"""class Animal:
    
    alive = True 
    
    def eat(self):
        print("This animal is eating")
        
    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal): 
    
    def run(self):
        print("This animal is running")

class Fish(Animal):
    
    def swim(self):
        print("This animal is swimming")

class Hawk(Animal):
    
    def fly(self):
        print("This animal is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


rabbit.run()
fish.swim()
hawk.fly()"""
"""class Organisim:
    
    alive = True

class Animal(Organisim):
    
    def eat(self):
        print("This animal is eating")
    
class Dog(Animal):
    
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()"""

#44 multiple inheritance 👨‍👩‍👧‍👦
"""class Prey:
    
    def flee(self):
        print("This animal flees")

class Predator:
    
    def hunt(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()
fish.flee()
fish.hunt()"""
#46 method chaining ⛓️
"""class Car:
    
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()

car.turn_on().drive().brake().turn_off()"""
"""class Car:
    color = None

class Motorcycle:
    
    color = None
    
def change_color(vehicle,color):
    
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_1.color)
print(car_3.color)
print(bike_1.color)"""
""""class Duck:
    
    def walk(self):
        print("This duck is walking")
    
    def talk(self):
        print("This duck is qwuacking")
        
class Chicken:
    
    def walk(self):
        print("This chicken is walking")
    
    def talk(self):
        print("This chicken is clucking")
        
class Person():
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)"""
#print(foods)
"""foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
print(foods)

foods = list()
while True:
    food := input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)"""
#sort 🗄️
"""students = [("Squidward","F",60),("Sandy","A",30),("Patrick","D",36),("Spongebob","B",20),("Mr. Paige","C",78),("Charlize","E",40),("Kenzah","G",15),("Keizyah","I",80)]
grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)
#sorted_students = sorted(students)
for i in students:
    print(i)"""
#map 🗺️
"""store = [("shirt",20.00),
        ("Pants",25.00),
        ("Jackets",50.00),
        ("Socks",10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

#for i in store_euros:
for i in store_dollars:
    print(i)"""
#filter 🍺
"""friends = [("Rachel",19),
            ("Bathazare",18),
            ("Phoebe",17),
            ("Joey",16),
            ("Chandler",21),
            ("Ross",20),
            ("Kenzah",8),
            ("Charlize",3)]

age = lambda data:data[1] >= 18

drinking_buddies  = list(filter(age,friends))

for i in drinking_buddies:
    print(i)"""
# reduce ♻️

#import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x, y,: x + y, letters)
#print(word)

"""factorial = [5,4,3,2,1]
result =  functools.reduce(lambda x, y,: x + y, factorial)
print(result)
"""
# list comprehensions 📰
"""students = [100,90,80,70,60,50,40,30,20,0]

#passed_students = list(filter(lambda x: x >= 60, students))

passed_students = [i for i in students if i >= 60]
print(passed_students)"""
#dictionary comprehensions 🕮 
#cities_in_F = {"New York": 32, "Boston": 75,"Los Angeles": 100, "Chicago":50}
#cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)
#----------------------------------------------------------------------------------------
#weather = {'New York': "snowing",'Boston':"Sunny",'Los Angeles':"Sunny",'Chicago':"Cloudy"}
#sunny_weather = {key: value for (key,value) in weather.items() if value =="Sunny"}
#print(sunny_weather)
#----------------------------------------------------------------------------------------
#cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
#print(desc_cities)
#----------------------------------------------------------------------------------------
"""def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"
    
cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)"""
#61 zip function 🤐
"""usernames = ["Bathazare","Paige","Kenzah","Keizyah","Charlize"]
passwords = ("p@word","123654","Abc-*/2","Y@ounde124","evol12354")


users = list(zip(usernames,passwords))

print(type(users))

for i in users:
    print(i)

"""
#62 if name == '__main__' ❓
#63 time module ⌚
#import time 
#import locale
#print(time.ctime(1000000))

#print(time.time()) 
#print(time.ctime(time.time()))
"""locale.setlocale(locale.LC_TIME,locale='fr_FR')
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%A, %d %B %Y %H:%M:%S", time_object)
print(local_time.capitalize())"""

"""time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)
"""
"""time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)"""

#64 threading 🧵

"""import threading
import time 

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
    
def drink_coffee():
    time.sleep(4)
    print("You drank coffe")
    
def study():
    time.sleep(5)
    print("You finish studying")
    
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())"""

# 65 daemon threads 😈


"""import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for : ", count, "seconds")
        
x =threading.Thread(target=timer,daemon=True)
x.start()

answer = input("Do you wish to exit ?") 
    """
"""import threading
import time

def daemon():
    while True:
        print("Daemon thread running")
        time.sleep(1)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()

d.join()
print("Daemon thread ended")"""

#66  multiprocessing ⚡
"""from multiprocessing import Process
import time


def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(1000000000))
    b = Process(target=counter, args=(1000000000))
    
    a.start()
    b.start()
    
    
    a.join()
    b.join()
    
    print("finished in:",time.perf_counter(),"seconds")


if __name__ == "__main__": 
    main()"""
#67 GUI windows 🖼️
"""from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Open4didact")

icon = PhotoImage(file="Open4didact - Logo.png")
window.iconphoto(True, icon)
window.config(background="#85287D")

window.mainloop()"""

#68 labels 🏷️
"""from tkinter import *

window = Tk()

photo = PhotoImage(file="Open4didact - Logo.png")

label = Label(window,
            text="Welcome",
            font=("Arial",40,"bold"),
            fg="#FFF",
            bg="#85287D",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound="bottom")


label.pack()
#label.place(x=100,y=100)





window.mainloop()
"""
#67 buttons 🛎️
"""
from tkinter import *

count = 0

def click():
    global count
    count +=1
    print(count)

window = Tk()

photo = PhotoImage(file="thumb-up.png")

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#85287D",
                bg="#29A0CA",
                activeforeground="#E63B2C",
                activebackground="#29A0CA",
                state=ACTIVE,
                image=photo,
                compound="bottom")

button.pack()

window.mainloop()"""

#70 entrybox ⌨️
"""from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)
    #entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
            font=("Arial",50),
            fg="#85287D",
            bg="#E63B2C",
            show="*")
#entry.insert(0,"Charlize")
entry.pack(side=LEFT)


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

window.mainloop()"""
# checkbox ✔️
"""from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree : 🙃")

window = Tk()

x = IntVar()

python_photo = PhotoImage(file="Open4didact - Logo.png")

check_button = Checkbutton(window,
                        text="I agreeto something",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        font=("Arial",20),
                        fg="#01f0fd",
                        bg="#d88dd4",
                        activeforeground="#01f0fd",
                        activebackground="black",
                        padx=25,
                        pady=10,
                        image=python_photo,
                        compound="left")
                        
check_button.pack()

window.mainloop()"""
#72 radio buttons 🔘
"""from tkinter import *

food = ["pizza","hamburger","hotdog"]
def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a hamburger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("hung")


window = Tk()

pizzaImage = PhotoImage(file="C:\\LearnPython\\images\\pizza.png")
hamburgerImage = PhotoImage(file="C:\\LearnPython\\images\\hamburger.png")
hotdogImage = PhotoImage(file="C:\\LearnPython\\images\\hot-dog.png")
foodImages = [pizzaImage,hamburgerImage,hotdogImage]



x =IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[index], #adds text to radio
                            variable=x, #groups radiobuttons togheter if they share the share the same variable
                            value=index, #assigns each radiobutton a different value
                            padx=25, #adds padding on x-axis
                            font=("impact",50),
                            image=foodImages[index], #adds image to radiobutton
                            compound="left", #adds image on text
                            indicatoron=0, #eleminate circle indicators
                            width=375, #sets width of radio buttons
                            command=order #set command of radionbutton to function 
                            )
    
    radiobutton.pack()
window.mainloop()"""
#73 scale 🌡️
"""from tkinter import *

def submit():
    print(f"The temperature is: {scale.get()} degrees C")

window = Tk()

scale = Scale(window,
            from_=100,
            to=0,
            length=600,
            orient=VERTICAL, #orientation of scale
            font=("Consolas",20),
            tickinterval=10,
            )
scale.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()"""
#94 send an email 📧
"""import smtplib

sender = "saturainvincent@gmail.com"
receiver = "bathazarepaige@gmail.com"
password = "J@maica&-022"
subject = "Python Email Test"
body = "I wrote an email I 🙃"

#Header 



server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in ...")
    server.sendmail(sender,receiver, message)
    print("Email has been sent!")
    
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")"""
#95  run with command prompt 👨‍💻

"""print("Hello World!")

name = input("What's your name?: ")

print(f"Hello {name}")"""
#96 pip 🏗️

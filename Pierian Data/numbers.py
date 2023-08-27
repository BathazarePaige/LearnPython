# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# sourcery skip: avoid-builtin-shadow
"""calcul = ((10**2 / 4) * 4) + 1 - 0.75
print(calcul)"""




"""trouver =  3 + 1.5 + 4
print(type(trouver))"""

"""loc = input("Enter the word : ")
if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the store!")
else:
    print("I don't not know much")"""
"""name = input("Enter your name : ")

if name == "Franckie":
    print("Hello Franckie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print(input("Sorry what's your name ? : "))"""

#mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f"Even Number :{num}")
    else:
        print(f"Odd Number : {num}")"""

"""list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    
print(list_sum)"""
"""name = input("Your name : ")

for i in range(1,11):
    print(i, name)
"""
"""tup = (1,2,3)

for item in tup:
    print(item)"""

"""mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for item in mylist:
    print(item)"""

"""d = {"k1":1,"k2":2,"k3":3,"k4":4,"k5":5}

for value in d.values():
    print(value)"""

"""for index, letter in enumerate("abcde"):
        print(f"At index {index} the is : {letter} ")"""

"""for index, letter in enumerate("abcde"):
    print(index)
    print(letter)
    print("\n")"""
"""    
mylist1 = [1,2,3,4,5,6]
mylist2=["a","b","c"]
mylist3=[100,200,300,400]

for item in zip(mylist1,mylist2,mylist3):
    print(item)"""
"""mylist = []

for x in [2,4,6]:
    mylist.extend(x*y for y in [100,200,300])
print(mylist)"""


# Use for, .split(), and if to create a Statement that will print out words that start with 's':

"""st = 'Print only the words that start with s in this sentence'

# Séparer la chaîne de caractères en mots
words = st.split()

# Boucle pour parcourir les mots
for word in words:
    # Si le mot commence par "s"
    if word[0].lower() == 's':
        print(word)"""
"""
for num in range(10):
    if num % 2 == 0:
        print(num)
"""

"""divisible_by_3 = [x for x in range(1, 50) if x % 3 == 0]
print(divisible_by_3)"""


# Go through the string below and if the length of a word is even print "even!


"""st = "Print every word in this sentence that has an even number of letters"

for word in st.split():
    if len(word) % 2 == 0:
        print(f"{word} : is even!")"""
        


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""    
for i in range(1,101):
    if i % 3 == 0:
        print(f"{i} : Fizz")
    elif i % 5 == 0:
        print(f"{i} : Buzz")
    else:
        print(f"{i} : Fizzbuzz")"""
        
# Use List Comprehension to create a list of the first letters of every word in the string below:
"""st = 'Create a list of the first letters of every word in this string'
first_letters = [word[0] for word in st.split()]
print(first_letters)"""

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    if i % 3 == 0:
        print(f"{i} : Fizz")
    elif i % 5 == 0:
        print(f"{i} : Buzz")
    else:
        print(f"{i} nothing else")
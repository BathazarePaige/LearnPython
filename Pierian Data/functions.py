"""def say_hello():
    print("Hello")
    print("are")
    print("you")
say_hello()"""


"""def say_hello(name="Default"):
    print(f"Hello {name}")
say_hello("Bathazare")"""


"""def add_num(num1, num2):
    return num1+num2
#result = add_num(10,20)
print(add_num(10,20))"""


"""def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([1,3,5]))"""

"""stock_prices = [("AAPL", 200),("GOOG",300),("MSFT",400)]

#for item in stock_prices:
#   print(item)
for stock,price in stock_prices:
    print(price)"""


"""work_hours = [("Abby",100),("Billy",400),("Cassie",800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return(employee_of_month,current_max)
print(employee_check(work_hours))"""


"""from random import shuffle

example = [1,2,3,4,5]
shuffle(example)

print(example)"""
"""
from random import shuffle

mylist = ["",0,""]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
#print(shuffle_list(mylist))

def player_guess():

    guess = ""

    while guess not in ["0","1","2"]:
        guess = input("Pick a number : 0, 1 or 2 : ")
        return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == "0":
        print("Correct Guess!")
    else:
        print("Wrong! Better luck next time")
        print(mylist)
mixed_list = shuffle_list(mylist)
guess = player_guess()

print(check_guess(mixed_list,guess))"""


"""stock_prices = [("APPL",200),("GOOG",400),("MSFT",100)]
#for item in stock_prices:
#    print(item)

for ticker,price in stock_prices:
    print(price+(0.1*price))"""

"""work_hours = [("Abby", 100),("Billy",400),("Cassie",800)]ter

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee,hours in work_hours:
    return
    return(employee_of_month,current_max)"""
# Fonction
"""def say_hello():
    print("Hello")
    print("Are")
    print("You")
say_hello()
"""
"""def say_hello(name):
    print(f"Hello {name}")
say_hello("Paige")"""


"""def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        return even_numbers

check_even_list([1,3,5])"""

# stock_prices = [("APPL",200),("GOOG",400),("MSFT",100)]
# for paige in stoc_prices:
#     print(paige)
# for paige, price in stock_prices:
#     print(price+(0.1*price))

"""work_hours = [("Paige",100),("Kenzah",400),("Keizyah",800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)

employee_check(work_hours)"""

"""def myfunc(*args):
    return sum((args))*0.05

myfunc(40,60,50,100,90)"""

"""def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print("I did not find any legumes here")

myfunc(fruit="apple",veggie="lettuce")"""

"""def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]}{kwargs['food']}")

myfunc(10,20,30, fruit="orange",food="eggs",animal="dog")"""

"""def myfunc(**kwargs):
    if "fruit" in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")

# myfunc(fruit="pineapple")
myfunc()"""

"""def myfunc(*args,**kwargs):
    if "juice" in kwargs:
        print(
            f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice ?")

myfunc("eggs","spam",fruit="cherries",juice="orange")"""


# def check_even_list(num_list):
#     even_numbers = []
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)

#     return even_numbers


# print(check_even_list([1, 2, 3, 5, 8, 12, 4, 16, 20, 24, 26, 30, 32]))
# stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]

# for item in stock_prices:
#     print(item)

# for ticker, price in stock_prices:
#     unit = 0.1*price
#     print(price+unit)


"""import random
example = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(example)
print(example)
"""


"""def hanoi(disks, source, helper, destination):
    # Base condition
    if (disks == 1):
        print(f"disk {disks} moves from tower {source} to tower {destination}")
        return

    hanoi(disks-1, source, destination, helper)
    print(f"Disk {disks} moves from tower {source} to tower {destination}")
    hanoi(disks-1, helper, source, destination)


disks = int(input("Number of disks to be displayed : "))

hanoi(disks, "A", "B", "C")
"""

"""trial = input("enter a word : ")
new_trial = trial[::-1]
print(new_trial)
"""

# menu = ["espresso",
#         "mocha",
#         "latte",
#         "cappucino",
#         "cortado",
#         "americano"]


# def find_coffee(coffee):
#     if coffee[0] == "c":
#         return coffee


# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)

# filter_coffee = filter(find_coffee, menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)
# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# data = [x+3 for x in data]
# print(f"Updateng the list : {data}")

# new_data = [x*2 for x in data]
# print(f"Updating new list : {new_data}")

# fourX = [x for x in new_data if x % 4 == 0]
# print(f"Divisible by four : {fourX}")


# fourxsub = [x-1 for x in new_data if x % 4 == 0]
# print(f"Divisible by four minus one : {fourxsub}")

# nines = [x for x in range(100) if x % 9 == 0]
# print(f"Nines : {nines}")

# usingrange = {x: x*2 for x in range(12)}
# print(f"Using range(): {usingrange}")


# months = ["Jan",
#         "Feb",
#         "Mar",
#         "Apr",
#         "May",
#         "June",
#         "July",
#         "Aug",
#         "Sept",
#         "Oct",
#         "Nov",
#         "Dec"]
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# numdict = {x: x*2 for x in number}
# print(f"Using one input list to create dict : {numdict}")


# months_dict = dict(zip(number, months))
# print(f"Using two lists : {months_dict}")

# set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
# print(set_a)
# Input data: List of dictionaries
# numbers = [15, 30, 47, 82, 95]


# def lesser(numbers):
#     return numbers < 50


# small = list(filter(lesser, numbers))
# print(small)

# class Paylips:
#     def __init__(self, name, payment, amount) -> None:
#         self.name = name
#         self.payment = payment
#         self.amount = amount

#     def pay(self):
#         self.payment = "yes"

#     def status(self):
#         if self.payment == "yes":
#             return f"{self.name} is paid ${str(self.amount)}"
#         else:
#             return f"{self.name} is not paid yet"


# keizyah = Paylips("Keizyah", "no", 1000)
# kenzah = Paylips("Kenzah", "no", 3000)

# print(keizyah.status(), "\n", kenzah.status())

# keizyah.pay()
# print("After payment")
# print(keizyah.status(), "\n", kenzah.status)

# class Employees:
#     def __init__(self, name, last) -> None:
#         self.name = name
#         self.last = last


# class Supervisors(Employees):
#     def __init__(self, name, last, password) -> None:
#         super().__init__(name, last)
#         self.password = password


# class Chefs(Employees):
#     def leave_request(self, days):
#         return f"May I take a leave for {str(days)} days"


# charlize = Supervisors("Charlize", "A", "Apple")

# emily = Chefs("Emily", "E")
# juno = Chefs("Juno", "J")

# print(emily.leave_request(3))
# print(charlize.password)
# print(emily.name)
# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)


import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

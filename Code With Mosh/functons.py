"""def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Bathazare", "Paige")
greet("Kenzah","Paige")"""


"""def multiply(*numbers):
    total = 1
    for number in numbers:
       total *= number
    return total

print(multiply(2, 3, 4, 5))"""
"""def save_user(**user):
    print(user)

save_user(id=1, name="Bathazare",age=13)"""

def fizz_buzz(input):
    # sourcery skip: assign-if-exp, hoist-repeated-if-condition, reintroduce-else
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
print(fizz_buzz(100))


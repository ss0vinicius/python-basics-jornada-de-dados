# Code a KPI calculator that ask the user for the following values:
# name, salary and bonus percentage. 
# The program should return the bonus that this person will receive.
# Bonus = 1000 + salary*bonus_percentage

CONST_BONUS = 1000

name = input("What the person's name? ")
salary = float(input("What is the salary? "))
bonus_percentage = float(input("What is the bonus percentage? "))
bonus = CONST_BONUS + salary*bonus_percentage

print(bonus)

print("The bonus that this person will receive will be: " + str(bonus) + " reais")
#or, to write strings and variables together, we can use f-string
print(f"The bonus that {name} will receive will be: {bonus} reais")
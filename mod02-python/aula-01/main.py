# 1 - Code a program that ask the name of the user and return the length of it

name = input("What is your name? ")
nameLength = len(name)
print(nameLength)

#or

print(len(input("What is your name? ")))

# 2 - Code a program that ask 2 numbers and return the sum of them

number1 = input("Enter a number: ") 
number2 = input("Enter another number: ")
sum = number1 + number2
print(sum)

print(input("Enter a number: ") + input("Enter another number: "))

# So, running the a code like this, we are going to have a problem. The input function always return a string, so when we try to sum the numbers, we are going to concatenate the strings. To solve this, we need to convert the strings to numbers before sum them.

number1 = int(input("Enter a number: ")) 
number2 = int(input("Enter another number: "))
sum = number1 + number2
print(sum)
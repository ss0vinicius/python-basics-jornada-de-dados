# #### Integer (`int`)

# 1. Write a program that adds two integers entered by the user.
# 2. Create a program that receives a number from the user and calculates the remainder of dividing that number by 5.
# 3. Develop a program that multiplies two numbers provided by the user and shows the result.
# 4. Make a program that asks for two integers and prints the integer division of the first by the second.
# 5. Write a program that calculates the square of a number provided by the user.

# 1. Write a program that adds two integers entered by the user.
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
sum = number_1 + number_2
print(sum)

# 2. Create a program that receives a number from the user and calculates the remainder of dividing that number by 5.
number_remainder = int(input("Type a number "))
remainder = number_remainder % 5
print(remainder)

# 3
number_3_1 = int(input("Type a number to be multiplied: "))
number_3_2 = int(input("Type another number: "))
multiplied = number_3_1 * number_3_2
print(multiplied)

# 4
number_4_numerator = int(input("Type the numerator: "))
number_4_denominator = int(input("Type the denominator: "))
division = number_4_numerator // number_4_denominator
print(f"The division result is: {division}")

# 5 
number_5 = int(input("Type the number that you would like to have the square of it: "))
number_square = number_5**2 
print(f"The square of {number_5} is: {number_square} ")
print(number_5**2)

# #### Float Numbers(`float`)

# 6. Write a program that receives two floating point numbers and performs their addition.
# 7. Create a program that calculates the average of two floating point numbers provided by the user.
# 8. Develop a program that calculates the power of a number (base and exponent provided by the user).
# 9. Make a program that converts the temperature from Celsius to Fahrenheit.
# 10. Write a program that calculates the area of a circle, receiving the radius as input.

# 6
number_6_1 = float(input("Type a number to be added "))
number_6_2 = float(input("Type another number "))
addition = number_6_1 + number_6_2 
print(f"The result of {number_6_1} + {number_6_2} = {addition}")

# 7 
number_7_1 = float(input("Type the first number that you would like to calculate the average: "))
number_7_2 = float(input("Type the other number: "))
average = (number_7_1 + number_7_2) / 2
print(f"The average between {number_7_1} and {number_7_2} is {average}")

# 8 
number_8_base = float(input("What is the number you would like to use as base? "))
number_8_exp = float(input("What is the exponent? "))
result_exponent = number_8_base ** number_8_exp
print(f"The result is {result_exponent}")

# 9
temperature = float(input("What is the current temperature?(Celsius) "))
temperature_fahrenheit = (temperature * (9/5)) + 32
print(f"The temperature in Fahrenheit is {temperature_fahrenheit}")

# 10 
radius = float(input("What is the radius of the circle? "))
pi = 3.14
area = pi*(radius**2)
print(f"The area of this circle is: {area:.2f}")
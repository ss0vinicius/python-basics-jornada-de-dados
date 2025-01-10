# #### Boolean (`bool`)

# 16. Write a program that evaluates two boolean expressions entered by the user and returns the result of the AND operation between them.
# 17. Create a program that receives two boolean values from the user and returns the result of the OR operation.
# 18. Develop a program that asks the user to enter a boolean value and then invert this value.
# 19. Make a program that compares if two numbers provided by the user are equal.
# 20. Write a program that checks if two numbers provided by the user are different.

# 16, 17 and 18
expression_16_1 = input("Write a boolean expression: ").lower()
expression_16_2 = input("Write another one: ").lower()

if expression_16_1 == "true":
    expression_16_1 = True
else:
    expression_16_1 = False
if expression_16_2 == "true":
    expression_16_2 = True
else:
    expression_16_2 = False

operation_and = expression_16_1 and expression_16_2
operation_nand = not (expression_16_1 and expression_16_2)
operation_or = expression_16_1 or expression_16_2
operation_xor = expression_16_1 ^ expression_16_2
operation_not_1 = not expression_16_1
operation_not_2 = not expression_16_2
operation_nor = not (expression_16_1 or expression_16_2)

print(f"The result of this 2 boolean expression with an and is: {expression_16_1} and {expression_16_2}")
print(f"AND: {operation_and}")
print(f"NAND: {operation_nand}")
print(f"OR: {operation_or}")
print(f"XOR: {operation_xor}")
print(f"NOT1: {operation_not_1}")
print(f"NOT2: {operation_not_2}")
print(f"NOR: {operation_nor}")

# 19
number_19_1 = int(input("Type a number: "))
number_19_2 = int(input("Type another number: "))
equal = number_19_1 == number_19_2
if equal:
    print(f"The numbers {number_19_1} and {number_19_2} are equal")
else:
    print(f"The numbers {number_19_1} and {number_19_2} are different")

# 20
number_20_1 = int(input("Type a number: "))
number_20_2 = int(input("Type another number: "))
different = number_20_1 != number_20_2
if different:
    print(f"The numbers {number_20_1} and {number_20_2} are different")
else:
    print(f"The numbers {number_20_1} and {number_20_2} are equal")
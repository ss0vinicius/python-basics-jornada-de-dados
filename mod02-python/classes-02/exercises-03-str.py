# #### Strings (`str`)

# 11. Write a program that receives a string from the user and converts it to uppercase.
# 12. Create a program that receives the user's full name and prints the name with all lowercase letters.
# 13. Develop a program that asks the user to enter a sentence and then prints this sentence without any blank spaces at the beginning and end.
# 14. Make a program that asks the user to enter a date in the format "dd/mm/yyyy" and then prints the day, month, and year separately.
# 15. Write a program that concatenates two strings provided by the user.

# 11
user_string = input("Write some string to save: ")
user_string_upper = user_string.upper()
print(f"Your string in uppercase: {user_string_upper}")

# 12
user_full_name = input("What is your full name? ")
user_fn_lower = user_full_name.lower()
print(f"Your name using lowercase: {user_fn_lower}")

# 13
sentence = input("Write a phrase: ")
sentence_without_blank_spaces = sentence.strip()
print(f"Your sentence without blank spaces in the beginning and in the end: {sentence_without_blank_spaces}")

# 14
date = input("Enter some date in this format: 'yyyy/mm/dd': ")
date_info = date.split("/")
print(f"The year is: {date_info[0]}, the month is: {date_info[1]} and the day is: {date_info[2]}")

# 15 
str_1 = input("Write the first string: ")
str_2 = input("Write another one: ")
concatenated = str_1 + str_2
print(f"The string concatenated is: {concatenated}")

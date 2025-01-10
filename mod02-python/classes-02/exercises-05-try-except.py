# #### try-except e if

# 21: temperature converter
# write a program that converts the temperature from Celsius to Fahrenheit. The program should ask the user for the temperature in Celsius and, using try-except, ensure that the input is numeric, handling any ValueError. Print the result in Fahrenheit or an error message if the input is not valid.

exit_program = False
while (not exit_program):
    print("___________________________________________________")
    try:
        temperature_celsius = float(input("What is the temperature you want to convert? "))
        if(temperature_celsius < -273.15):
            raise ValueError("The temperature can't be lower than -273.15")
    except ValueError as value_error:
        print(value_error)
    except Exception as error:
        print(error)
    else:
        option = None
        while(option != "kelvin" and option != "fahrenheit"):
            try:
                option = input("Do you want it in Kelvin or Fahrenheit? ").lower()
                if(option != "kelvin" and option != "fahrenheit"):
                    raise ValueError("The option is not valid")
            except ValueError as value_error:
                print(value_error)
            except Exception as error:
                print(error)    
            else:
                if(option == "kelvin"):
                    temperature_kelvin = temperature_celsius + 273.15
                    print(f"The temperature in Kelvin is {temperature_kelvin}")
                if(option == "fahrenheit"):
                    temperature_fahrenheit = (temperature_celsius * (9/5)) + 32
                    print(f"The temperature in Fahrenheit is {temperature_fahrenheit}")
                exit_program = input("Do you want to exit the program?(yes) ").lower() == "yes"
                
    
# 22: palindrome checker
# Create a program that checks if a word or phrase is a palindrome (reads the same from back to front, disregarding spaces and punctuation). Use try-except to ensure that the input is a string. Tip: Use the isinstance() function to check the type of the input.

# 23: simple calculator
# Development a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. Use try-except to handle divisions by zero and non-numeric inputs. Use if-elif-else to perform the mathematical operation based on the provided operator. Print the result or an appropriate error message.

# 24: number classifier
# Write a program that asks the user to enter a number. Use try-except to ensure that the input is numeric and use if-elif-else to classify the number as "positive", "negative" or "zero". Additionally, identify if the number is "even" or "odd".

# 25: type conversion with validation
# Create a script that asks the user for a list of numbers separated by commas. The program should convert the input string into a list of integers. Use try-except to handle the conversion of each number and validate that each element of the converted list is an integer. If the conversion fails or an element is not an integer, print an error message. If the conversion is successful for all elements, print the list of integers.

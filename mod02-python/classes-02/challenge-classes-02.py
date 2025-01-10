### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# código original da aula anterior

# Code a KPI calculator that ask the user for the following values:
# name, salary and bonus percentage. 
# The program should return the bonus that this person will receive.
# Bonus = 1000 + salary*bonus_percentage
CONST_BONUS = 1000
try:
    name = input("What the person's name? ")
    if name == "":
        raise ValueError("Name cannot be empty")
    if name.isdigit():
        raise ValueError("Name cannot be a number")
    if name.isnumeric():
        raise ValueError("Name cannot be a number")
    if name.isspace():
        raise ValueError("Name cannot be a space")
except ValueError as error:
    print(f"Error: {error}")
else:
    try:
        salary = float(input("What is the salary? "))
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        if salary == 0:
            raise ValueError("Salary cannot be zero")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        try:
            bonus_percentage = float(input("What is the bonus percentage? "))
            if bonus_percentage < 0:
                raise ValueError("Bonus percentage cannot be negative")
            if bonus_percentage == 0:
                raise ValueError("Bonus percentage cannot be zero")
            if bonus_percentage > 1:
                raise ValueError("Bonus percentage cannot be greater than 1")
        except ValueError as error:
            print(f"Error: {error}")
        else:    
            bonus = CONST_BONUS + salary*bonus_percentage
            print(f"The bonus that {name} will receive will be: {bonus} reais")
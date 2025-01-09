print(4 % 3)

car_model = "fusca"

car_model.capitalize()

print(car_model)

print(car_model.capitalize())
car_model = car_model.upper()
print(car_model)
car_model = car_model.split("S")
print(car_model)
print(car_model[0])

print("___________________________________________________")
list_model = ["fusca; ", "gol; ", "palio; ", "uno; "]
print(list_model)
list_model.append("celta")
print(list_model)
list_model.insert(2, "ka")
print(list_model)
list_model.remove("gol; ")
print(list_model)
list_model.pop(2)
print(list_model)
list_model.pop()
print(list_model)
print(list_model)
#list_model.strip()
print(list_model)
#list_model = list_model.join(list_model)

car = (list_model[0].split(";")).pop()
print(car)
#list_model[0] = list_model[0].strip()
print(list_model)
print(car)

if ("fusca; " not in list_model):
    print("The car is not in the list")

if (3 and 6 > 2):
    print("bigger then 2")
    print(3 and 6 > 5) # I am with 3 = True and 6 > 5 = True, so the result is True, but I should have used () to use the > to both numbers

while list_model:
    print(list_model.pop())
    print(f"New list model: {list_model}")

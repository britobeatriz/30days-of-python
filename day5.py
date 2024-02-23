# Booleans: True or False values

# 1.
list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]

print(id(list_1) == id(list_2)) 

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1

print(id(list_1) == id(list_2)) 

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1

print(list_1 is list_2) 

# 2.
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

numbers = [1, 2, 3, 4]
numbers.append(5)

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(numbers is new_numbers)  

numbers = [1, 2, 3, 4]
print(id(numbers))  # 140220707722752

numbers.append(5)
print(id(numbers))  # 140220707722752

numbers = [1, 2, 3, 4]
numbers_copy = numbers

numbers.append(5)

print(numbers is numbers_copy)  # True

# 3.
number = float(input("Put a number: "))
if number > 0:
    print("The number is Positive")
elif number == 0:
    print("The number is Zero")
else:
    print("The number is Negative")

# 4.
name = input("Your name: ")
hours_worked = float(input(f"How many hours did {name}'s hourly wage? "))
hourly_wage = float(input(f"What is {name}'s hourly wage? "))

if hours_worked > 40:
    regular_pay = 40 * hourly_wage
    overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
    owed_pay = int(regular_pay + overtime_pay)

    print(f"{name} is owed ${owed_pay}")
else:
    owed_pay = int(hours_worked * hourly_wage)
    print(f"{name} is owed ${owed_pay}.")
# getting values from the user

# exercises:
# 1. ask the user for their name and age, assign a values
# to two variables, and then print them.
name = input('Ask your name: ')
age = input('Ask your age: ')
print(f"{name} is {age} years old.")

# 2. investigate what happens when you try to assign a value to a
# variable that you've already defined. Try printing the variable
# before and after you reuse the name.
name = "beatriz"
print(name) # the variable overwrites

# Below you’ll find some code with a number of errors. Try to go
# through the program line by line and fix the issues in the code. 
# I’d encourage you to try running the program while you’re working 
# on it, as reading the error messages is great practice for
# debugging your own programs.
hourly_wage = input('Please enter your hourly wage: ')
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)
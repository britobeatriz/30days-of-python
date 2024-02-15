# Formatting Strings and Processing User Input

# 1.
greeting = "Hello, world"
print(f"{greeting}" + "!")

# 2.
name = input("ask me your name: ").strip().title()
greeting = "Hello, "
print(f"{greeting}" + f"{name}" + "!")

# 3.
age = 29
age = str(age)
print(f"I am {age}")

# 4. 
# string interpolation 
title = "Joker"
director = "Todd Phillips"
release_year = 2019
release_year = str(release_year)
print(f"{title}  ({release_year}),  directed by {director}")
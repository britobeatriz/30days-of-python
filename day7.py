# converting tuples and strings

numbers = [1, 2, 3]
numbers = str(numbers)
print(numbers)

# join
project_authors = ["bia", " alan", " vicente"]
project_authors = "," .join(project_authors)
print(f"the people... {project_authors}")

# or

project_authors = ["bia", " alan", " vicente"]
print(f"the people... {','.join(project_authors)}")

numbers = [1, 2, 3]
numbers = str(numbers)
numbers = "".join(numbers)
print(numbers)

numbers = [1, 2, 3]
stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(', '.join(stringified_numbers))

# split
# list
user_numbers = input("Please enter 3 numbers separated by commas: ")
numbers_list = user_numbers.split(",")

print(numbers_list) 

# tuple
user_numbers = input("Please enter 3 numbers separated by commas: ")
numbers_tuple = tuple(user_numbers.split(","))

print(numbers_tuple) 

user_numbers = input("Please enter 5 numbers separated by commas: ") 
user_numbers = user_numbers.split(",")
numbers_list = []
for number in user_numbers:
    numbers_list.append(number.strip())
print(numbers_list) 

sample_string = "Python"
print(list(sample_string)) 
print(tuple(sample_string)) 

# slicing
originalString = "python"
sliced = originalString[3:] 
print(sliced)

# fuction "length" or len
numbers = [1,2]
len(numbers)

# exercises

# 1) Ask the user to enter their given name and surname in 
# response to a single prompt. Use split to extract the names,
#  and then assign each name to a different variable. For this exercise,
#  you can assume that the user has a single given name and a single surname.

full_name = input("enter your first name and surname: ").split()
name = full_name[0]
surname = full_name[1]
print(name)
print(surname)

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using
#  the join method. Remember that you can only join collections of 
# strings, so you’re going to need to do some initial processing
#  of the list of numbers.

numbers = [1, 2, 3, 4, 5]
numbers_strip = []
for number in numbers:
    numbers_strip.append(str(number))
print(" | ".join(numbers_strip))

# 3) Below you’ll find a short list of quotes:
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

# Each quote is a string, but each string actually contains quote
#  characters at the start and end. Using slicing, extract the 
# text from each string, without these extra quote marks, and print
# each quote.
#You may also want to try a solution using strip.

for quote in quotes:
    print(quote.strip("'"))

# or

for quote in quotes:
    print(quote[1:-1])

# 4) Ask the user to enter a word, and then print out the length
#  of the word. You should account for any excess whitespace in
# the user’s input, so you’re going to have to process the string 
# before you find its length.

user_word = input("type a word: ").strip()
length_word = len(user_word)
print(f"the word has {length_word} characters.")
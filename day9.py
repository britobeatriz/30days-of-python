# unpacking, enumeration, and the zip fuction

# unpacking


movie = ("12 angry men", "sidney lumet", 1957)
print(movie)

title = movie[0]
director = movie[1]
year = movie[2]

title, director, year = movie
print(movie)

# unpacking in loops
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

for title, director, year in movies:
    print(f"{title} ({year}), by {director}")

# enumaration
for index in range(len(movies)):
    print(f"{index + 1}. {movies[index][0]} ({movies[index][2]}), by {movies[index][1]}")

counter = 1

for title, director, year in movies:
    print(f"{counter}. {title} ({year}), by {director}")
    counter += 1
    counter = counter + 1

# enumaration function
names = ["harry", "rachel", "brian"]
for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")

# zip function

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
print(pet_owners, pets)

pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))

# zip loops
for owner, pet, in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")

# exercises
# 1) Below is some simple data about characters from BoJack 
# Horseman:
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
# The data contains the character name, the voice actor or actress 
# who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print 
# each tuple:

for actor, voice, species in main_characters:
    print(f"{actor} is a {species} voice by {voice}")

# 2) Unpack the following tuple into 4 variables:
# ("John Smith", 11743, ("Computer Science", "Mathematics"))
# The data represents a student's name, their student id number,
# and their major and minor disciplines in that order.

pack = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, identifier, (major,minor) = pack
print(name)
print(identifier)
print(major)
print(minor)

# 3) Investigate what happens when you try to zip two iterables 
# of different lengths. For example, try to zip a list containing 
# three items, and a tuples containing four items.

letters = ["a", "b", "c"]
numbers = [1, 2]

print(list(zip(letters, numbers)))
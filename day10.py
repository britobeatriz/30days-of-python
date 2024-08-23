# Dictionaries

# defining a dictionary 
student = {"name": "jonh smith"}
# defining a dictionary empty
empty = {}

# A dictionary can have many keys, but each key must be unique inside that dictionary,
# and each key must have a single value. That value can, however, be a collection, including 
# another dictionary.
student = {
    "name": "jhon smith",
    "grades": [88, 76, 92]
}

# acessing values in a dictionary
print(student["grades"])

# method get
print(student.get("grade"))

# method update
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

meta_info = {
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
}

movie.update(meta_info)

# deleting items from a dictionary
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019,
    "runtime": 181
}

del movie["runtime"]
print(movie)

# iterating over dictionaries
for attribute in movie:
    print(attribute)

for value in movie.values():
    print(value)

for key in movie:
    print(f"{key}: {movie[key]}")
# values
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

for attribute in movie:
    print(movie[attribute])

# excercises

# 1) Below is a tuple describing an album:
#  (
#     "The Dark Side of the Moon",
#     "Pink Floyd",
#     1973,
#     (
#         "Speak to Me",
#         "Breathe",
#         "On the Run",
#         "Time",
#         "The Great Gig in the Sky",
#         "Money",
#         "Us and Them",
#         "Any Colour You Like",
#         "Brain Damage",
#         "Eclipse"
#     )
#  )

#Inside the tuple we have the album name, the artist (in this case, 
# the band), the year of release, and then another tuple containing the track list.

#Convert this outer tuple to a dictionary with four keys.

album = {
    "title": "The Dark Side of the Moon",
    "artist" : "Pink Floyd",
    "year": 1973,
    "tracks": (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}
print(album)

#2) Iterate over the keys and values of the dictionary you create in exercise 1.
# For each key and value,
# you should print the name of the key, and then the value alongside it.

for items in album:
    print(f"{items}: {album[items]}")

#3) Delete the track list and year of release from the dictionary you created.
#  Once you've done this, add a new key to the dictionary to store the date of release. The date of release for 
# The Dark Side of the Moon was March 1st, 1973.
# If you use a different album for the exercises, update the date accordingly.

del album["tracks"]
del album["year"]
print(album)

album["date_release"] = "1º de março de 1973"
print(album)

# 4) Try to retrieve one of the values you deleted from the dictionary. This should 
# give you a KeyError. Once you've tried this, 
# repeat the step using the get method to prevent the exception being raised.
# print(album["year"])
print(album.get("year", "Unknown"))
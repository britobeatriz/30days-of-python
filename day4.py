# list: is a object can even mix different types and is a object changeable
# ex: friend_details = ["John", 27, "Web Developer"]
# tuple: one differences between tuples and list is that tuple are immutable
# ex: tuple = (1, 2) or tuple = 1, 2

# 1. 
movies = [
    ("the room", "tommy wiseau", "2003", "$6,000,000")
]

# 2. 
title = input("Title: ")
director_name = input("Director: ")
release_year = input("Year of release: ")
budget = input("Budget ")

# 3.
movie = title, director_name, release_year, budget

# 4.
print(f'{movie[0]} ({movie[2]})')

# 5.
movies.append(movie)

# 6.
print(movies[0])
print(movies[1])

# 7.
movies.pop()
#del movies[0]
print(movies)
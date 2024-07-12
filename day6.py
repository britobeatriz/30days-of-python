# define loop
# a loop is a means of performing some set of operations for 
# each item in a collection
# iterable

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

movie = movies[0]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

movie = movies[1]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

movie = movies[2]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

# or 

print(f"{movies[0][0]} ({movies[0][2]}), by {movies[0][1]}")
print(f"{movies[1][0]} ({movies[1][2]}), by {movies[1][1]}")
print(f"{movies[2][0]} ({movies[2][2]}), by {movies[2][1]}")

# with loop
for movie in movies:
    print(f"{movie[0]}")

# range function
print(list(range(10)))

for number in range(10):
    print(number)

for _ in range(10):
    print("hello world")

# exercises:
# 1) Below we've provided a list of tuples, where each tuple contains details
#  about an employee of a shop: their name, the number of hours worked last week,
#  and their hourly rate. 
#  Print how much each employee is due to be paid at the end of the week in a nice,
#  readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    pay = employee[1] * employee[2]
    #print(f"{employee[0]}")
    print(f"{employee[0]}, receveid: ${pay}")

# 2) For the employees above, print out those who are earning an hourly wage
# above average.

pay_employees = 0
total = len(employees)

for employee in employees:
    em = {employee[1]}  
    #pay_employees.append(em)
    pay_employees += sum(em) 

    average = pay_employees / total 
    if employee[1] > average: 
         print(f"{employee[0]}")
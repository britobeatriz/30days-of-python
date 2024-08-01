# while loops
# A while loop in many ways is quite a bit simpler than a for loop.
# We just need to use the while keyword, followed by some 
# condition to test. If the condition evaluates to a truthy 
# value, the loop will
# run one iteration, and then it will test the condition again.

#while with condition
user_number = input("please enter a number: ")

while int(user_number) < 10:
    print("your number was less than 10.")
    user_number = input("please select another number")

print("your number was at least 10.")

# infinite loops
while True:
    print("Hello there!")
    break

# break
while True:
    selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        print("You selected option 'a'!")
    elif selected_option == "b":
        print("You selected option 'b'!")
    elif selected_option == "c":
        print("You selected option 'c'!")
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break
    else:
        print("you selected an invalid option.") 

# continue
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

# Get a number to test from the user, and set the initial divisor to 2
dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
    #If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break

    # Increment the divisor for the next iteration
    divisor = divisor + 1
else:
   # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

# 1) Write a short guessing game program using a while loop. The user should be 
# prompted to guess a number between 1 and 100, and you should tell them whether 
# their guess was too high or too low after each guess. The loop should keeping 
# running until the user guesses the number correctly.

# target_number = 50
# user_number = int(input("insert number: "))
# while user_number != target_number:
#     print("wrong")
#     user_number = int(input("insert number: "))
# print("you guessed correctly! ")

target_number = 50
user_number = int(input("insert number: "))
while user_number != target_number:
    if user_number > target_number:
        print("too hight ")
    else:
        print("too low")
    user_number = int(input("insert number: "))
print("correctly")

# 2) Use a loop and the continue keyword to print out every character in the string 
# "Python", except the "o". Remember that strings are collections, and they are 
# iterable, so you can iterate over the string, which will yield one character at a 
# time.

word = "python"

for character in word:
    if character == "o":
        continue
    print(character)

# 3) Using one of the examples from earlier—or a solution entirely of your own—create a 
# program that prints out every prime number between 1 and 100.

dividend = int(input("enter a number: "))
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))
print(", ".join(primes))
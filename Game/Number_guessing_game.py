import math
import random

# Asking user for a valid lower bound integer
while True:
    lower_bound = input("Enter a starting range number: ")
    if lower_bound.isdigit():
        lower_bound = int(lower_bound)
        break
    print("Enter a valid number!!")

# Asking user for a valid upper bound integer
while True:
    upper_bound = input("Enter a ending range number: ")
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        if upper_bound > lower_bound:
            break
        print("Entered number is smaller or equals to lower bound")
    print("Enter a valid number!!")

# Storing the system guessed number in a variable
answer = random.randint(lower_bound, upper_bound)


# Function to get a valid number
def guessing():
    while True:
        guessed_num = input("Enter a valid number to check: ")
        if guessed_num.isdigit():
            return int(guessed_num)
        print("Enter a valid number!!")


# Storing Lives in a variable and printing for user to know
lives = math.ceil(math.log(upper_bound - lower_bound + 1, 2))
print(f"You have {lives} Lives")

# Finally Game setup
while True:
    if lives == 0:
        print(f"Game Over :( Try Again... The answer was {answer}")
        break

    guess_num = guessing()

    if guess_num == answer:
        print(f"You have guessed correct answer with {lives} Lives remaining")
        break

    elif guess_num < answer:
        lives -= 1
        print("Try Again! You guessed too small")
        print(f"Lives left {lives}")
    else:
        lives -= 1
        print("Try Again! You guessed too high")
        print(f"Lives left {lives}")

# Importing Libraries
import random

# Storing number to guess
answer = random.randint(1000,10000)

# Creating Fuction to check for a valid input
def check_num():
    while True:
        num = input("Enter a 4 digit number to guess: ")
        if num.isdigit():
            if len(num) == 4:
                return int(num)
            print("Enter only 4 digit number ")
        print("Enter only numbers!")

# Storing firt user input
num = check_num()

# Attempts to record and print later for the user to know
attempt = 0

# Loop to play game until user guess correctly
while True:
    num = str(num)
    answer = str(answer)
    attempt += 1
    count = 0
    code = ['X']*4
    if num == answer:
        print(f"You got the correct answer it was {answer} in {attempt} attempts")
        break

    for i in range(4):
        if num[i] == answer[i]:
            count += 1
            code[i] = num[i]
    if count != 0:
        print(f"Not the quite number. But you did get {count} digits correct!")
        print(code)
        num = check_num()

    else:
        print("None of your answer matched code try again")
        num = check_num()

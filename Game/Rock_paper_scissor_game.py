import random

print("Game Rules are mentioned below: ")
print("Rock vs Paper -> Paper Wins\nPaper vs Scissor -> Scissor Wins\nScissor vs Rock -> Rock Wins\n")


def choice(num):
    if num == 1:
        return "Rock"
    if num == 2:
        return "Paper"
    return "Scissor"


def check_winning(p1, com):
    if p1 == com:
        return 0
    if (p1 == 1 and com == 2) or (p1 == 2 and com == 3) or (p1 == 3 and com == 1):
        return 2
    return 1


def play_again():
    while True:
        play = input("Would you like to play again press 'y' else 'n': ")
        if play.lower() == "n":
            return True

        if play.lower() == "y":
            return False

        print("Invalid Input")


score = 0
games = 0
draw = 0
lose = 0

while True:
    games += 1
    print("Enter Your Choice:\n1 - Rock\n2 - Paper\n3 - Scissor\n")
    while True:
        num = input("Enter your choice: ")
        if num.isdigit():
            if 0 < int(num) < 4:
                num = int(num)
                break
            print("Enter number between 1 to 3.")
        print("Enter a valid number!")

    com = random.randint(1, 3)

    p1_choice = choice(num)
    com_choice = choice(com)

    winner = check_winning(num, com)

    if winner == 0:
        draw += 1
        print(f"Its a draw you both chose same thing {p1_choice}")
        dont_play = play_again()
        if dont_play:
            break
    elif winner == 2:
        lose += 1
        print(f"Computer wins since it chose {com_choice} and you chose {p1_choice}")
        dont_play = play_again()
        if dont_play:
            break
    else:
        score += 1
        print(f"You won since you chose {com_choice} and computer chose {p1_choice}")
        dont_play = play_again()
        if dont_play:
            break

print(f"You played total {games} games in which you won {score} times | lost {lose} times | Draw {draw} times")

import random

text_file = open("words.txt")
list_words = list(text_file)


def hangman_prototype(life):
    if life == 7:
        hangman = '''
        ______________________
        |       
        |       
        |      
        |      
        |
        -----------------------
        '''
        return hangman

    elif life == 6:
        hangman = '''
        ______________________
        |           |
        |       
        |      
        |      
        |
        -----------------------
        '''
        return hangman

    elif life == 5:
        hangman = '''
        ______________________
        |          |
        |          O
        |      
        |      
        |
        -----------------------
        '''
        return hangman

    elif life == 4:
        hangman = '''
                ______________________
                |          |
                |          O
                |          |
                |      
                |
                -----------------------
                '''
        return hangman

    elif life == 3:
        hangman = '''
                ______________________
                |          |
                |          O
                |         /|
                |      
                |
                -----------------------
                '''
        return hangman

    elif life == 2:
        hangman = '''
                ______________________
                |          |
                |          O
                |         /|\\
                |      
                |
                -----------------------
                '''
        return hangman

    elif life == 1:
        hangman = '''
                ______________________
                |          |
                |          O
                |         /|\\
                |         /
                |
                -----------------------
                '''
        return hangman

    else:
        hangman = '''
                ______________________
                |          |
                |          O
                |         -|-
                |         / \\
                |
                -----------------------
                '''
        return hangman


choice = random.choice(list_words)

lives = 7

ans = ""

for _ in range(len(choice)):
    ans += "_"

print(f"The word you need to guess has {len(choice)} alphabet")

an = ""


def guess():
    wor = input("Enter a alphabet to guess word: ")
    return wor


choice_list = list(choice)
ans_list = list(ans)
print(f"You have {lives} lives remaining")
guessed = []


def check_word():
    while True:
        guess_wor = str(guess()).lower()
        if len(guess_wor) > 1 or len(guess_wor) < 1:
            print("You have entered more than 1 or less than 1 alphabet try again")
        else:
            break
    return guess_wor


while True:
    if lives < 1:
        hang = hangman_prototype(lives)
        print(hang)
        print(f"You lost the game the word was {choice}.")
        break
    else:
        if "_" in ans_list:
            guess_word = check_word()
            if guess_word in guessed:
                print("You have already guessed word try again.")
                print(f"Guessed alphabet: {guessed}")
                guess_word = guess().lower()
            else:
                guessed.append(guess_word)
            if guess_word in choice_list:
                for i, letter in enumerate(choice_list):
                    if letter == guess_word:
                        ans_list[i] = guess_word
            else:
                lives -= 1
            n = "".join([str(a) for a in ans_list])
            hang = hangman_prototype(lives)
            print(hang)
            print(n)
            print(f"Guessed alphabet: {guessed}")
            print(f"You have {lives} lives left.")
        else:
            print(f"You have successfully guessed the word with {lives} lives left.")
            print(f"As you guessed the word was {choice}.")
            break

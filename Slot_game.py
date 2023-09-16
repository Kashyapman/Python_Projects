import random

MIN_LINE = 1
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

symbol_count = {
    "Mango": 2,
    "Apple": 4,
    "Banana": 6,
    "Pineapple": 8
}

symbol_value = {
    "Mango": 5,
    "Apple": 4,
    "Banana": 3,
    "Pineapple": 2
}


def get_slot_machine(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_counts in symbols.items():
        for _ in range(symbol_counts):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_columns = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_columns)
            current_columns.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

    print()


def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_line.append(line + 1)

    return winnings, winning_line


def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Please enter a valid amount since you just entered an amount less than $1.")
            else:
                print(f"You have just deposited ${amount}")
                break
        else:
            print("Try again as you have not entered number!")
    return amount


def get_bet():
    while True:
        amount = input("Enter the bet amount: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print(f"You have just bet ${amount} for each line")
                break
            else:
                print("Please enter a valid amount since you just entered an amount less than $1 or greater than $100.")

        else:
            print("Try again as you have not entered number!")
    return amount


def bet_on_lines():
    while True:
        lines = input(f"Enter lines you want to bet on from {MIN_LINE} - {MAX_LINE}: ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINE <= lines <= MAX_LINE:
                print(f"You have just decided to bet on {lines}")
                break
            else:
                print("Please enter a valid line since you just entered line out of range.")

        else:
            print("Try again as you have not entered number!")
    return lines


def spin(balance):
    line = bet_on_lines()
    bet = get_bet()
    while True:
        total_bet = bet * line
        if balance < total_bet:
            print(f"Your bet is more than balance. You have ${balance} and you just tried to bet ${total_bet}")
            more_balance = input("Do you want to add more balance if yes type yes else no or y else n. : ")
            if more_balance.lower() == "yes" or more_balance.lower() == "y":
                while True:
                    add_bal = deposit()
                    balance += add_bal
                    if add_bal < (total_bet - balance):
                        print("Sorry the amount you just added is less please enter again.")
                        rem = total_bet - balance
                        print(f"Please add more ${rem} to continue")
                    else:
                        break
            elif more_balance.lower() == "no" or more_balance.lower() == "n":
                spin(balance)
                break
            else:
                print("Sorry your input was not correct try again")
        else:
            break
    print(f"You have bet ${bet} on {line} lines and your total bet is ${total_bet}")
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winnings_line = check_winnings(slots, line, bet, symbol_value)
    print(f"You just won ${winnings}.")
    print("You have won on lines:", *winnings_line)
    print()
    rem_bal = balance + (winnings - total_bet)
    return rem_bal


def main():
    global rem_bal
    balance = deposit()
    while True:
        answer = input("Press Enter to play or q to quit. ")
        if answer.lower() == "q":
            break
        rem_bal = spin(balance)
        print(f"Your current balance is ${rem_bal}.")
    print(f"You are leaving with ${rem_bal}")


main()

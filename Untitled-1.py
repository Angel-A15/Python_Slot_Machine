MAX_LINES = 3


# Function will allow the user to interact with the interface order to add credits
def deposit():
    while True:
        amount = input("What would like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function will allow the user to interact with the interface order to add number of lines
def get_number_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + "). ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def main():
    balance = deposit()
    lines = get_number_lines()
    print(balance, lines)

main()


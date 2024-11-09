
# Function will allow the user to interact with in order to add credits
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

deposit()


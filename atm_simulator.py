
# Simple ATM Simulator
# Skillnexis Week 1 Project

# Account details
correct_pin = "1234"
balance = 5000.0


# Check Balance Function
def check_balance():
    print("\n-------------------------")
    print("      CHECK BALANCE")
    print("-------------------------")
    print("Your balance is: ₹", balance)


# Deposit Function
def deposit():
    global balance

    amount = float(input("\nEnter amount to deposit: ₹"))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)
    else:
        print("Invalid amount!")


# Withdraw Function
def withdraw():
    global balance

    amount = float(input("\nEnter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance: ₹", balance)


# -------------------------
# ATM LOGIN
# -------------------------

print("==============================")
print("      WELCOME TO SIMPLE ATM")
print("==============================")

pin = input("Enter your PIN: ")


# Check PIN
if pin == correct_pin:

    print("\nLogin successful!")

    # -------------------------
    # ATM MENU
    # -------------------------

    while True:

        print("\n==============================")
        print("          ATM MENU")
        print("==============================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice: ")


        # Check Balance
        if choice == "1":
            check_balance()


        # Deposit
        elif choice == "2":
            deposit()


        # Withdraw
        elif choice == "3":
            withdraw()


        # Exit
        elif choice == "4":
            print("\nThank you for using the ATM!")
            print("Have a nice day!")
            break


        # Invalid Choice
        else:
            print("\nInvalid choice!")
            print("Please select 1, 2, 3, or 4.")


# Wrong PIN
else:
    print("\nIncorrect PIN!")
    print("Access denied.")


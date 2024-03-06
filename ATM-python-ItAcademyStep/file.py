import os

file_path = "accounts.txt"

def main():
    if not os.path.exists(file_path):
        create_default_file()

    while True:
        print("Welcome to the ATM application!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                print("Thank you for using the ATM application. Goodbye!")
                return
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        print()

def create_default_file():
    try:
        with open(file_path, "w") as writer:
            writer.write("dima,1000.00\n")
            writer.write("gio,500.00\n")
    except Exception as ex:
        print(f"Error creating default accounts file: {ex}")

def check_balance():
    print("Checking balance...")
    username = get_username()
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == username:
                    print(f"Your balance is: {parts[1]}")
                    return
            print("User not found.")
            response = input("Would you like to add a new user? (yes/no): ").lower()
            if response == "yes":
                add_new_user(username)
    except Exception as ex:
        print(f"Error reading account data: {ex}")

def add_new_user(username):
    try:
        initial_balance = input("Enter initial balance for the new user: ")
        with open(file_path, "a") as writer:
            writer.write(f"{username},{initial_balance}\n")
            print("New user added successfully.")
    except Exception as ex:
        print(f"Error adding new user: {ex}")

def deposit():
    print("Depositing money...")
    username = get_username()
    amount = input("Enter amount to deposit: ")
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                parts = line.strip().split(',')
                if parts[0] == username:
                    balance = float(parts[1])
                    balance += float(amount)
                    lines[i] = f"{username},{balance}\n"
                    with open(file_path, "w") as writer:
                        writer.writelines(lines)
                    print("Deposit successful.")
                    return
            print("User not found.")
    except Exception as ex:
        print(f"Error updating account data: {ex}")

def withdraw():
    print("Withdrawing money...")
    username = get_username()
    amount = input("Enter amount to withdraw: ")
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                parts = line.strip().split(',')
                if parts[0] == username:
                    balance = float(parts[1])
                    if balance >= float(amount):
                        balance -= float(amount)
                        lines[i] = f"{username},{balance}\n"
                        with open(file_path, "w") as writer:
                            writer.writelines(lines)
                        print("Withdrawal successful.")
                        return
                    else:
                        print("Insufficient balance.")
                        return
            print("User not found.")
    except Exception as ex:
        print(f"Error updating account data: {ex}")

def get_username():
    return input("Enter username: ")

if __name__ == "__main__":
    main()

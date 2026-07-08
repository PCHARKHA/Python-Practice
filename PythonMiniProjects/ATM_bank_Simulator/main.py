import datetime

accounts = {
    "1001": {
        "name": "Pranjal",
        "pin": "1234",
        "balance": 5000,
        "failed_attempts":0,
        "locked":False,
        "history": []
    },
    "1002": {
        "name": "Aman",
        "pin": "5678",
        "balance": 10000,
        "failed_attempts":0,
        "locked":False,
        "history": []
    }
}

def create_account():
    name =input("Enter name of account holder: ")
    try :
        init_deposit =int(input("Enter initial deposit amount: "))
        if init_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        else:
            pin = input("Enter a 4-digit PIN: ")
        
            account_number = str(len(accounts) + 1001)

            accounts[account_number] = {
                "name": name,
                "pin": pin,
                "balance": init_deposit,
                "failed_attempts": 0,
                "locked": False,
                "history": []
            }

            print("\nAccount Created Successfully!")
            print(f"Account Number: {account_number}")
            print(f"Name: {name}")
            print(f"Balance: ₹{init_deposit}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

def login():
    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    account = accounts[account_number]

    if account["locked"]:
        print("Account is locked.")
        return

    pin = input("Enter PIN: ")

    if pin == account["pin"]:
        account["failed_attempts"] = 0
        print("Login Successful")
        return account
    
    else:
        account["failed_attempts"] += 1

        if account["failed_attempts"] >= 3:
            account["locked"] = True
            print("Account Locked")
            return None

        else:
            remaining = 3 - account["failed_attempts"]
            print(f"Wrong PIN. {remaining} attempts left.")

def check_balance(account):
    print(f"Current balance is: ₹{account['balance']}")

def deposit(account):
    while True:
        try:
            deposit_amount = int(input("Enter amount to be deposited: "))
            if deposit_amount > 0:
                account["balance"]+=deposit_amount
                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
                account["history"].append(f"{timestamp} - Deposited ₹{deposit_amount}")
                print(f"{deposit_amount} deposited successfully. \n Updated account balance = {account['balance']}")
                break
   
            else:
                print("Invalid amount. Please enter a positive amount.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def withdraw(account):
    while True:
        try:
            withdraw_amount = int(input("Enter amount to be withdrawn: "))

            if withdraw_amount > 0 and withdraw_amount <= account['balance']:
                account["balance"] -= withdraw_amount
                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
                account["history"].append(f"{timestamp} - Withdrew ₹{withdraw_amount}")
                print(f"{withdraw_amount} withdrawn successfully.\nUpdated account balance = {account['balance']}")
                break

            else:
                if withdraw_amount <= 0:
                    print("Please enter a positive amount.")

                elif withdraw_amount > account['balance']:
                    print("Insufficient balance.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def change_pin(account):
    current_pin = input("Enter current PIN: ")

    if current_pin != account['pin']:
        print("Incorrect PIN")

    else:
        while True:
            new_pin = input("Enter new PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():

                if new_pin == current_pin:
                    print("New PIN and current PIN cannot be the same.")

                else:
                    account['pin'] = new_pin
                    print("PIN changed successfully.")
                    break

            else:
                if len(new_pin) != 4:
                    print("PIN should be exactly 4 digits.")

                elif not new_pin.isdigit():
                    print("PIN should contain only digits.")

def transfer_money(account):
    receiver_account_number = input("Enter receiver's account number: ")

    if receiver_account_number not in accounts:
        print("Receiver account not found.")
        return

    receiver_account = accounts[receiver_account_number]

    if receiver_account == account:
        print("You cannot transfer money to your own account.")
        return

    while True:
        try:
            transfer_amount = int(input("Enter amount to be transferred: "))

            if transfer_amount > 0 and transfer_amount <= account['balance']:
                account["balance"] -= transfer_amount
                receiver_account["balance"] += transfer_amount
                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

                account["history"].append(
                f"{timestamp} - Transferred ₹{transfer_amount} to {receiver_account['name']}")

                receiver_account["history"].append(
                f"{timestamp} - Received ₹{transfer_amount} from {account['name']}")

                print(f"₹{transfer_amount} transferred successfully to {receiver_account['name']}.")
                print(f"Updated Balance: ₹{account['balance']}")
                break

            else:
                if transfer_amount <= 0:
                    print("Please enter a positive amount.")

                elif transfer_amount > account['balance']:
                    print("Insufficient balance.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def transaction_history(account):
    print("\n========== TRANSACTION HISTORY ==========")

    if len(account["history"]) == 0:
        print("No transactions found.")

    else:
        for transaction in account["history"]:
            print(transaction)

logged_in_account = None
while True:
    print("\n========== ATM MENU ==========")
    print("1. Create Account")
    print("2. Login")
    print("3. Check Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Change PIN")
    print("7. Transfer money")
    print("8. Transaction History")
    print("9. Logout")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        if logged_in_account:
            print(f"{logged_in_account['name']} is already logged in.")
        else:
            logged_in_account = login()

    elif choice == "3":
        if logged_in_account:
            check_balance(logged_in_account)
        else:
            print("Please login first.")

    elif choice == "4":
        if logged_in_account:
            deposit(logged_in_account)
        else:
            print("Please login first.")

    elif choice == "5":
        if logged_in_account:
            withdraw(logged_in_account)
        else:
            print("Please login first.")

    elif choice == "6":
        if logged_in_account:
            change_pin(logged_in_account)
        else:
            print("Please login first.")

    elif choice == "7":
        if logged_in_account:
            transfer_money(logged_in_account)
        else:
            print("Please login first.")
    
    elif choice == "8":
        if logged_in_account:
            transaction_history(logged_in_account)
        else:
            print("Please login first.")

    elif choice == "9":
        if logged_in_account:
            print(f"{logged_in_account['name']} logged out successfully.")
            logged_in_account = None
        else:
            print("No user is currently logged in.")

    elif choice == "10":
        print("Thank you for using the ATM Simulator!")
        break

    else:
        print("Invalid choice. Please try again.")

    
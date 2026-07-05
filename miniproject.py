import random
import datetime


accounts = {
    "1001": {
        "name": "Aravind",
        "pin": "1234",
        "balance": 17000,
        "history": []
    },
    "1002": {
        "name": "Siva",
        "pin": "2345",
        "balance": 1,
        "history": []
    },
    "1003": {
        "name": "Pravesh",
        "pin": "3456",
        "balance": 0,
        "history": []
    },
    "1004": {
        "name": "Karthik",
        "pin": "4567",
        "balance": 30,
        "history": []
    },
    "1005": {
        "name": "Ananya",
        "pin": "5678",
        "balance": 15000,
        "history": []
    },
    "1006": {
        "name": "Vikram",
        "pin": "6789",
        "balance": 7200,
        "history": []
    },
    "1007": {
        "name": "Sneha",
        "pin": "7890",
        "balance": 6400,
        "history": []
    },
    "1008": {
        "name": "Rohan",
        "pin": "8901",
        "balance": 9800,
        "history": []
    },
    "1009": {
        "name": "Meera",
        "pin": "9012",
        "balance": 4300,
        "history": []
    },
    "1010": {
        "name": "Aditya",
        "pin": "0123",
        "balance": 11000,
        "history": []
    }
}

def login():
    attempts=0
    while attempts < 3:
        acc_no=(input("Enter your account number:"))
        pin=(input("Enter your pin: "))

        if acc_no in accounts:
            if pin==accounts[acc_no]["pin"]:
                print("Login Successful, welcome",accounts[acc_no]["name"])
                return acc_no

            else:
                print('''login failed!
                        enter the correct pin
                        remaining attempts: ''', 3-(attempts+1))
                attempts+=1

        else:
            print('''login failed!
                      account doesnt exist''')
            break


    if attempts>=3:
        print("Atempts over, cant try again")
current_account=login()

def check_balance(current_account):

    print("Your Balance is: ",accounts[current_account]["balance"])

def deposit(current_account):
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

    deposit=int(input("Enter an amount to deposit:"))
    if deposit >=0:
        accounts[current_account]["balance"]+=deposit
        print("Your Balance is: ",accounts[current_account]["balance"])
        accounts[current_account]["history"].append(f"deposited {deposit} at [{time}]")

        recipt=input('Do you want a receipt? (y/n)')
        if recipt=="y":
            transaction_id = random.randint(100000, 999999)
            time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

            print("=" * 40)
            print("        TRANSACTION RECEIPT")
            print("=" * 40)

            print("Transaction ID :", transaction_id)
            print("Date & Time    :", time)
            print("Transaction    :", "deposited")
            print("Amount         : ₹", deposit)
            print("Balance        : ₹", accounts[current_account]["balance"])

            print("=" * 40)
            print("Thank you for banking with AURA ATM!")
            print("=" * 40)

        else:
            pass
    else:
        print("You cant use negative money")

def withdraw(current_account):
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
    withdraw=int(input("Enter an amount to withdraw:"))
    if withdraw>=0:
        if withdraw<=accounts[current_account]["balance"]:
            accounts[current_account]["balance"]-=withdraw
            print("Withdrew", withdraw)
            print("Your Balance is: ",accounts[current_account]["balance"])
            accounts[current_account]["history"].append(f"withdrew {withdraw} at [{time}]")
            recipt = input('Do you want a receipt? (y/n)')
            if recipt == "y":
                transaction_id = random.randint(100000, 999999)
                time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

                print("=" * 40)
                print("        TRANSACTION RECEIPT")
                print("=" * 40)

                print("Transaction ID :", transaction_id)
                print("Date & Time    :", time)
                print("Transaction    :", "withdrawal")
                print("Amount         : ₹", withdraw)
                print("Balance        : ₹", accounts[current_account]["balance"])

                print("=" * 40)
                print("Thank you for banking with AURA ATM!")
                print("=" * 40)


            else:
                pass
    elif withdraw<0:
        print("You cant use negative money")
    else:
        print('''withdraw failed!
                 you dont have enough balance to withdraw''')

def transfer(current_account):
    recipient=input("enter reciptent acoount number")
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

    if recipient in accounts:
        transfer = int(input("Enter an amount to transfer:"))
        if transfer>=0:
            if transfer<=accounts[current_account]["balance"]:
                accounts[recipient]["balance"]+=transfer
                accounts[current_account]["balance"]-=transfer
                print("Transfered", accounts[current_account]["balance"],"to",accounts[recipient]["name"])
                print("Your Balance is: ",accounts[current_account]["balance"])
                accounts[current_account]["history"].append(f"transfered {transfer} to {accounts[recipient]["name"]} at [{time}]")
                accounts[recipient]["history"].append(
                    f"Received {transfer} from {current_account} at [{time}]"
                    )
                recipt = input('Do you want a receipt? (y/n)')
                if recipt == "y":
                    transaction_id = random.randint(100000, 999999)
                    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

                    print("=" * 40)
                    print("        TRANSACTION RECEIPT")
                    print("=" * 40)

                    print("Transaction ID :", transaction_id)
                    print("Date & Time    :", time)
                    print("Transaction    :","transfer")
                    print("From           :", accounts[current_account]["name"])
                    print("To             :", accounts[recipient]["name"])
                    print("Amount         :", transfer)
                    print("Balance        :", accounts[current_account]["balance"])

                    print("=" * 40)
                    print("Thank you for banking with AURA ATM!")
                    print("=" * 40)


                else:
                    pass
        elif transfer<0:
                print("You cant use negative money")
        else:
            print("transfer failed!You dont have enough balance to transfer")

    else:
        print("Recipient account not found!")

def transaction_history(current_account):
    if not accounts[current_account]["history"]:
        print("No transactions yet.")
    else:
        for transaction in accounts[current_account]["history"]:
            print(transaction)

def change_pin(current_account):
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
    otp=random.randint(1000, 9999)
    print("An otp has been sent to the phone number registered to you account")
    print("otp recieved:", otp)
    p=int(input("Enter the recieved otp:"))
    if p==otp:
        newpin=input("Enter your new pin:")
        if not len(str(newpin))==4 and newpin.isdigit():
            print("Pin not valid! Enter a four digit number")
            accounts[current_account]["history"].append(
                f"PIN changed at [{time}]"
            )
        else:
            print(f"Your pin has been changed to {newpin}")
            accounts[current_account]["pin"]=newpin
            accounts[current_account]["history"].append(
                f"PIN change attempt at [{time} but not changed]"
            )

    else:
        print("Incorrect OTP! PIN not changed.")

def menu(current_account):
    while True:
        print("""
        ========================================
                      AURA ATM
        ========================================
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Transfer Money
        5. Transaction History
        6. Change PIN
        7. Logout
        ========================================
        """)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            check_balance(current_account)

        elif choice == "2":
            deposit(current_account)

        elif choice == "3":
            withdraw(current_account)

        elif choice == "4":
            transfer(current_account)

        elif choice == "5":
            transaction_history(current_account)

        elif choice == "6":
            change_pin(current_account)

        elif choice == "7":
            print("Logging out...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if current_account:
    menu(current_account)




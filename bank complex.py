# a bank program simulation with a menu driven system 

from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self):
        amount = self.get_valid_int("Enter amount to deposit: ")
        self.balance += amount
        print(f"You have deposited {amount}. New balance: {self.balance}")

    def withdraw(self):
        amount = self.get_valid_int("Enter the amount to withdraw: ")
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

    def customer_details(self):
        print("\nAccount Details")
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

    @staticmethod
    def get_valid_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

#a function to handle invalid input error
def get_valid_date():
    while True:
        date_input = input("Enter the date of account opening (DD-MM-YYYY): ")
        try:
            valid_date = datetime.strptime(date_input, "%d-%m-%Y").strftime("%d-%b-%Y")
            return valid_date
        except ValueError:
            print("Invalid date format! Please enter in DD-MM-YYYY format.")

account_number = BankAccount.get_valid_int("Enter your account number: ")
balance = BankAccount.get_valid_int("Enter the balance: ")
name = input("Enter your name: ")
date_of_opening = get_valid_date()  

#Creating the account
my_account = BankAccount(account_number, balance, date_of_opening, name)

# Menu Loop
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Account Details\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        my_account.deposit()
    elif choice == "2":
        my_account.withdraw()
    elif choice == "3":
        my_account.check_balance()
    elif choice == "4":
        my_account.customer_details()
    elif choice == "5":
        print("Exiting... Thank you for using the bank system!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

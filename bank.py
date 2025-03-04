# bank account: a program that performs the basic operations of a bank i.e deposit, withdraw and check balance

class bankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self):
        deposit = int(input("Enter amount to deposit: "))
        self.balance += deposit
        return f"you have deposited {deposit} and your new balance is {self.balance}"
    def withdraw(self):
        amount = int(input("\nEnter the amount to withdraw: "))
        if self.balance < amount:
            return "\ninsuffucient balance"
        else:
            self.balance -= amount
            return f"\nyou have withdrawn {amount} and your balance is {self.balance}"
    def check_balance(self):
        return f"your current balance is {self.balance}"
    def customer_details(self):
        return f"\nAccount Details\n Name: {self.customer_name}\n account number: {self.account_number}\n Date of opening: {self.date_of_opening}\n Balance: {self.balance} "
    
my_account = bankAccount(219257834, 5000, "27th Feb 2025", "maria" )
print(my_account.deposit())
print(my_account.withdraw())
print(my_account.check_balance())
print(my_account.customer_details())
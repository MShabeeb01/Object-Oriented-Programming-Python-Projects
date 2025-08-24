# Mega project based on entire OOPS Principles 
'''
The ATM Machine will allow users  to:
•Authenticate with PINs securely
•Check account balance
•Deposit money
•Withdraw money with balance validation
•Change PIN
'''
#Concepts Used 
'''
• Encapsulation : Secure PIN handling and balance access
• Static Method: For utility task like PIN validation
• Class Method : To maintain account level settings
• Polymorphism : Flexibility in transaction operations
'''

# Mini ATM Machine

import json
import os

# Bank Account Class
class BankAccount:
    def __init__(self, account_number, pin, balance=0, transactions=None):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.transactions = transactions if transactions else []

    # Validate PIN
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin

    # Check balance
    def check_balance(self):
        print(f"Current balance: {self.__balance}")
        self.transactions.append(f"Checked balance: {self.__balance}")

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
            self.transactions.append(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient Funds.")
            self.transactions.append(f"Failed withdrawal {amount} - Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
            self.transactions.append(f"Withdrew {amount}")

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN changed successfully!")
            self.transactions.append("PIN changed successfully")
        else:
            print("Failed to change PIN. Ensure old PIN is correct and new PIN is 4 digits.")
            self.transactions.append("Failed PIN change attempt")

    # Convert to dict (for saving in JSON)
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "pin": self.__pin,
            "balance": self.__balance,
            "transactions": self.transactions
        }


# ATM Class
class ATM:
    def __init__(self, filename="atm.json"):
        self.filename = filename
        self.accounts = self.load_accounts()

    # Load accounts from atm.json
    def load_accounts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                accounts = {}
                for acc_num, acc_data in data.items():
                    accounts[acc_num] = BankAccount(
                        acc_data["account_number"],
                        acc_data["pin"],
                        acc_data["balance"],
                        acc_data["transactions"]
                    )
                return accounts
        return {}

    # Save accounts to atm.json
    def save_accounts(self):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    # Create account
    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account already exists!")
            return

        pin = input("Set a 4 digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            self.save_accounts()
            print("Account created successfully.")
        else:
            print("Invalid PIN. PIN must be 4 digits.")

    # Authenticate Account
    def authenticate_account(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentication Successful.")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN.")

    # Account Menu
    def account_menu(self, account):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                account.check_balance()
                self.save_accounts()
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                self.save_accounts()
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                self.save_accounts()
            elif choice == "4":
                old_pin = input("Enter old pin: ")
                new_pin = input("Enter new pin: ")
                account.change_pin(old_pin, new_pin)
                self.save_accounts()
            elif choice == "5":
                print("\n--- Transaction History ---")
                for t in account.transactions:
                    print("-", t)
            elif choice == "6":
                print("Logging out. Thank you for using our ATM.")
                self.save_accounts()
                break
            else:
                print("Invalid choice.")

    # Main Menu
    def main_menu(self):
        while True:
            print("\n--- Welcome to ATM Machine ---")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.authenticate_account()
            elif choice == "3":
                print("Thank you for using Mini ATM Machine. Goodbye!")
                break
            else:
                print("Invalid choice.")


# Start the ATM
if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()

import random

# Parent class
class Bank:
    def __init__(self):
        self.username = None
        self.password = None
        self.account_number = None
        self.balance = 0.0

    def create_account(self):
        self.username = input("Enter your username: ")
        self.password = input("Set your password: ")
        self.balance = float(input("Enter initial deposit amount (₹): "))
        self.account_number = str(random.randint(1000000000, 9999999999))  # 10-digit number

        print("\nAccount created successfully.")
        print(f"Username      : {self.username}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance       : ₹{self.balance}")

# Child class
class BankOperations(Bank):
    def login(self):
        uname = input("Enter your username: ")
        pwd = input("Enter your password: ")
        if uname == self.username and pwd == self.password:
            print(f"\nLogin successful. Welcome, {self.username}.")
            return True
        else:
            print("Incorrect username or password.")
            return False

    def deposit(self):
        amount = float(input("Enter amount to deposit (₹): "))
        self.balance += amount
        print(f"{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw (₹): "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def view_details(self):
        print("\nAccount Details")
        print(f"Username      : {self.username}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance       : ₹{self.balance}")

    def update_password(self):
        old_pwd = input("Enter current password: ")
        if old_pwd == self.password:
            new_pwd = input("Enter new password: ")
            self.password = new_pwd
            print("Password updated successfully.")
        else:
            print("Incorrect current password.")

# Main program
def main():
    bank = BankOperations()
    account_created = False

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if not account_created:
                bank.create_account()
                account_created = True
            else:
                print("Account already created. Only one user allowed.")

        elif choice == '2':
            if not account_created:
                print("No account found. Please create one first.")
                continue
            if bank.login():
                while True:
                    print("\n--- Account Operations ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. View Account Details")
                    print("5. Update Password")
                    print("6. Logout")
                    op = input("Choose an operation: ")

                    if op == '1':
                        bank.deposit()
                    elif op == '2':
                        bank.withdraw()
                    elif op == '3':
                        bank.check_balance()
                    elif op == '4':
                        bank.view_details()
                    elif op == '5':
                        bank.update_password()
                    elif op == '6':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")

        elif choice == '3':
            print("Exiting. Thank you.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# ATM program using python function
def atm_menu():
    # displays the atm menu
    print("\n Welcome To Atm")
    print("1.check balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exit")
def check_balance(balance):
    # displays the current account balance
    print(f"Your  Account Balance is: ${balance}")
def withdraw(balance,amount):
    #withdraws money from the account.
    if amount<balance:
        balance-=amount
        print(f" Withdrawl Successful. your account balance is {balance} rupees")
    else:
        print("insufficient amount.")
        return balance
def deposit(balance,amount):
    #credits money into the account.
    if amount>0:
        balance+=amount
        print(f" Deposit Successful.Your account is credited with {amount} Rupees")
        print(f"Your current account baslance is {balance} Rupees")
        return balance
    else:
        print("please enter positive amount only")
def atm_program():
    #Runs The ATM Program
    balance=1000
    while True:
        atm_menu()
        choice=int(input("please enter your choice(1-4):"))
        if choice==1:
            check_balance(balance)
        elif choice==2:
            amount=int(input("enter withdrawl amount:"))
            balance=withdraw(balance,amount)
        elif choice==3:
            amount=int(input("enter amount to deposit:"))
            balance=deposit(balance,amount)
        elif choice==4:
            print("Thank You For Using The ATM")
            break
        else:
            print("invalid choice")
atm_program()
    


        
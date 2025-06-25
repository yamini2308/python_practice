class ATM():
    def __init__(self,user_name,pin,balance):
        self.user_name=user_name
        self.pin=pin
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"your account is credited with {amount} rupees")
        print(f"your current account balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance-=amount
            print(f"withdrawl successful.{amount} rupees is debited from your account.")
            print(f"your current account balance is {self.balance} rupees")
    def check_balance(self):
        print(f"your current account balance is {self.balance} rupees")
    def change_pin(self,new_pin):
        new_pin=int(input("enter your new pin:"))
        self.pin=new_pin
        print("pin changed successfully")   
    def run(self):
        user_name="john"
        pin=1234
        balance=1000
        atm=ATM(user_name,pin,balance)
        pin=int(input("please enter your pin:"))
        while True:
            if pin==self.pin:
                print("welcome to ATM")
                print("1.check balance")
                print("2.deposit money")
                print("3.withdrawl money")
                print("4.change pin")
                print("5.exit")
                choice=int(input("please enter your choice:"))
                if choice==1:
                    atm.check_balance()
                elif choice==2:
                    amount=int(input("please enter your amount:"))
                    atm.deposit(amount)
                elif choice==3:
                    amount=int(input("enter withdrawl amount:"))
                    atm.withdraw(amount)
                elif choice==4:
                    atm.change_pin("new_pin")
                elif choice==5:
                    print("Thank You..")
                    break
                else:
                    print("invalid choice. please try again")
            else:
                print("you entered wrong pin. please try again")
                break
user_name="john"
pin=1234
balance=1000
atm=ATM(user_name,pin,balance)
atm.run()

        
    
    


                
                


         
    

    
#SUPERMARKET BILL GENERATION
import datetime
now=datetime.datetime.now()
date_time=now.strftime("%Y-%m-%d %H:%M:%S")
name=input("enter your name:")
#list of items
lists='''
milk      70/lit
paneer    300/kg
bread     45/pac
juice     30/lit
rice      25/kg
mango     100/kg
jam       150/bottle
egg       6/each
papaya    40/each
oil       150/lit
'''
items={"milk":70,"paneer":300,"bread":45,"juice":30,"rice":25,"mango":100,
"jam":150,"egg":6,"papaya":40,"oil":150}
#DECLARATIONS
price=0
total_price=0
discount_price=0
final_price=0
products_list=[]
option=int(input("press 1 to show list of items or 2 to exit:"))
while True:
    if option==2:
        print("Thank You Visit Again.")
        break
    elif option==1:
        print(lists)
        choice=int(input("choice 1 to buy or 2 to exit:"))
        while True:
            item=input("enter item to buy:")
            quantity=int(input("enter quantity of item:"))
            if item in items.keys():
                price=items[item]*quantity
                products_list.append((item,quantity,price))
            else:
                print(f"sorry {item} is out of stock")
            select=input("can i bill yes or no:")
            if select=="no":
                pass
            elif select=="yes":
                print("*"*10,"Sri Rama SuperMarket","*"*10 )
                print("            ","Ongole")
                print("       ","ph.no:9999999999")
                print("-"*40)
                print(f"customer_name:{name}\tdate:{date_time}")
                print("-"*40)
                print(f"item\tquantity\tprice")
                for i,j,k in products_list:
                    print(f"{i}\t{j}\t\t{k}")
                    total_price+=k
                    discount_price+=total_price*5/100
                    final_price=total_price-discount_price
                print("-"*40)
                print(f"total_price\t\t{total_price}")
                print(f"you save {discount_price} rupees by 5% discount")
                print(f"final_price\t\t{final_price}")
                print("********* Thank you for shopping visit again********")
                break
            
        break
    break





    

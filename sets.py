#SUPERMARKET BILL GENERATION USING PYTHON
print("**********SRI RAMA SUPER-MARKET************")
print("               ","ongole")
print("           ","ph.no:9999999999")
print("="*50)
name=input("customer name:")
#LIST OF ITEMS
lists='''
Milk       35/packet
Sugar      40/kg
Bread      35/packet
Dates      200/box
Rice       18/kg
Oil        150/lit
Mango      200/kg
Orange     100/kg
Papaya     50/piece
Juice      150/bottle
'''
#DECLARATIONS
price=0
product_list=[]
total_price=0
final_price=0
item_list=[]
quantity_list=[]
price_list=[]
items={"Milk":35,
"Sugar":40,
"Bread":35,
"Dates":200,
"Rice":18,
"Oil":150,
"Mango":200,
"Orange":100,
"Papaya":50,
"Juice":150}
while True:
    option=input("please select 1 for list of items or 2 for exit:")
    if option=="2":
        print("thank you for shopping.")
        break
    if option=="1"
        print(lists)
        for i in range(len(items)):
            choice=input("choose 1 to buy or 2 to exit:")
            if choice=="2":
                print("thank you for shopping.")
                break
            if choice=="1":
                item=input("enter item to buy:")
                quantity=int(input("quantity of the item:"))
                if item in items.keys():
                    price=quantity*items[item]
                    product_list.append((item,quantity,price))
                    total_price+=price
                    discount=(total_price*5)/100
                    final_price=total_price-discount
                else:
                    print(f" {item} is out of stock")
            else:
                print("please choose only 1 or 2")
    else:
        print("please select only 1 or 2")
    
     




                












    


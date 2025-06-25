#CREATING TUPLE
my_details=("john",25,"green")
print(my_details)
#ACCESSING TUPLE ELEMENTS
week=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(week[3])
#tuple concatenation
even_num=[]
odd_num=[]
for i in range(1,7):
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(tuple(even_num))
print(tuple(odd_num))
numbers=even_num+odd_num
print(numbers)
#TUPLE UNPACKING
my_tuple=(4.5,2)
length,width=my_tuple
print(f"length of the rectangle:{length}")
print(f"width of the rectangle:{width}")
area=length*width
print(f"area of the rectangle is {area}")
#CHECK IF AN ELEMENT EXISTS
my_tuple=("ram",90,5.7,"krishna",[1,2,3])
print("siva" in my_tuple)
print("ram" in my_tuple)





# #GENERATE SUPERMARKET BILL
# name=input("enter the customer name:")
# products=[]
# count=0
# total=0
# while count<5:
#     item=input("enter the item:")
#     price=int(input("enter the price:"))
#     products.append((item,price))
#     count+=1
# print("item\tprice")
# print("-"*20)
# for i,j in products:
#     total+=j
#     print(f"{i}\t{j}")
# print("-"*20)
# print(f"total\t{total}")


# SUM OF THE SQUARES OF NUMBERS FROM 1 TO 5
# sum=0
# for i in range(1,6):
#     result=i**2
#     sum+=result
# print(f" SUM OF THE SQUARES OF NUMBERS FROM 1 TO 5: {sum}")

# print 5 to 1
# count=5
# while count>0:
#     print(count)
#     count-=1

# multiplication table
# num=int(input("enter the value:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# nested for loop
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")
#     print("*"*20)

# multiplication table by using nested for loop
# num=int(input("enter the value:"))
# for i in range(1,11):
#     for j in range(1,2):
#         print(f"{num}x{i}={num*i}")
        
# sum of even numbers between 1 to 10
# sum=0
# for i in range(0,11,2):
#     sum+=i
# print(sum)
# # sum of even numbers between the given numbers
# start=int(input("enter the starting number:"))
# end=int(input("enter the ending number: "))
# sum=0
# for i in range(start,end+1):
#     if i%2==0:
#         sum+=i
# print(sum)

#sum of numbers upto given number
# num=int(input("ener the ending number:"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
#     print(sum)
    
#display numbers from list
my_list=list(range(1,50,10))
# print(my_list)
# for i in my_list:
#     print(i)

# display numbers from -10 to -1
# for i in range(-10,0):
#     print(i)

#pattern print
# num=int(input("enter num of rows:"))
# for i in range(num+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# rows=5
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

rows=5
for i in range(rows):
    for j in range(1,i+1):
        print(" "*(rows-i-1),"*",end=" )

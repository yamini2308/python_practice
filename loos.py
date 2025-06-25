# # SUM OF SQUARES OF NUMBERS FROM 1 TO 5
# sum=0
# for i in range(1,6):
#     result=i**2
#     sum+=result
# print(f"sum of squares from 1 to 5 is {sum}")
# # COUNTDOWN FROM 1 TO 5
# count=5
# while count>0:
#     print(count)
#     count-=1
# # multipication table by using nested for loop
# num=int(input("enter the number:"))
# for i in range(1,2):
#     for j in range(1,11):
#         print(f"{num}x{j}={num*j}")
#     print("*"*10)
# SUM OF EVEN NUMBERS AND ODD NUMBERS
# first_number=int(input("enter the starting number: "))
# last_number=int(input("enter the ending number: "))
# even_sum=0
# odd_sum=0
# for i in range(first_number,last_number+1):
#     if i%2==0:
#         even_sum+=i
# print(f" sum of even numbers between {first_number} and {last_number} is {even_sum}")
# for j in range(first_number,last_number+1):
#     if j%2!=0:
#         odd_sum+=j
# print(f"sum of odd numbers between {first_number} and {last_number} is {odd_sum}")
# #SUM OF ALL NUMBERS UPTO GIVEN NUMBER
# num=int(input("enter the last number:"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(f"sum of numbers between 1 and {num} is {sum}")
# #DISPLAY NUMBERS FROM LIST
# my_list=list(range(1,21,4))
# print(my_list)
# for i in my_list:
#     print(i)
#DISPLAY NUMBERS FROM -10 TO -1
for i in range(-10,0):
    print(i)
#SUM OF CUBES UPTO GIVEN NUMBER
num=int(input("enter the ending number:"))
sum=0
for i in range(1,num+1):
    result=i**3
    sum+=result
print(f"sum of cubes of the numbers between 1 and {num} is {sum}")

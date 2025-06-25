# #vowel checker
# character=input("enter the alphabet:")
# vowel_list=["A","E","I","O","U","a","e","i","o","u"]
# if character in vowel_list:
#     print(f"{character} is a vowel")
# else:
#     print(f"{character} is a consonant")

# #AGE GROUP CLASSIFFICATION.
# age=int(input("enter your age:"))
# if age<=12:
#     print("your age group id child.")
# elif age>=13 and age<=17:
#     print("your age group is teenager.")
# elif age>=18 and age<=64:
#     print("your age group is adults.")
# else:
#     print("your age group is senior.")

# #number classification.'
# number=int(input("enter a number:"))
# if number>0:
#     print(f"{number} is a positive number.")
# elif number<0:
#     print(f"{number} is a negative number.")
# else:
#     print("it is zero")

# LEAP YEAR OR NOT
# year=int(input("enter a year:"))
# if (year%4==0) and (year%100!=0 or year%400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
# # simple calculator
# num_1=int(input("enter the value of num_1: "))
# num_2=int(input("enter the value of num_2: "))
# choice=input("select the operator: ")
# if choice=="+":
#     result=num_1+num_2
#     print(f"addition value of {num_1} and {num_2} is {result}")
# elif choice=="-":
#     result=num_1-num_2
#     print(f"substraction value of {num_1} and {num_2} is {result}")
# elif choice=="*":
#     result=num_1*num_2
#     print(f"multipication value of {num_1} and {num_2} is {result}")
# elif choice=="/":
#     result=num_1/num_2
#     print(f"addition value of {num_1} and {num_2} is {result}")
# else:
#     print("invalid choice.")
#SHORT HAND IF
x=int(input("enter a number: "))
if x%2==0: print("even")
else: print("odd")

# discount calculator
bill_amount=int(input("enter the bill amount:"))
discount_percentage=int(input("enter the discount:"))
discount_amount=bill_amount*discount_percentage/100
final_bill=bill_amount-discount_amount
print(f"your finla bill after {discount_amount} discount is {final_bill} rupees.")
#BMI Calculation
weight=int(input("enter your weight in kgs: "))
height=float(input("enter your height in meter:"))
bmi=weight/(height)**2
print(f"your bmi is{bmi}")
                        
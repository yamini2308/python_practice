 # calculate the area of a rectangle by using user input.
# length=float(input("enter the length of the rectangle:")) 
# width=float(input("enter the width of the rectangle:"))
# # formula to calculate area of the rectangle area=length*width
# area=length*width
# print(f"The area of the rectangle :{area}")

# # incrementing and decrementing a variable.
# num=int(input("enter the value:"))
# print(f"The actual number is {num}")
# num+=5
# print(f"number after increment of 5 {num}")
# num=int(input("enter the value:"))
# print(f"The actual number is {num}")
# num-=5
# print(f"number after decremented by 5 is {num}")

# # converting temperatue from celsius to fahrenheit
# celcius=float(input("enter the temperature in celcius: "))
# # formula for conversion f=(c*9/5)+32
# fahrenheit=(celcius*9/5)+32
# print(f"{celcius} degrees celcius is equal to {fahrenheit} degrees fahrenheit")

# # # calculating the simple intrest
# # principle_amount=int(input("enter the amount:"))
# # interest_rate=float(input("enter the rate of interest:"))
# # time=float(input("enter the time period in years:"))
# # # formula to calculate  simple interest=(amount*rate*time)/100
# # simple_interest=(principle_amount*interest_rate*time)/100
# # print(f"the simple interest for {principle_amount} in {time} years is {simple_interest}")

# # concatination of strings
# first_name=input("enter first name:")
# last_name=input("enter last name:")
# full_name=first_name+last_name
# print(full_name)

# #converting distance from kilometers to miles
# kilometers=float(input("enter the distance in kilometers: "))
# # formula 1kilometer=0.62 miles
# conversion_factor=0.62
# miles=kilometers*0.62
# print(f"{kilometers} kilometers distance is equal to {miles} miles")

# welcoming the user and stating their age
name=input("enter the name: ")
age=int(input("enter the age:"))
print(f" welcome {name}, you are {age} years old")

#list creation
my_list=[1,2,3,4,5,6,7,8,9,10]
#using membership operators
print(5 in my_list)
print(15 not in my_list)
print(20 in my_list)
print(6 not in my_list)
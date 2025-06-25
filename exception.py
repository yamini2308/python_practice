# # ZeroDivisionError
# numerator=int(input("enter numerator value:"))
# denominator=int(input("enter denominator value:"))
# try:
#     result=numerator/denominator
#     print(result)
# except ZeroDivisionError as e:
#     print(f"error: {e}")

#ValueError
# import math
# try:
#     num=int(input("enter a positive number:"))
#     result=math.sqrt(num)
#     print(f"The square root of {num} is {result}")
# except ValueError as e:
#     print(f"error:{e}")

#TypeError and IndexError
# my_list=[2,4,6,8,10]
# try:
#     print(my_list[3])
#     print(my_list["two"])
# except TypeError as e:
#     print(f"error:{e}")
# try:
#     print(my_list[2])
#     print(my_list[7])
# except IndexError as e:
#     print(f"Error:{e}")

#FileNotFoundError
# try:
#     my_file=open("python.text","r")
#     print(my_file)
#     my_file.close()
# except FileNotFoundError as e:
#     print(f"Error:{e}")

#KeyError
# my_dict={1:"apple",2:"banana",3:"mango"}
# try:
#     value=my_dict[2]
#     value2=my_dict[4]
# except KeyError as e:
#     print(f"Error:{e}")

# #AttributeError
# class Person():
#     def __init__(self,name):
#         self.name=name
# obj=Person("ram")
# try:
#     print(obj.name)
#     print(obj.age)
# except AttributeError as e:
#     print(f"Error: {e}")


# #OverflowError
# import math
# try:
#     result=math.exp(450987)
#     print(result)
# except OverflowError as e:
#     print(f"error: {e}")

#IOError
try:
    my_file=open("list.py","rb")
    content=my_file.read
    print(content)
    my_file.close()
except IOError as e:
    print(f"Error:{e}")

    


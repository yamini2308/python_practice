# fruits=["banana","mango","orange","guava","kiwi","grapes","apple","pear"]
# print(fruits)
# # accessing list elements by positive indexing
# print(fruits[3])
# print(fruits[5])
# print(fruits[0])
# # accesing list elements by using negative indexing
# print(fruits[-1])
# print(fruits[-5])
# print(fruits[-8])
# # accessing group of elements by slicing
# print(fruits[2:6])
# print(fruits[::])
# print(fruits[:8:2])
# print(fruits[0::3])
# print(fruits[::-1])
# print(fruits[7:3:-1])
# print(fruits[:6:-1])
# print(fruits[-3:-7:-2])
# print(fruits[::-2])


# # REVERSING THE  ORDER OF LIST ELEMENTS
# #  by using slicing
# my_list=[10,20,30,40,50,11]
# reversed_list=my_list[::-1]
# print(reversed_list)
# # by using reverse method
# my_list.reverse()
# print(my_list)

# #COMMON ELEMENTS
# list_1=[1,2,3,4,5]
# list_2=[4,5,6,7,8]
# common_list=[]
# for i in list_1:
#     if i in list_2:
#         common_list.append(i)
# print(common_list)

# #UNIQUE ELEMENTS
# original_list=[1,2,2,3,4,4,5]
# unique_list=[]
# for i in original_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# #REMOVE DUPLICANTS
# duplicated_list=[1,2,2,3,4,4,5]
# #LIST TO SET CONVERSION
# my_set=set(duplicated_list)
# print(my_set)
# #SET TO LIST CONVERSION
# my_list=list(my_set)
# print(my_list)


#LIST CONCATANATION
# list_1=["ram","siva","laxman"]
# list_2=["arjun","raja","krishna"]
# # by using "+"
# list_3=list_1+list_2
# print(list_3)
# # by using extend method
# list_1=[10,20,30]
# list_2=[50,60,70]
# list_1.extend(list_2)
# print(list_1)
# # by using loop
# list_1=[100,400,300]
# list_2=[120,780,987]
# for i in list_2:
#     list_1.append(i)
# print(list_1)


# #LIST REPETITION
# my_list=[20,50,60,40,30]
# repeated_list=my_list*3
# print(repeated_list)

# #removing elements
# my_list=[10,20,30,40,50,60,70,80,90]
# new_list=[]
# for i in range(len(my_list)):
#     if i%2!=0:
#         new_list.append(my_list[i])
# print(new_list)

#inserting elements
my_list=[13,14,15,16]
my_list.insert(0,10)
my_list.insert(1,11)
my_list.insert(2,12)
print(my_list)


#list comprehensions
squares=[i*i for i in range(1,11)]
print(squares)

even_numbers=[i for i in range(1,21) if i%2==0]
print(even_numbers)
words=["apple","banana","orange","grapes"]

words_length=[len(i) for i in words]
print(words_length)


    




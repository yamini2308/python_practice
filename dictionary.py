# #DICTIONARY MANAGEMENT
# my_dictionary={}
# while True:
#     print("   DICTINARY MANAGEMENT SYSTEM   ")
#     print("1.add a word")
#     print("2.search for meaning")
#     print("3.display all words")
#     print("4.update meaning")
#     print("5.delete word")
#     print("6.exit")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         word=input("enter your word:")
#         meaning=input("enter the meaning of the word:")
#         my_dictionary[word]=meaning
#         print(f"{word} is successfully added to the dictionary.")
#     elif choice==2:
#         word=input("enter the word to search:")
#         if word in my_dictionary:
#             print(f"meaning of {word} is {my_dictionary[word]}")
#         else:
#             print(f"{word} is not found in the dictionary.")
#     elif choice==3:
#         print("the dictionary contains the following words and their meanings")
#         if my_dictionary:
#             for word,meaning in my_dictionary.items():
#                 print(f"{word} meaning is {meaning}")
#         else:
#             print("dictionary is empty")
#     elif choice==4:
#         word=input("enter the word be updated:")
#         if word in my_dictionary:
#             meaning=input("enter the new meaning for the word:")
#             my_dictionary[word]=meaning
#             print(f"{word} is updated successfully")
#         else:
#             print(f"{word} not found in the dictionary")
#     elif choice==5:
#         word=input("enter the word to be delete:")
#         if word in my_dictionary:
#             my_dictionary.pop(word)
#             print(f"{word} is successfully deleted from the dictionary")
#         else:
#             print(f" {word} is not found.")
#     elif choice==6:
#         print("exit")
#         break
#     else:
#         print("enter the valid choice between 1 to 6")





# DICTIONARY UPDATE
my_dict={"name":"python","age":25}
my_dict["city"]="west godavari"
print(my_dict)
#using update method
my_dict.update({"city":"west godavari"})
print(my_dict)
#DICTIONARY ACCEESS
product_info={"name":"laptop","brand":"dell","price":1200}
print(product_info["price"])
#DICTIONARY REMOVAL
my_dict={"name":"python","age":25,"city":"bhimavaram"}
my_dict.pop("city")
print(my_dict)
del my_dict["age"]
print(my_dict)
# DICTIONARY KEYS & VALUES
my_dict={"name":"python","age":25,"city":"rajamandi"}
print(my_dict.keys())
print(my_dict.values())


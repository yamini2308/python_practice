#PRINT THE CHARACTER AT EVEN INDICES
# by slicing 
sentence="Python is amazing"
result=sentence[::2]
print(result)
# using loop
for i in range(len(sentence)+1):
    if i%2==0:
        print(sentence[i],end="")
print()

#REPLACE ALL SPACES IN THE STRING WITH (_)
s="python is fun and powerful"
modified_string=s.replace(" ","_")
print(modified_string)

#CHECK IF THE STRING CONTAINS ONLY DIGITS
s="123456"
print(s.isdigit())
print(s.isalpha())

#PRINT THE STRING IN REVERSE ORDER
s="python is amazing"
print(s[::-1])

#CAPTILIZE THE FIRST LETTER OF EACH WORD IN THE STRING
s="python programming is fun"
s2=s.title()
print(s2)
str="take a string that you want to capitalize"
for word in str.split(" "):
    print(word.capitalize(),end=" ")

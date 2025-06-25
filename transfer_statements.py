numbers=[25,30,20,40,15,25]
sum=0
for i in numbers:
    sum+=i
    if sum>=100:
        break
print(f"sum exceeds 100,sum value:{sum}")

#USING CONTINUE STATEMENT
for i in range(1,601):
    if i%2!=0:
        print(i)
        continue
        

# USING PASS STATEMENT
num=int(input("enter the number:"))
if num%2==0:
    print("given number is even_number")
else:
    pass

#COMBINING TRANSFER STATEMENTS
list_words=["apple","banana","orange","skip","mango","kiwi","break","grapes"]
for word in list_words:
    if word=="break":
        break
    elif word=="skip":
        continue
    else:
        print(word)


        
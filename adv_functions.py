#SQUARE OF ALL NUMBERS BY MAP FUNCTOIN
number_list=[2,4,7,9,23,67,85,59,32]
result=map(lambda a:a*a, number_list)
print(list(result))
#FILTER_POSITIVE NUMBERS
number_list=[-7,-98,78,65,43,-54,-22,56,77]
positive_num=filter(lambda a:a>0 ,number_list)
negative_num=filter(lambda a:a<0 ,number_list)
print(f"positive_numbers: {list(positive_num)}")
print(f"negative_numbers:{list(negative_num)}")
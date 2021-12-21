import random
first_list = []
second_list = []
n = 9
while n >= 0:
	first_list.append(random.randint(1, 10))
	second_list.append(random.randint(1, 10))
	n -= 1
#print('second list ', second_list)
#print('first list ' , first_list) 
#stdout1 = list(set(first_list) & set(second_list))
#print('stdout1 =  ',stdout1 )

stdout = set(first_list).intersection(set(second_list))

#first_list = set(first_list)
#second_list = set(second_list)
print('second   ',second_list,type(second_list), len(second_list))
print('first    ',first_list, type(first_list), len(first_list))
print(stdout)

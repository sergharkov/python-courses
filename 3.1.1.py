import random
random_list=[]
n = 9
while n >= 0:
	random_list.append(random.randint(0, 9))
	print(n)
	n -= 1
print(random_list)
random_list.sort()
print(random_list[9])
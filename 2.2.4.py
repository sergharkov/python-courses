import random
c=''
n = 100
while n > 0:
	n -= 1
	c += str(random.randint(0, 9))
	print(c)
	print(n)
	continue
print(c)
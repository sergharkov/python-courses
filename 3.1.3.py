list = []
stdout=[]
n = 0
while n <= 100:
    list.append(n)
    if((n % 7 == 0) and (n % 5 != 0)):
        stdout.append(n);
    n += 1
print(stdout)


#or   000000
stdout2=[]
for n in range(100):
    if((n % 7 == 0) and (n % 5 != 0)):
        stdout2.append(n);
print(stdout2)

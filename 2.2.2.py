a_str = "OBD8XZYF1F96KRI207H17K0PJF6M2W5C"
# your code goes here
#print(len(a_str))
i=0
res=0
while i < len(a_str):
#    print(i)
#    print(a_str[i])
#    print(ord(a_str[i]))
    res += ord(a_str[i])
    i += 1
    continue
print(res)

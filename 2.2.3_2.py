a_str = 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C'
b_str = 'RJUAKY9QKJVJIDWFZQPJ8293EEEO9SB8ZH832HTOP'
# your code goes here
res = 0
i=0
if len(a_str) > len(b_str):
	ln=len(b_str)
else:
	ln=len(a_str)
print(ln)
#print(len(b_str))
#print(len(a_str))

while i<ln:
	res += abs(ord(a_str[i]) - ord(b_str[i]))
	print(res)
	print(i)
	i += 1
	continue
print("111111111", res)
print(ord('0')*(len(a_str)-len(b_str)))
res = res + abs(ord('0')*(len(a_str)-len(b_str)))
print(res)

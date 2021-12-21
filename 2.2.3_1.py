a_str = 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C'
b_str = 'RJUAKY9QKJVJIDWFZQPJ8293EEEO9SB8ZH832HTOP'
# your code goes here
res = 0
i=0
ln=len(b_str) if len(a_str) < len(b_str) else len(a_str)
while i<ln:
	if len(a_str)>i:
		res += abs(ord(a_str[i]) - ord(b_str[i]))
	else:
		res += abs(0 - ord(b_str[i]))
	i += 1
	continue
print("111111111", res)

a_str = "1D+3qwKBgESv4cYluNDRLl7aACr"
b_str = "Jq77sGRFnnHkTmcQLfZKJdOJEmRALYS8tLoZM"
# your code goes here
N= len(a_str) - len(b_str)
if N>0:
	print(f'a_str is bigger than b_str by {abs(N)} characters)
elif N<0:
	print(f'b_str is bigger than a_str by {abs(N)} characters')
else:
	print(f'a_str and b_str lengths are equal')	

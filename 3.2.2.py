stock = {
   'banana': 6,
   'apple': 0,
   'orange': 32,
   'pear': 15
  }
prices = {
   'banana': 4,
   'apple': 2,
   'orange': 1.5,
   'pear': 3
  }
# write your program here
total=0
for key, value in stock.items():
    total=total+ value * prices[key]
print(total)

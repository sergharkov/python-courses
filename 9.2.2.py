"""
Створіть власну реалізацію вбудованої функції range під назвою in_range(), 
яка приймає три параметри: start, end, і опціонально step.
Підказка: перегляньте документацію для функції range.
"""
def in_range(start, end=None, step=1):
    if end != None:
        ran=[]
 #      print(f"start :{start} end :{end} step : {step}")
        while start < end:
            ran.append(start)
            start = start + step    
    else:
        ran=[]
        i=0
#       print(f"start :{start} end :{end} step : {step}")
        while i < start:
            ran.append(i)
            i = i + step
    return ran





print("---------i-----------")
for i in range(2):
    print(f"range  : {i}")
    
print("---------ii-----------")   
for ii in in_range(2):
    print(f"in_range  : {ii}")    
     
print("---------ii-----------")   
for ii in in_range(2,8):
    print(f"in_range  : {ii}")

"""
Створіть власну реалізацію вбудованої функції enumerate під назвою with_index,
яка приймає два параметри: iterable і start, за замовчуванням 0.
Підказка: перегляньте документацію для функції enumerate.

"""
def with_index1(iterable, start=0):
    res = [] 
    i=0
    while i < len(iterable):
        key = i+start
        value = iterable[i]
        res1=(key, value)
        res.append(res1)
        i +=1
    return res


#pass variant---------------
def with_index(iterable, start=0):
    count = start
    for elem in iterable:
        yield (count, elem)
        count += 1



          
iterable = [16, 46, 26, 36]
print(with_index1(iterable, start=20))


print(with_index(iterable, start=20))



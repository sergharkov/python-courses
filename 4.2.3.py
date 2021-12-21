def make_operation(operator, *number):
    try:
        i=0
        if (type(operator) is not str):
            raise TypeError
        if ((operator not in '+,*,-')):
            raise ValueError
        while i<len(number):
            if (type(number[i]) is not float) and (type(number[i]) is not int):
                raise TypeError
            i+=1
        return eval(operator.join(map(str,number)))
    except TypeError:
        print ('TypeError')
        raise
    except ValueError:
        print('ValueError')
        raise      
print(make_operation('+',5,5,100,-20))

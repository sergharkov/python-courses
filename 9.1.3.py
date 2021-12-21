"""
Напишіть клас TypeDecorators, який має різні методи конвертації результатів 
функцій у зазначений тип, якщо це неможливо – викликати відповідний виняток.
Методи:
to_int
to_str
to_bool
to_float
Не забувайте використовувати @wraps

class TypeDecorators:
    pass
        
@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string
        
assert do_nothing('25') == 25
assert do_something('hello') is True  

"""

from functools import wraps
import time

class TypeDecorators:
 
#----------------------------------------------------------------------     
    def to_int(f):
        @wraps(f)
        def wrapper(par):
                try:
                    _result = int(par)
                except ValueError:
                    raise ValueError("input string can not be transform")
                else:
                    return _result
        return wrapper
#----------------------------------------------------------------------   
    def to_str(f):
        @wraps(f)
        def wrapper(par):
                _result=str(par)
                print(f"decorator to_str  {_result}")
                return _result
        return wrapper
#---------------------------------------------------------------------- 
    def to_bool(f):
        @wraps(f)
        def wrapper(par):
                try:
                    _result = par.lower() in ("yes", "true", "t", "1")

                except ValueError:
                    raise ValueError("input string can not be transform")
                else:
                    return _result
        return wrapper
    
    
    
#----------------------------------------------------------------------     
    def to_float(f):
        @wraps(f)
        def wrapper(par):
                try:
                    _result = float(par)
                except ValueError:
                    raise ValueError("input string can not be transform")
                else:
                    return _result
        return wrapper




        
@TypeDecorators.to_int
def do_nothing(string: str):
    return string
print(do_nothing('25'))
print(type(do_nothing('25')))




@TypeDecorators.to_bool
def do_nothing(string: str):
    return string
print(do_nothing('1'))
print(type(do_nothing('0')))


@TypeDecorators.to_float
def do_nothing(string: str):
    return string
print(do_nothing('1.2'))
print(type(do_nothing('0')))




@TypeDecorators.to_str
def do_nothing(string: str):
    return string
print(do_nothing('фф'))
print(type(do_nothing('aa')))




"""
Перевірка позиційних параметрів
1 point possible (graded)
Напишіть параметризований декоратор (додаткови рівень декората, що може приймати параметри) string_arg_rules, 
який перевіряє позиційні аргументи, що передаються будь-якій задекорованій функції. 
При цьому цей декоратор гарантує, що всі позиційні аргументи є рядками та відповідають визначеним у декораторі вимогам.
Декоратор має приймати 3 аргументи:
- max_length - целое число, допустимая длина входной строки
- contains - кортеж символов, который должен содержать аргумент, по умолчанию пустой кортеж
- exclude - кортеж символов, который не должен содержать аргумент, по умолчанию пустой кортеж
В случае провала любой из проверок, ваш декоратор должен вызвать соответствующее исключение с сообщением об ошибке, 
перед любым выполнением декорированной функции. 
У разі провалу будь-якої з перевірок, ваш декоратор має викликати відповідний виняток (TypeError або ValueError) 
з повідомленням про помилку, перед будь-яким виконанням функції, що декорується. 
Для перевірки спробуйте використати декоратор на різних функціях, які приймають різні набори аргументів.


-------------------------------------------------------------------
from functools import wraps


def string_arg_rules(max_length=1, contains=(), exclude=()):
    pass


@string_arg_rules(max_length=15, contains=('05', '@'), exclude=("S", 's'))
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    create_slogan('peter@05')  # ok
    create_slogan('peter@06')  # ValueError: Arguments must contain '05'
    create_slogan('Seter@05')  # ValueError: Arguments must not contain 'S'    
"""
from functools import wraps

def string_arg_rules(max_length=1, contains=(), exclude=()):
    def s_d_param_dec(func):
        @wraps(func)
        def wrap(*args, **kwargs): 

            for arg in args:
                if (type(arg) is not str):
                    raise TypeError(f"Arguments must been String type")                
                
                if len(arg) > max_length :
                    raise ValueError(f"Arguments must been not over {max_length}")
                for con in contains:
                    if con not in arg:
                        raise ValueError(f"Arguments must contain '{con}'")
                for con in exclude:
                    if con in arg:
                        raise ValueError(f"Arguments must not contain '{con}'" )
            return func(*args, **kwargs)
        return wrap
    return  s_d_param_dec   

@string_arg_rules(max_length=15, contains=('05', '@'), exclude=("S", 's'))
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    create_slogan('peter@05')  # ok
    print('111111111111111111111111111111111111111111111111111111111')
    create_slogan('peter@06')  # ValueError: Arguments must contain '05'
    print('111111111111111111111111111111111111111111111111111111111')    
    create_slogan('Seter@05')  # ValueError: Arguments must not contain 'S' 
    
    
    
    
    
"""    
if (type(max_length) is not int):
                raise TypeError(f"TypeError: Arguments must been Int type")
            if (type(contains) is not str):
                raise TypeError(f"TypeError: Arguments must been tuple type")
            if (type(exclude) is not str):
                raise TypeError(f"TypeError: Arguments must been tuple type")
"""
      


# -*- coding: utf-8 -*-
"""
Створіть функцію to_power, яка приймає два параметри: x та exp,
і повертає x ^ exp. Вам потрібно реалізувати цю функцію виключно за допомогою рекурсії. Приклад:
"""

def to_power(x, exp):
   try: 
       if exp<0:
           raise ValueError   
       if exp==0:
           return 1
       return x*to_power(x, exp-1)   
   except ValueError:
        raise ValueError('This function works only with exp > 0.')
   

to_power(-3.5, -1)

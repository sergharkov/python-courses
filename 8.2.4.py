# -*- coding: utf-8 -*-
"""
Тиждень 8  Задача 4
--------------------
Створіть функцію sum_of_digits, яка приймає введення рядків 
і повертає суму всіх символів переданого рядка (тобто числового представлення символу). 
Функція працює тільки з рядками, і якщо переданий об'єкт іншого типу, вона повинна викликати TypeError. 
Вам потрібно реалізувати цю функцію виключно за допомогою рекурсії.
"""
import re
def sum_of_digits(digit_string):
   try: 
       if (type(digit_string) is not str):
           raise TypeError
       elif digit_string == '':
           return 0
       else:
           digit_string=re.sub("[^0-9]", "", digit_string)
           
           return int(digit_string[0]) + sum_of_digits(digit_string[1:])
        
   except TypeError:
        raise TypeError("input string must be string")
   

print(sum_of_digits('2g6t'))



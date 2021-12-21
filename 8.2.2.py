# -*- coding: utf-8 -*-
"""
Напишіть Python-функцію під назвою operation_mapper, 
яка приймає на вхід математичну операцію у вигляді рядка: “+”, “-”, “/”, “*”, “**” 
(в іншому випадку, має викликатися правильний виняток ValueError); 
має повертатися функція, яка працює з двома вхідними параметрами, 
застосовує математичну операцію до них і повертає результат.


4 week .3 task

def operation_mapper(operation):
    # write your program here 
    
eval(operator.join(map(str,number)))
    
"""
a,b = 0,0

operation = ''

def _sub(a, b):
    return a-b
    
def _add(a, b):
    return a+b
    
def _mul(a, b):
    return a*b

def _div(a, b):
    return a/b

def _squ(a, b):
    return a**b
    
##others____    
def non_operation(*args, **kwargs):
    return f"ValueError"
    raise      


def operation_mapper(operation):
    operation_dict = {
        "-": _sub,
        "+": _add,
        "*": _mul,
        "/": _div,
        "**": _squ,
    }
    if operation in operation_dict:
        return operation_dict[operation]
    else:
        return non_operation
    
print(operation_mapper('+')(2, 3))

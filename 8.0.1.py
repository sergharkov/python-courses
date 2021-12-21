"""
Тиждень 8  Задача 1
-------------------

Напишіть Python-функцію inspector, яка визначає корисну інформацію в переданом
їй об'єкті функції та створює читабельний рядок з цією інформацією в такому форматі:

Func name: {func_name}
Func docs: {func_doc_string}
Num of local variables: {num_of_local_variables}
Name of local variables: {local_variable_names}

"""


def func1():
    a=10
    b=20
    pass


def inspector(func):
    # students write your program here  
    func_name = func.__name__
    func_doc_string = func.__doc__
    num_of_local_variables = func.__code__.co_nlocals
    local_variable_names = func.__code__.co_varnames
    local_variable_names = ', '.join(local_variable_names)
    return f"Func name: {func_name}\nFunc docs: {func_doc_string}\nNum of local variables: {num_of_local_variables}\nName of local variables: {local_variable_names}\n"
  
res=inspector(func1)
print(res)


print("===========================================")

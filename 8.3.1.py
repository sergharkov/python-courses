from functools import wraps
#import json
def logger(f):
    # students write your program here
    @wraps(f)
    def wrap(fun_a,*args, **kwargs):
        func_name = f.__name__
        k=0
        if type(fun_a) is str:
            args_res=f"'{fun_a}'"
        else:
            args_res=str(fun_a)
        if len(args) >0:
            for arg in args:
                args_res += str(arg)
        if len(kwargs) == 0:
            kwargs_list={}
        if len(kwargs)>0:
            kwargs_list=""
            for (key, value) in kwargs.items():
                if k == 0: 
                    sep=""
                else: sep=","
                k +=1                
                if type(value) is str:
                    kwargs_list = kwargs_list + sep + "{0}='{1}'".format(key, value)
                else:
                    kwargs_list =kwargs_list + sep + "{0}={1}".format(key, value)                          
        print(f"{func_name} called with args: {args_res} and kwargs: {kwargs_list}")
    return wrap

@logger
def test_some1(a):
    return a
@logger
def test_some2(a, b, c):
    return a
print(test_some1(1)) # test_some1 called with args: 1 and kwargs: {}
print(test_some2({1, 2, 3},2, b='y', c='e')) # test_some2 called with args: 2 and kwargs: b='y',c='e'  
print(test_some2('s',{1, 2, 3}, b='y', c='e'))
print(test_some2("<class 'ValueError'>", test='test',temp=1.23,n={1: 2}))

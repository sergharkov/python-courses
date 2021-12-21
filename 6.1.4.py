class ValidationMixin:
    def  validate(self,list_int):
        try:
            if (type(list_int) is not list):
                raise TypeError
            if all(isinstance(x, int) for x in list_int):
                return list_int  
            else: raise ValueError
            return list_int
        except  TypeError:
            print (f"Class is working with strings only")
            raise
        except  ValueError:
            print (f"Class is working with part integer only")
            raise 
class SquareNums(ValidationMixin):
     def square_nums(self, list_int):
        self.validate(list_int)
        return [i ** 2 for i in list_int]
class RemovePositives(ValidationMixin):
    def remove_positives(self, list_int):        
        self.validate(list_int)
        list_pos = []
        for i in list_int: 
            if i<0: list_pos.append(i)
        return list_pos
    
class FilterLeaps():
    def filter_leaps(self, list_int):
        self.validate(list_int)
        not_vis=[]
        for i in list_int:
            if (i > 0):
                if (i % 4 == 0) and i % 100 != 0 or i % 400 == 0:
                    not_vis.append(i)
        return not_vis

class Mathematician(FilterLeaps, RemovePositives, SquareNums):
    pass  
        
m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

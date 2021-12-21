class Validate:
    def __init__(self, Val):
        self.Val = Val
    def Vstr(self):
        try:
            if (type(self.Val) is not str):
                raise TypeError
            return self.Val.lower()
        except  TypeError:
             print (f"Class is working with strings only")
             raise
    def Vint(self):
        try:
            if (type(self.Val) is not int):
                raise TypeError
            return int(self.Val)
        except  TypeError:
             print (f"Class is working with strings only")
             raise
class Library:
    books_count = 0
    def __init__(self,):
        self.name=name
        self.year = books[]
        self.author = author[]
        
    def add_new_book(self, book):
        self.books.add(book)
        self.authors.add(book.author)
        
        
    def group_by_author(self,):
        pass
    
    def group_by_year(self,):
        pass

    def __str__(self):
        result="Library name: "+self.name+"\n"
        return result


class Book:
    books_count = 0
    def __init__(self,name="",year=0):
        self.name   = name
        self.year   = year
        self.author = author  #part of class Author
        pass
    
    def add_new_book(self, set_name_book, set_year_book):
        self.name = Validate(set_name_book).Vstr()
        self.year = Validate(set_name_year).Vint()
        
       # self.library.books.append(self)#put this book in the library

class Author:
    def __init__(self,name="",country="",birthday=""):
        self.name     = name
        self.country  = country
        self.birthday = birthday
        self.books    = set ()
    def write_new_book(self, name: str, year: int):
        book = Book(name,year)
        Book.books_count += 1
        self.books.add(book)
        return book
    
    
book1= Book()  
    
 
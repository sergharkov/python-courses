class Library:
    def __init__(self, name, books=None, authors=None):
        if books is None:
            self.books = set()
        elif type(books) is set:
            self.books = books
        else:
            raise TypeError
            
        if authors is None:
            self.authors = set()
        elif type(authors) is set:
            self.authors = authors
        else:
            raise TypeError
        self.name = name
    def add_new_book(self, book):
        if book not in self.books:
            self.books.add(book)
        if book.author not in self.authors:
            self.authors.add(book.author)
    def group_by_author(self, author):
        lst =[]
        for book in self.books:
            if book.author == author:
                lst.append(book)
        return lst
    def group_by_year(self, year: int):
        lst =[]
        for book in self.books:
            if book.year == year:
                lst.append(book)
        return lst     
    def __str__(self):
        return f'({self.name}, {self.books}, {self.authors})'
    def __repr__(self):
        return f'{self.__class__}, {self.name}, {self.books}, {self.authors}'
class Book:
    books = set()
    books_count = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
    def __str__(self):
        return f'{(self.name, self.year, self.author)}'
    def __repr__(self):
        return f'{self.__class__}, {self.name}, {self.year}, {self.author}'
    def __eq__(self, other):
        return self.name == other.name and self.year == other.year and self.author == other.author
    def __hash__(self):
        return hash((self.name, self.year, self.author))
class Author:
    def __init__(self, name, country, birthday, books = set()):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
    def write_new_book(self, name: str, year: int):
        new_book = Book(name, year, self)
        self.books.add(new_book)
        Book.books.add(new_book)
        Book.books_count = len(Book.books)
        return new_book
    def __str__(self):
        return f'({self.name}, {self.country}, {self.birthday})'
    def __repr__(self):
        return f'{self.__class__}, {self.name}, {self.country}, {self.birthday}'
    def __eq__(self, other):
        return self.name == other.name and self.country == other.country and self.birthday == other.birthday
    def __hash__(self):
        return hash((self.name, self.country, self.birthday))
    
nameLib=Library("testLib")





Book1=Book("Book1",1860,"Author1")
Book2=Book("Book2",1861,"Author1")
Book3=Book("Book3",1862,"Author1")
Book4=Book("Book4",1863,"Author1")

Author1=Author("Author1", "USS",1901,Book1)
Author2=Author("Author2", "USS",1902,Book2)
Author3=Author("Author3", "USS",1903,Book3)


nameLib.add_new_book(Book1)
nameLib.add_new_book(Book2)
nameLib.add_new_book(Book3)
nameLib.add_new_book(Book4)

print(nameLib.group_by_year(1860))


#print(Book1)
#print(nameLib)




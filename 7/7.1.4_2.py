class Library:
    def __init__(self, name):
        self.name=name
        self.books=[]

    def add_new_book(self, book: Book):
        self.books.add(book)
        self.authors.add(book.author)

        

    def __str__(self):
        return f"Library NAME   {self.name}\n   {self.books}"
    def __repr__(self):
        return f"Library NAME   {self.name}\n   {self.books}"
    
class Book:
    def __init__(self, title, year, library):
        self.title=title
        self.year=year
        self.library=library
        self.authors=[]
        self.library.books.append(self) #put this book in the library
    def __str__(self):
        return f" \n\
                  Books NAME   : {self.title}\n\
                  YEar of books: {self.year}\n\
                  Author of books: {self.authors}\n"   
    def __repr__(self):
        return f" \n\
                  Books NAME   : {self.title}\n\
                  YEar of books: {self.year}\n\
                  Author of books: {self.authors}\n" 
                  
class Author:
    def __init__(self,name,country="",birthday="",book=""):
        self.name=name
        self.country=country
        self.birthday=birthday
        self.book=book
        self.book.authors.append(self)   #put this author in the book
    def __str__(self):
        return f" \n\
                  NAME Author      :  {self.name}\n\
                  Country of Author:  {self.country}\n\
                  Year Author      :  {self.birthday}  "  
    def __repr__(self):
        return f" \n\
                  NAME Author      :  {self.name}\n\
                  Country of Author:  {self.country}\n\
                  Year Author      :  {self.birthday}  " 
                  
  
        
        
        
    # Create library
orangeCountyLibrary = Library("Orange County Public Library")
    # Create book
warAndPeace = Book("War and Peace", 1869,orangeCountyLibrary)

Tolstoy=Author("Tolstoy", "USSR", 1886, warAndPeace)

hitchhikersGuide = Book("Hitchhiker's Guide to the Galaxy, The", 1985,orangeCountyLibrary)
    # Print the current owner of Hitchhiker's Guide
print(hitchhikersGuide.library)  # Orange County Public Library


print("---------------------      ")
print(Tolstoy.book)
#print(hitchhikersGuide.Book)
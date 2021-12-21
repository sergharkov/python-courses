# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:00:31 2021

@author: ksi
"""

class Library:
    
    def __init__(self, books = None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
    def pages_over_n(self, number):
        """Returns books that have more than specified number of pages"""
        return [book for book in self.books if book.pages > number]
    
    def get_library(self):
        """Returns all books in Library"""
        return self.books
    
    def __repr__(self):
        return f"Library({self.books})"
    
    def __str__(self):
        return f"Library has {len(self.books)}"

class Novel:
    
    def __init__(self, title, pages, publicationDate):
        self.title = title
        self.pages = pages
        self.publicationDate = publicationDate
        
    def __repr__(self):
        return f"Novel({self.title}, {self.pages}, {self.publicationDate})"
    
    def __str__(self):
        return f"Media: {self.title}"
    
class ComicBook(Novel):
    
    def __init__(self, title, pages, publicationDate, artist):
        super().__init__(title, pages, publicationDate)
        self.artist = artist
        
    def get_artist(self):
        return f"Artist: {self.artist}"
        
    def __repr__(self):
        return (f"ComicBook({self.title}, {self.pages}, " 
                f"{self.publicationDate}, {self.artist})")
    
class ReadingList:
    
    def __init__(self):
        self.list = []
    
    def add_book(self, book):
        """Add book to reading list"""
        self.list.append(book)
        
    def remove_book(self, book):
        """Remove book from reading list"""
        self.list.remove(book)

    def total_pages(self):
        """Returns total pages in reading list"""
        total = 0
        for book in self.list:
            total += book.pages
        return total

    def __repr__(self):
        return f"ReadingList({self.list})"
    
    def __str__(self):
        return f"Reading list of size {len(self.list)}"

# Initialise Library
library = Library()

# Create a few books
novel1 = Novel("Harry Potter", 500, 1991)
novel2 = Novel("LotR", 1000, 1960)
novel3 = Novel("Game of Thrones", 2000, 2018)
comic1 = ComicBook("Batman", 100, 2020, "Stan Lee")
print(library.get_library())
# Add books to library.
library.add_book(novel1)
library.add_book(novel2)
library.add_book(novel3)
library.add_book(comic1)

# Create a new reading list.
readingListOne = ReadingList()

# Add a couple of books to reading list.
readingListOne.add_book(novel1)
readingListOne.add_book(comic1)

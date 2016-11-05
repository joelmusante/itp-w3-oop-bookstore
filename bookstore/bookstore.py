
class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []
    
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, author=None, title=None):
        found_books = []
        if author is not None:
            for book in self.books:
                if book.author == author:
                    found_books.append(book)
            return found_books
            
        if title is not None:
            found_books = []
            for book in self.books:
                if title.lower() in book.title.lower():
                    found_books.append(book)
            return found_books

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
    

        
    
    


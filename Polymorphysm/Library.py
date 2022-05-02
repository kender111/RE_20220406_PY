class Author:
    def __init__(self, fname, lname, country, birthday):
        self.fname = fname
        self.lname = lname
        self.country = country
        self.birthday = birthday
        books = []

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author.Author

class Library:
    def __init__(self, name):
        self.name = name
        books = []
        authors = []
        
    def new_book(name, year, author):
        
        

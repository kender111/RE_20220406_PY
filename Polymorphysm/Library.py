class Author:
    def __init__(self, fname, lname, country, birthday ):
        self.fname = fname
        self.lname = lname
        self.country = country
        self.birthday = birthday
        self.books = []
    
    def __repr__(self):
        return f'Писатель {self.fname} {self.lname}, рожден в {self.country} в {self.birthday} году'
        

    
class Book(Author):
    def __init__(self, title, year, author, city, p_house, pages):
        self.title = title
        self.year = year
        self.author = author # OBJECT Class Author
        self.city = city
        self.p_house = p_house
        self.pages = pages
        
    def __repr__(self):
        return f'{self.author.lname} {self.author.fname[0]}, {self.title} // {self.city[0]}. : {self.p_house}, {self.year}. - {self.pages} c.'
    

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # List of OBJECTS Class Book
        self.authors = [] # List of OBJECTS Class Author
   
    def __str__(self):
        s = self.name + ':\n'
        for b in self.books:
            s += f'{b.title} \n'
        return s

    def new_book(self, name, year, author, city, p_house, pages):
        b = Book(name, year, author, city, p_house, pages)
        self.books.append(b)
        return(b)
    
    def group_by_author(self, author):
        lst = []
        for b in self.books:
            if b.author == author:
                lst.append(b)
        return lst
        
    def group_by_year(self, year):
        lst = []
        for book in self.books:
            if book.year == year:
                lst.append(book)
        return lst

a = Author('Терри', 'Пратчетт', 'UK', 1948)
b = Author('Джон', 'Толкиен', 'UK', 1892)
c = Author('Дуглас', 'Адамс', 'UK', 1952)
lib = Library('Библиотека Менина')

lib.new_book('Гобіт', 1991, b, 'Киев', 'Веселка', 303)
lib.new_book('Сильмариллион', 2022, b, 'Киев', 'Астролябия', 576)
lib.new_book('Стража! Стража!', 1989, a, 'Киев', 'Эксмо', 496)
lib.new_book('Ресторан В конце Вселенной', 1980, c, 'Киев', 'АСТ', 352)

print(lib)
print(lib.books)

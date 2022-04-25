class Person:
    def __init__(self, fname, lname, age):
        self.name = fname
        self.surname = lname
        self.age = age
        
    def talk(self):
        print(f'Hello! My name is {self.name} {self.surname}! My age is {self.age}.')
        
        
p = Person('John', 'Doe', '32')
p.talk()
    
        

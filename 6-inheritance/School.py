class Person:
    def __init__(self, fio, gender, age, address, phone_number):
        self.fio = fio
        self.gender = gender
        self.age = age
        self.address = address
        self.ph_number = phone_number
        

class Teacher(Person):
    def __init__(self, fio, gender, age, address, phone_number, salary,\
                 bonus, expirience, prof_int, si_degree, position):
        Person.__init__(self, fio, gender, age, address, phone_number)
        self.salary = salary
        self.bonus = bonus
        self.exp = expirience
        self.prof_int = prof_int
        self.degree = si_degree
        self.pos = position
        
    
class Student(Person):
    def __init__(self, fio, gender, age, address, phone_number, course,\
                 stipend, rating, visiting = 1.0, curtains = 'yes'):
        Person.__init__(self, fio, gender, age, address, phone_number)
        self.course = course
        self.stipend = stipend
        self.rating = rating
        self.visiting = visiting
        self.curtains = curtains #handed over the purchase of curtains
        

s = Student('Lisa Batory', 'f', 20, 'Hungary', '0967585584', course = 2, stipend = 'yes', rating = 'A')

t = Teacher('Maria Curie', 'f', 30, 'Poland', '0967526384', 3526, 0.5, 10, 'Chemistry', 'PHD', 'Head of Department')

print(s.__dict__, t.__dict__, sep = '\n')

    

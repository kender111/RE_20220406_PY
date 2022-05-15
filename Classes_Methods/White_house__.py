class Person:

    count = 0
    staff = 0
    all_salary = 0
    staff_salary = 0
    staff_assistants = []
            
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.__class__.count += 1
        self.__class__.all_salary += self.salary
        if self.status != "Detailee":
            self.__class__.staff += 1
            self.__class__.staff_salary += self.salary
        if self.position_title == "STAFF ASSISTANT":
            self.__class__.staff_assistants.append(self)
    
    def report2():
        return f'''Всего {Person.count} сотрудников, 
        общая зарплата {Person.all_salary}, 
        средняя зарплата {Person.all_salary / Person.count :.{2}f}, 
        средняя зарплата штатных сотрудников {Person.staff_salary / Person.staff :.{2}f}'''
        
    def __del__(self):
        self.__class__.count -= 1
        self.__class__.all_salary -= self.salary
        if self.status != "Detailee":
            self.__class__.staff -= 1
            
    def assistants_report():
        c = 0
        for i in wh.sotr:
            c += 1
            print(f'{c}. {str.capitalize(i.position_title)}: {i.name} / salary: ${i.salary}')


    def __repr__(self):
        return self.name
    
class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)
        
    def get_sotr(self, name_file):
        f = open(name_file, 'r')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$','').replace(',',''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)
    
    def recount(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        Person.all_salary = su
        
    
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary
            
        return su/len(self.sotr)
        
    def top10(self):
        
        def sal(i):
            return i.salary
            
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse = True)
        
        return top2[:10]

    def detailees(self):        
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):        
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
    def count_sotr(self):
        print(f'''Всего {Person.count} сотрудников, 
из них {Person.staff} на постоянной основе
общий заработок {Person.all_salary}''')
            
        
    
wh = WH('white_house_2017_salaries_com.csv')
#wh.rep()
print(Person.report2()) # Инфо по сотрудникам
print(Person.staff_assistants) # Добавление STAFF ASSISTANT в отдельный список
print(Person.staff_assistants)
del Person.staff_assistants[0] # Удаление STAFF ASSISTANT из списка
print(Person.staff_assistants)
print(Person.assistants_report())# Вывод списка сотрудников в заданном формате

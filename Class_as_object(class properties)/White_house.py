class Person:
    count = 0
    staff = 0
    all_salary = 0
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        Person.count += 1
        Person.all_salary += self.salary
        if status != 'Detailee':
            Person.staff += 1

        
    def __repr__(self):
        return self.name
        
class WH:
    def __init__(self, filename):
        self.sotr = []
        self.get_sotr(filename)
        
    def get_sotr(self, filename):
        f = open(filename, 'r')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$', '').replace(',', ''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)

wh = WH('white_house_2017_salaries_com.csv')
print(f'''Всего сотрудников: {Person.count}
        Из них постоянных: {Person.staff}
        Oбщая зарплата всех сотрудников: {Person.all_salary}''')


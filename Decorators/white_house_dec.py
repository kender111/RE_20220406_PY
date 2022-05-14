from heapq import nlargest


class Employee:
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        
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
            e = Employee(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(e)
            
    def sum(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        return su/len(self.sotr)
    
    def top10(self):
        top = self.sotr.copy()
        res = nlargest(10, top, key = lambda t : t.salary)
        return res
    
    def detailees(self):
        t = []
        for i in self.sotr:
            if i. status == 'Detailee':
                t.append(i)
        return t
    
    def staff_assist(self):
        t = []
        for i in self.sotr:
            if i.position_title == 'STAFF ASSISTANT':
                t.append(i)
        return len(t)
    
    def staff_salary(self):
        t = []
        s = 0
        c = 0
        for i in self.sotr:
            if i.position_title == 'STAFF ASSISTANT':
                s += i.salary
                c += 1
        return f'{s / c:.{2}f}' 
    
    def all_pos(self):
        all_p = []
        for i in self.sotr:
            all_p.append(i.position_title)
        return f'{set(all_p)}, общее количество должностей: {len(set(all_p))}'
    
    def pos(self):
        dct = {}
        for i in self.sotr:
            if i.position_title in dct:
                dct[i] +=1
            else:
                dct[i] = 1
        return dct

    def rep(self):
        for i in self.sotr:
            print(i)
            
wh = WH('white_house_2017_salaries_com.csv')

print(wh.sum())         #2.1 Средний заработок всех сотрудников
print(wh.top10())       #2.2 Какие 10 сотрудников зарабатывают больше всех
print(wh.detailees())   #2.3 Сколько людей временно назначены на другую должность
print(wh.staff_assist())#2.4 Сколько людей в должности "STAFF ASSISTANT"
print(wh.staff_salary())#2.5 Среднюю зарплату всех "STAFF ASSISTANT"
print(wh.all_pos())     #2.6 Сколько всего должностей и какие они?
print(wh.pos())#2.7 Сколько людей на каждой из должностей?

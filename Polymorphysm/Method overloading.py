class Animal:
    def talk(self):
        print('preved medved')

class Dog(Animal):
    def talk(self):
        print('woof woof')
    
class Cat(Animal):
    def talk(self):
        print('MEOW')

def univ_talk(who_talk):
    return who_talk.talk()
    

#a = Animal()
c = Cat()
d = Dog()
#univ_talk(a)
univ_talk(c)
univ_talk(d)

class Dog:
    def __init__(self, age_factor = 7):
        self.age_f = age_factor
        
    def human_age(self):
        return self.age_f *7
     
d = Dog(15)
print(d.human_age())

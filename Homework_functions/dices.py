import unicodedata
import random as r

def dice():
    print(r.randint(1,6))
    
dice()

'''-----------------'''

def graph_dice():
    randomint = r.randint(1,6)
    print(unicodedata.lookup(f'DIE FACE-{randomint}'))

graph_dice()


def universal_dice(s = 6):
    print(r.randint(1,s))
    
universal_dice()

'''-----------------'''

def vedro_kubov(n, k):
    count = 1
    vederko = []
    while count <= k:
        brosok = r.randint(1, n)
        count += 1
        vederko.append(brosok)
    print(vederko)

user_gran = input('Хочете змінити дайс? Введіть число або Enter: ')
user_bros = input('Хочете кинути кубик більше 1 разу? Введіть число або Enter: ')
n=6
k=1
if user_bros.isdigit():
    k = int(user_bros)
    
if user_gran.isdigit():
    n = int(user_gran)

if user_gran.isdigit() and user_bros.isdigit():
    n = int(user_gran)
    k = int(user_bros)

vedro_kubov(n, k)

'''-----------------'''
    

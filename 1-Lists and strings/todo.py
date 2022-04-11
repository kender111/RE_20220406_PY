todo = ['first task', 'second task', 'third task', 'fourth task', 'fifth task', 'sixth task', 'seventh task']

#1.2
print(todo[0], todo[2], todo[3], todo[-1], sep='\n')

#1.3
print(todo[:3], todo [3:], sep='\n')

#1.4
todo.append('random task')
todo.append('another random task')

#*
todo[0], todo[-1] = todo[-1], todo[0]

#*
usr_task = input('Put your task here, master: ')
todo.append(usr_task)

#**
todo2 = todo
todo3 = todo[:]
todo4 = list(todo)
todo5 = todo.copy()
print(f'todo2 {id(todo2)} todo3 - {id(todo3)} todo4 - \
{id(todo4)} todo5 - {id(todo5)} ')

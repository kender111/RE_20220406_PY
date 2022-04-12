with open('fio.txt') as fiodate:
	usr_dat = fiodate.read()

lst_usr = []
for line in usr_dat.split(' '):
	if not line.strip():
		continue
	lst_usr.append(line.lstrip())

print(f'Доброго дня, {lst_usr[1]}! Ваш вік {2020 - int(lst_usr[3])} років!')

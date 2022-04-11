fio = 'Беседа Юлія Сергіївна'

print(len(fio))

print(fio.split())

name, fam, otch = fio.split()
print(name, fam, otch)

print(f'о - {fio.count("о")}, е - {fio.count("е")}')

fio_s = f'{name} \n {fam} \t {otch}'
print(fio_s) 

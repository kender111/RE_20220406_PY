f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()

st = 0
count = 0
min_max = []
usr_mon = input('Введіть місяць у форматі ХХ: ')
for x in t:
    date_txt = x.split('-')[1]
    if date_txt == usr_mon:
        temp_txt = x.split()[2]
        temp_int = int(temp_txt.replace('°C,',''))
        st = st + temp_int
        min_max.append(temp_int)
        count +=1
   
print(f'Середня температура в місяці {usr_mon}: {st / count}°C')
print(f'Всього записів за вибраний місяць: {count}')
print(f'Найвища температура {max(min_max)}°C')
print(f'Найнижча температура {min(min_max)}°C')

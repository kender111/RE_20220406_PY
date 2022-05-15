#1.1
print([ str(x) for x in range(10)])

#1.2
lists = ['кит', 'кот', 'крот', 'кит', 'кот', 'крот']
print([str(n)+ ' '+m for (n, m) in enumerate(lists)])

#1.3
print([str(n)+ ' '+m for (n, m) in enumerate(lists) if len(m) <=3])

#1.4
lists = ['111', 'cat', 'got', 'ddd', '222']
print([x for x in lists if x.isdigit()])

#1.5
print([ m for m, x in enumerate(lists) if x.isdigit()])
#1.6

print([ (m, x) for (m, x) in enumerate(lists) if x.isdigit()])

#1.7
phones = [
'044 225 73 39', '099 116 30 87', '094 129 81 69', 
'094 127 04 85', '044 222 74 33', '044 353 55 31', '097 921 27 09', 
'094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', 
'099 752 22 97', '050 761 49 45', '094 497 75 09', '094 498 89 53', 
'094 496 13 91', '094 497 35 13', '094 497 75 69', '050 063 52 97', 
'050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', 
'097 001 42 67', '096 097 58 16', '094 497 34 37', '094 097 12 17', 
'094 497 75 69', '097 497 75 97', '094 497 34 85', '094 496 52 54'
]
print([j for x, j in enumerate(phones) if '097' == phones[x][:3]])

#1.8
print([j for x, j in enumerate(phones) if '097' == phones[x][:3] or '050' == phones[x][:3]])

#1.9
print(['+38' + j.replace(' ', '') for x, j in enumerate(phones) if '097' == phones[x][:3] or '050' == phones[x][:3]])

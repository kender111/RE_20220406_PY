month = input()
def season(month):
    if int(month) == 1 or int(month) == 2 or int(month) == 12:
        print ('Winter')
    elif int(month) == 3 or int(month) == 4 or int(month) == 5:
        print ('Sping')
    elif int(month) == 6 or int(month) == 7 or int(month) == 8:
        print ('Summer')
    elif int(month) == 9 or int(month) == 10 or int(month) == 11:
        print ('Autumn')
    else:
        print ('Error')
        
season(month)







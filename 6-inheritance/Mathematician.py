class Mathematician:
    def square_nums(self, liist):
        list1 = []
        for i in range(len(liist)):
                n = liist[i] ** 2
                list1.append(n)
        return(list1)
    
    def remove_positives(self, liist):
        list1 = []
        for i in range(len(liist)):
            if liist[i] < 0:
                list1.append(liist[i])
        return list1
    
    def filter_leaps(self, liist):
        list1 = []
        for i in range(len(liist)):
            if liist[i] % 4 == 0:
                list1.append(liist[i])
        return list1

m = Mathematician()


assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


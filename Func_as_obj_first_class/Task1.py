def myfunc():
    one = 1
    two = 2
    three = "Test"
    four = {1 : 5}

print(myfunc.__code__.co_nlocals)

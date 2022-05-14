import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cikl_args = [repr(a) for a in args] 
        my_args = ", ".join(cikl_args)
        f = f'Функція {func.__name__} робить дивні дії з цифрами {my_args}'
        return f
    return wrapper

@logger
def add(x, y):
    return x + y
    
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
    

print(add(4, 5))
print(square_all(3, 5, 9))

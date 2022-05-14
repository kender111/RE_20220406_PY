import functools

def stop_words(words: list):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            for i in words:
                f = f.replace(i, '!@#$%')
            return f
        return wrapper
    return dec
    
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
    
#assert create_slogan("Steve") == "Steve drinks !@#$% in his brand new !@#$%!"
print(create_slogan('Totoro'))

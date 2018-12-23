import time

def square_mult(n):
    def decorator(f):
        def wrap(*args, **kwargs):
            result = [i * n for i in f(*args, **kwargs)]
            return result
        return wrap
    return decorator

def time_decorator(f):
    def wrap(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print(f'The {f.__name__} took {str((end-start)*1000)} ml seconds')
        return result
    return wrap

@square_mult(4)
def threes(numbers):
    list_of_numbers = [i for i in numbers if i % 2 == 0]
    return list_of_numbers

array = range(1,1000000)
print(threes(array)[1:50])



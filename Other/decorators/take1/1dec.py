import time

def multiplier(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = [number *n for number in f(*args, **kwargs)]
            return result
        return wrapper
    return decorator


def timer(function):
    def new_function(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'{function.__name__} took {end-start} seconds')
        return result
    return new_function

# def odd(numbers):
#     start = time.time()
#     result = [n for n in numbers if n % 2 == 1]
#     end = time.time()
#     print(f'Process took {end-start} seconds')
#     return result


# def even(numbers):
#     start = time.time()
#     result = [n for n in numbers if n % 2 == 0]
#     end = time.time()
#     print(f'Process took {end-start} seconds')
#     return result

@timer
def odd(numbers):
    result = [n for n in numbers if n % 2 == 0]
    return result
    
@timer
@multiplier(10)
def even(numbers):
    result = [n for n in numbers if n % 2 == 1]
    return result

# odd = timer(odd)
# even = timer(even)

######################################################
#es aris igive rac multiplier dekoratori
# even = multiplier(10)(even)

######################################################

numbers = range(1, 1000000)
print(even(numbers)[:50])
# print(odd(numbers)[:50])


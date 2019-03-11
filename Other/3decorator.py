import time


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'{f.__name__} took {end-start} seconds to finish')
        return result
    return wrapper

# def timer(f, *args, **kwargs):
#     start = time.time()
#     result = f(*args, **kwargs)
#     end = time.time()
#     print(f'{f.__name__} took {end-start} seconds to finish')
#     return result


@timer
def evens(numbers:list) -> list:
    result = [num for num in numbers if num % 2 == 1]
    return result
# evens = timer(evens)


@timer
def odds(numbers:list) -> list:
    result = [num for num in numbers if num % 2 == 0]
    return result
# odds = timer(odds)


numbers = range(1,1000000)
# evens = timer(evens, numbers)
# odds = timer(odds, numbers)
print(odds(numbers)[:50])
print(evens(numbers)[:50])
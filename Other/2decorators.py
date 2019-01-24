import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('Are you inside??? Oh yeaaaah')
        print(f'{f.__name__} took {end-start} seconds')
        return result
    return wrapper


@timer
def odds(numbers:list) -> list:
    result = [n for n in numbers if n % 2 == 0]
    return result


numbers = range(1,1000000)
print('Answer is: ', odds(numbers)[:50])
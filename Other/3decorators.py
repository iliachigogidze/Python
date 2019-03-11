import time
import random


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'{f.__name__} aeeeeeeeeeeee')
        result = f(*args, **kwargs)
        end = time.time()
        print(f'{f.__name__} took {end-start} secs to finish the proccess') 
        return result
    return wrapper

@timer
def opana():
    while True:
        random_number = random.randint(1,1000)
        if random_number == 17:
            break

@timer
def odds(numbers:list) -> list:
    '''
    From the given list return only odd numbers as a list
    '''
    result = [n for n in numbers if n % 2 == 0]
    return result


numbers = range(1000000)
print('Odds: ', odds(numbers)[:50])
print('random: ', opana())
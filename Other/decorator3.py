import time

def my_decorator(f):
    def wrap(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + ' took {} to finish'.format(str((end-start)*1000) + ' mil seconds'))
        return result
    return wrap

@my_decorator
def square(numbers):
    result = [number * number for number in numbers] 
    return result

@my_decorator
def cube(numbers):

    result = [number * number * number for number in numbers]
    return result

array = range(1, 100000)
square(array)
cube(array)

import time

def timer(f):
    def wrap(numbers):
        # print('Here is theee: ', n)
        start = time.time()
        result = f(numbers)
        end = time.time()
        print('{} took {} secs to finish the process'.format(f.__name__, str(end-start)))
        return result
    return wrap

@timer
def print_odds(numbers):
    odds = [n for n in numbers if n % 2 == 0]
    return odds[:50]

# print_odds = timer(print_odds)


numbers = range(10000000)
print(print_odds(numbers))
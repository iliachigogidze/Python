import random

def dice(n=2):
    return tuple(random.randint(1,6) for _ in range(n))

dice(4)
dice(3)
dice()
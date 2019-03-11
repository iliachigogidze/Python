import argparse

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result           

parser = argparse.ArgumentParser()
parser.add_argument('integers', nargs=3, type = int, help='Enter integers')

group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', dest='accumulates', action='store_const', const=sum, default=max, help='Sums integers (default: finds maximum integer)')
group.add_argument('--mult', dest = 'accumulate', action='store_const', const=multiply, default=max)
args = parser.parse_args()

print(args.accumulate(args.integers))

 

import argparse

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

parser = argparse.ArgumentParser(description='Descriptiooon')
parser.add_argument('name', nargs=2, metavar='', type=str, help='Enter your name and lastname')
parser.add_argument('integers', nargs = '+', type=int, metavar='s', help='Enter 3 integers')

group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', dest='saxeli', action='store_const', const=sum, default=max, help='Help')
group.add_argument('--mult', dest = 'saxeli', action='store_const', const=multiply, default=min, help='help2')



# group.add_argument('--sum', dest='accumulates', action='store_const', const=sum, default=max, help='Sums integers (default: finds maximum integer)')
# group.add_argument('--mult', dest = 'accumulate', action='store_const', const=multiply, default=max)
args = parser.parse_args()

print(args.name, ' ', args.saxeli(args.integers))
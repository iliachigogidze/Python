import argparse

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

parser = argparse.ArgumentParser(description='asfas')
parser.add_argument('integers', nargs='+', type=int, metavar='N', help='Enter integers')
group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', dest='saxeli', action='store_const', const=sum, default=max, help='sdasd')
group.add_argument('--mult', dest='saxeli', action='store_const', const=multiply, default=max, help='sdasd')
args = parser.parse_args()


print(args.saxeli(args.integers))
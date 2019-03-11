import argparse


def multiply(numbers:list) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


parser = argparse.ArgumentParser(description='Enter integers to calculate')
parser.add_argument('integers', nargs='+', metavar='N', help='Enter integers', type=int)
parser.add_argument('integers', nargs='+', metavar='N', help='Enter integers', type=int)
group = parser.add_mutually_exclusive_group()
group.add_argument('-s', '--sum', dest='ragac', action='store_const', const=sum, default=max, help='Sums or max on default')
group.add_argument('-m', '--mult', dest='ragac', action='store_const', const=multiply, default=max, help='Multiplies or max on default')
args = parser.parse_args()


print(args.ragac(args.integers))

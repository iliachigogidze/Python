import argparse

parser = argparse.ArgumentParser(description='Adds, Subtracts or Multiplies two nubmers')
parser.add_argument('-n1','--number1',type=float, required=True,help='Number 1')
parser.add_argument('-n2','--number2',type=float, required=True, help='Number 2')
parser.add_argument('-o','--operation', choices=['add','subtract','multiply'])
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet', action="store_true")
group.add_argument('-v','--verbose',action="store_true")
args = parser.parse_args()


result = None
if args.operation == 'add':
    result = args.number1 + args.number2
elif args.operation == 'subtract':
    result = args.number1 - args.number2
elif args.operation == 'multiply':
    result = args.number1 * args.number2

if args.quiet:
    print(result)
elif args.verbose:
    print('Answer is: ', result)
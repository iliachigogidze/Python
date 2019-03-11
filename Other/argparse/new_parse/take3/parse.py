import argparse

parser = argparse.ArgumentParser(description='Ouch is this the desctiption??')
parser.add_argument('integers',metavar='N', nargs='+', type=int, help='Enter integers')
group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', dest='ragac', action='store_const', const=sum, default=min, help='help text')
args = parser.parse_args()

print(args.ragac(args.integers))
import argparse

parser = argparse.ArgumentParser(description='This is parsing your arguments')
parser.add_argument('name',metavar='', help='Enter your name')
parser.add_argument('-ln','--lastname',required=True, metavar='', help='Enter your lastname')
parser.add_argument('-id','--id_number', required=True, metavar='', type=int, help='Enter your ID number')
parser.add_argument('-s','--sex', choices=['male','female'], metavar='',help='Enter your sex')
parser.add_argument('-a','--age',metavar='',help='Enter your age', type=int)
parser.add_argument('-H', '--height', metavar='', type=float, help='Enter your height')
parser.add_argument('-w', '--weight', metavar='', type=float, help='Enter your weight')
group=parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet', action='store_true', help='Prints quietly')
group.add_argument('-v','--verbose', action='store_true', help='Prints verbosely')
group.add_argument('-t','--teslurad', action='store_true', help='Prints teslurad')
args= parser.parse_args()




def create_profile(name:str, lastname:str, id_number:int, sex:str, age:int=None, height:float=None, 
    weight:float=None):
    profile = {
        'name':name,
        'lastname':lastname,
        'id_number':id_number,
        'sex':sex,
        'age':age,
        'height':height,
        'weight':weight
    }
    return profile


profile = create_profile(args.name, args.lastname, args.id_number, args.sex, args.age, 
    weight=args.weight, height=args.height)

if args.quiet:
    print(profile)
elif args.verbose:
    print('Verbose: ', profile)
elif args.teslurad:
    print('Teslurad: ', profile)
else:
    print('Whhaaaaaaaaat???!')


import argparse

parser = argparse.ArgumentParser(description='ragac description')
parser.add_argument('-n','--name',required=True, type=str, metavar='', help='Enter you name')
parser.add_argument('-ln','--lastname',required=True, type=str, metavar='', help='Enter you lastname')
parser.add_argument('-id','--id_number',required=True, type=int, metavar='', help='Enter you id number')
parser.add_argument('-a','--age', type=int, metavar='', help='Enter you age')
parser.add_argument('-s','--sex', type=str, metavar='', choices=['male','female'], help='Enter you sex')
parser.add_argument('-w','--weight', type=float, metavar='', help='Enter you weight')
parser.add_argument('-H','--height', type=float, metavar='', help='Enter you height')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action = 'store_true', help='Prints quietly')
group.add_argument('-v', '--verbose', action = 'store_true', help='Prints verbose')
group.add_argument('-t', '--teslurad', action = 'store_true', help='Prints teslurad')

args = parser.parse_args()



def create_profile(name:str, lastname:str, id_number:int, age:int = None, sex:str = None, 
    weight:float = None, height:float = None):

    profile = {
        "name":name,
        "lastname":lastname,
        "id number":id_number,
        "age":age,
        "sex":sex,
        "weight":weight,
        "height":height
    }

    return profile


profile = create_profile(args.name, args.lastname, args.id_number, args.age, args.sex, 
    height = args.height, weight = args.weight)

if args.quiet:
    print(profile)
elif args.verbose:
    print('Verbose: ', profile)
elif args.teslurad:
    print('teslurad: ', profile)
else:
    print('Error')


#python args.py -n ilia -ln chigogide id_number 0102123 -a 14 -s male -w 72
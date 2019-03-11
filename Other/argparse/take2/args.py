import argparse

parser = argparse.ArgumentParser(description='Creates profile with name, lastname, id, sex, weight and height')
parser.add_argument('-n','--name', required=True, metavar='', help='Enter your name')
parser.add_argument('-ln','--lastname', required=True, metavar='', help='Enter your latsname')
parser.add_argument('-id','--id_number', required=True, metavar='', help='Enter your id number', type=int)
parser.add_argument('-w','--weight', metavar='', help='Enter your weight', type=float)
parser.add_argument('-H','--height', metavar='', help='Enter your height', type=float)
parser.add_argument('-s','--sex', metavar='', help='Enter your sex', choices = ['male','female'])

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action = 'store_true', help='Prints quietly')
group.add_argument('-v', '--verbose', action = 'store_true', help='Prints verbose')
group.add_argument('-t', '--teslurad', action = 'store_true', help='Prints teslurad')
args = parser.parse_args()

def create_profile(name:str, lastname:str, _id:int, weight:float = None, height:float = None, sex:str = None) -> dict:
    profile = {
        "name":name,
        "lastname":lastname,
        "id":_id,
        "weight":weight,
        "height":height,
        "sex":sex
    }
    return profile


profile = create_profile(args.name, args.lastname, args.id_number, args.weight, args.height, args.sex)
if args.quiet:
    print(profile)
elif args.verbose:
    print('aeeeeeeee ', profile)
elif args.teslurad:
    print('oeeeeeeee ', profile)
else:
    print('amas ar velodi ', profile)
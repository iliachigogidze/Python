import argparse

parser = argparse.ArgumentParser(description='Takes inputs: name, lastname, id number, sex, height and weight to create user profile')
parser.add_argument('-n','--name', required=True, metavar='', help='Enter your name')
parser.add_argument('-ln','--lastname', required=True, metavar='', help='Enter your lastname')
parser.add_argument('-w','--weight', metavar='', help='Enter your weight', type=float)
parser.add_argument('-H','--height', metavar='', help='Enter your height', type=float)
parser.add_argument('-s','--sex', metavar='', choices = ['male','female'], help='Enter your sex')
parser.add_argument('-id','--id_number', metavar='',help='Enter your id number', type=int)

group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet', action='store_true', help='Prints quielty')
group.add_argument('-v','--verbose', action='store_true', help='Prints verbosely')
group.add_argument('-t','--teslurad', action='store_true', help='Prints teslurad')

args = parser.parse_args()

def create_profile(name:str, lastname:str, id_number:int, sex:str, weight:float = None, height:float = None) -> dict:
    profile = {
        "name":name,
        "lastname":lastname,
        "id_number":id_number,
        "sex":sex,
        "weight":weight,
        "height":height
    }
    return profile


profile = create_profile(args.name, args.lastname, args.id_number, args.sex, args.weight, args.height)

if args.quiet:
    print(profile)
elif args.verbose:
    print('verbos: ', profile)
elif args.teslurad:
    print('teslurad: ', profile)
else:
    print('opana')
    


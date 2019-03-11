import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n","--name",required=True, type=str, metavar='', help="Enter your name")
parser.add_argument("-ln","--lastname",required=True, type=str, metavar='', help="Enter your lastname")
parser.add_argument("-id","--id_number",required=True, type=int, metavar='', help="Enter your id number")
parser.add_argument("-a","--age",required=True, type=int, metavar='', help="Enter your age")
parser.add_argument("-s","--sex", type=str, metavar='', choices = ['male','female'], help="Enter your sex")
parser.add_argument("-w","--weight", type=float, metavar='', help="Enter your weight")
parser.add_argument("-H","--height", type=float, metavar='', help="Enter your height")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true', help='Prints result quietly')
group.add_argument('-v','--verbose', action='store_true',help='Prints result verbosely')
group.add_argument('-t','--teslurad',action='store_true',help='Prints result teslurad')

args = parser.parse_args()


def create_profile(name:str, lastname:str, age:int, id_number:int, sex:str = None, weight:float = None, 
    height:float = None) -> dict:
    profile = {
        "name":name,
        "lastname":lastname,
        "age":age,
        "id_number":id_number,
        "sex":sex,
        "weight":weight,
        "height":height
    }
    return profile



profile = create_profile(name=args.name, lastname=args.lastname, sex=args.sex, age=args.age, 
    id_number=args.id_number,weight=args.weight, height=args.height)

if args.quiet:
    print(profile)
elif args.verbose:
    print('Verbose: ', profile)
elif args.teslurad:
    print('teslurad: ', profile)
else:
    print('Fuckin\' error')

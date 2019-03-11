import argparse

parser = argparse.ArgumentParser("Creates Profile")
parser.add_argument("-n",'--name', required=True, type=str, metavar='', help="Enter your name")
parser.add_argument("-ln",'--lastname', required=True, metavar='', type=str, help="Enter your lastname")
parser.add_argument("-id",'--id_number', required=True, type=int, metavar='', help="Enter your id number")
parser.add_argument("-a",'--age', type=int,metavar='',  help="Enter your age")
parser.add_argument("-s",'--sex', choices = ['male', 'female'],metavar='',  type=str, help="Enter your sex")
parser.add_argument("-H",'--height', type=float, metavar='', help="Enter your height")
parser.add_argument("-w",'--weight', type=float, metavar='', help="Enter your weight")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='prints quietly')
args = parser.parse_args()



def create_profile(name:str, lastname:str, id_number:int, age:int = None, sex:str = None, height:float = None, 
    weight:float = None) -> dict:

    profile = {
        "name":name,
        "lastname":lastname,
        "id_number":id_number,
        "age":age,
        "sex":sex,
        "height":height,
        "weight":weight
    }
    return profile


profile = create_profile(args.name, args.lastname, args.id_number, args.age, args.sex, 
    weight = args.weight, height=args.height)
if args.quiet:
    print('Quiet: ', profile)
else:
    print(profile)
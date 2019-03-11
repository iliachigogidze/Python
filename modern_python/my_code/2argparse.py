import math

import argparse

parser = argparse.ArgumentParser(description='Calcualtes volume of the Cylinder')
parser.add_argument('-r','--radius',required=True,type=int,help='Radius of the Cylinder')
parser.add_argument('-H','--height',required=True,type=int,help='Height of the Cylinder')
args = parser.parse_args()


def square(radius:int, height:int) ->float:
    return math.pi * (radius**2) * height


print(square(args.radius, args.height))
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument('-r','--radius', required=True, metavar='', type=int, help='Radius of the Cylinder')
parser.add_argument('-H','--height', required=True, metavar='', type=int, help='Height of the Cylinder')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol


volume = cylinder_volume(args.radius, args.height)
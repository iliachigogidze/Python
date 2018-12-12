'''
Write a program in C to find the first capital letter in a string using recursion.
'''

def main(str):
    str1 = ''.join(str.split(' '))
    print('Original: ', str,    '   || Join: ', str1)

main('my Name is Ilia')
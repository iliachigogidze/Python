'''
find result of Exponentiation of the integer
'''

def main(n, e):
    print('NUMBER IS: ', n, '   EXP IS: ', e)
    return recursion(n, e)

def recursion(n, e):
    if n == 0:
        return 0
    if e == 0: 
        return 1
    elif e < 0:
        n = 1/n
        e = -e
        return n * recursion(n, e-1)       
    else:
        #print('n: ', n, 'e: ',e)
        return n * recursion(n, e-1)
    

print('ANSWER: ', main(4,3))
print('ANSWER: ', main(4,-3))
print('ANSWER: ', main(4,0))
print('ANSWER: ', main(0,0))
print('ANSWER: ', main(0,3))
print('ANSWER: ', main(0,-3))





'''

'''
from math import sin

stack = []
op = ['+','-','*','/']

def minus(a,b):
    '''
    returns a-b
    '''
    return a - b

def plus(a,b):
    return a + b

def divide(a,b):
    return a / b

def mult(a,b):
    return a * b

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

sandro = {
    '-': (minus, 2),
    '+': (plus, 2),
    '/': (divide, 2),
    '*': (mult, 2),
    's': (fact, 1)
}

def main(exp):
    print('Expression: ', exp)


    for c in exp[::-1]:
        if c in sandro:
            op, n = sandro[c]         
            stack.append(op(*[stack.pop() for _ in range(n)]))
        else:
            stack.append(float(c))

    return stack.pop()




print('ANSWER: ', main('+5*23'))
stack = []
print('ANSWER: ', main('s+*2+231'))
stack = []

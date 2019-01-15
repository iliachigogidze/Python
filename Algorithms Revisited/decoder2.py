
stack = []

def minus(a, b):
    return a - b

def plus(a, b):
    return a + b

def divide(a, b):
    return a / b

def mult(a, b):
    return a * b

op = {
    '-': (minus, 2),
    '+': (plus, 2),
    '/': (divide, 2),
    '*': (mult, 2)
}


def main(exp):
    print('Expression: ', exp)

    for c in exp[::-1]:
        if c in op:
            ope, n = op[c]
            stack.append(ope(*[stack.pop() for _ in range(n)]))
        else:
            stack.append(float(c))

    return stack.pop()



print('ANSWER: ', main('+5*23'))
print('ANSWER: ', main('+*2+231'))




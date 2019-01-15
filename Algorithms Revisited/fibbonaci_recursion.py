'''
5. Write a Python program to solve the Fibonacci sequence using recursion
'''

def main(n):
    print('Number is: ', n)
    n = abs(n)
    return rec(n)


def rec(n):
    if n <= 2:
        return [0,1]
    else:
        x = rec(n-1)
        

print('ANSWER: ', main(7))


# def main(n):
#     print('Number is: ', n)

#     return recursion(n)

# def recursion(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0,1]
#     else:
#         # x = recursion(n-1) + recursion(n-2) # es rato aris cudi??
#         x = recursion(n - 1)
#         print(x)
#         return x + [x[-1] + x[-2]] 
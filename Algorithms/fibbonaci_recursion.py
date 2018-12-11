'''
5. Write a Python program to solve the Fibonacci sequence using recursion
'''

sequence = []

def main(n):
    print('NUMBER IS: ', n)

    if n <= 0:
        print('Enter positive integer')
    else:
        recursion(n)
        return sequence
        
def recursion(n):
    
    if n == 1:
        sequence.append(1)
        return 1
    elif n == 2:
        sequence.append(1)
        return 1
    else:
        a = recursion(n - 1)
        b = recursion(n - 2)
        x = a + b
        sequence.append(x)
        return x

# def recursion(n):
#     if n in set([1,2]):
#         return 1
#     else:
#         return recursion(n-1) + recursion(n-2)

        

print('ANSWER: ', main(7))
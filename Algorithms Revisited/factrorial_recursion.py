'''
Write a Python program to get the factorial of a non-negative integer.
'''

def main(n):
    print('Numbers is: ', n)
    n = abs(n)
    return rec(n)

def rec(n):
    if n <= 0:
        return 1
    else:
        return n * rec(n - 1)



print('Answer: ', main(5))
print('Answer: ', main(0))
print('Answer: ', main(-5))


        


# def main(n):
#     print('NUMBERS IS: ', n)
#     if n < 0:
#         print('Integer should be positive')
#     else:
#         return recurse(n)

# def recurse(n):
#     if n <= 0:
#         return 1
#     else: 
#         return n * recurse(n-1)
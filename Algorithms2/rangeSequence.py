'''
Recursively produce a sequence of numbers from 3 to 9 with exclusive bounds.
assert.equal(range(3, 9), [4, 5, 6, 7, 8]);
'''

sequence = []

def main(n, k):
    print('FROM: ', n, '   TO: ', k)

    recursion(n , k)
    return sequence

def recursion(n, k):
    if n == k:
        return n
    else:
        sequence.append(n)
        return recursion(n + 1, k)


print('ANSWER: ', main(4,9))
print('ANSWER: ', main(-5,2))
print('ANSWER: ', main(-5,-3))



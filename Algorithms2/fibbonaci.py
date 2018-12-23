'''
5. Write a Python program to solve the Fibonacci sequence 
'''

def main(n):
    print('Number is: ', n)
    seq = [0,1]
    for i in range(2,n):
        seq.append(seq[-1] + seq[-2])
    return seq


print('Answer: ', main(7))
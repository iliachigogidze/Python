'''
implement selection sort with recursion
'''

def main(numbers):
    print('Numbers: ', numbers)

    return recurse(numbers)

def recurse(numbers):
    if len(numbers) is 1:
        return numbers[0]
    elif len(numbers) is 2:
        return numbers[0] if numbers[0] < numbers[1] else numbers[1]
    else:
        return min (numbers[0], recurse(numbers[1:]))



print('Answer: ', main([-2,5,1,2,3,3,1,12,-5,0,1]))
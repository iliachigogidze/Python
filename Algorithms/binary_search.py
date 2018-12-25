'''
binary search with recursion
'''

def main(numbers, target):
    # print('NUMBERS: ', numbers, '   || target: ', target)
    min = 0
    max = len(numbers) - 1
    while len(numbers) >= 1:
        print('min/max: ', min, max)
        print('len= ', len(numbers))
        middle = len(numbers) // 2
        print('middle_pos= ', middle)
        print('middle_number= ', numbers[middle])
        if numbers[middle] is target:
            return numbers[middle]
        elif numbers[middle] > target:
            max = middle - 1
            return main(numbers[min:max+1], target)
        elif numbers[middle] < target:
            min = middle + 1
            return main(numbers[min:max],target)
        else:
            return False



numbers = range(1,20)
print(main(numbers, 11))

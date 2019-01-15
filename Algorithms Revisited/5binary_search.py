'''
binary search with recursion
'''

def main(numbers, target):
    numbers = sorted(numbers)
    
    print('NUMBERS: ', numbers, '   || target: ', target)
    min = 0
    max = len(numbers) - 1
    while len(numbers) >= 1:
        middle = len(numbers) // 2
        if numbers[middle] is target:
            return numbers[middle]
        elif numbers[middle] < target:
            min = middle + 1
            return main(numbers[min:max], target)
        else:
            max = middle
            return main(numbers[min:max], target)
        



#numbers = range(1,20)
print(main([7,2,5,1,9,-2,4,99,23,24,55,3,36,6,5,5,4,9,5,0,11,13,6,23,65], 11))




# def main(numbers, target):
#     # print('NUMBERS: ', numbers, '   || target: ', target)
#     min = 0
#     max = len(numbers) - 1
#     while len(numbers) >= 1:
#         print('min/max: ', min, max)
#         print('len= ', len(numbers))
#         middle = len(numbers) // 2
#         print('middle_pos= ', middle)
#         print('middle_number= ', numbers[middle])
#         if numbers[middle] is target:
#             return numbers[middle]
#         elif numbers[middle] > target:
#             max = middle - 1
#             return main(numbers[min:max+1], target)
#         elif numbers[middle] < target:
#             min = middle + 1
#             return main(numbers[min:max],target)
#         else:
#             return False


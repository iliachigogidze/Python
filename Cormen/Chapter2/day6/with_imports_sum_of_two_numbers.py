'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''


from Chapter2.day4.binary_search import main as search
from Chapter2.day3.merge_sort import main as merge


def main(numbers, target_value):
    print(f'{target_value} in {numbers}')

    sorted_numbers = merge(numbers)

    result = False
    for i in range(2, len(sorted_numbers)+1):
        new_numbers = sorted_numbers[:i]
        last = new_numbers[-1]
        list_for_search = new_numbers[:-1]
        new_target = target_value - last
        if search(list_for_search, new_target):
            result = True
    return result 

print('Answer is: ', main([6,1,2,4,-2,23],99))
print('Answer is: ', main([6,1,2,4,-2,23],2))
print('Answer is: ', main([6,1,2,4,-2,7],7))
print('Answer is: ', main([6,1,2,4,-2,23],4))
print('Answer is: ', main([6,1,2,4,-2,23],23))
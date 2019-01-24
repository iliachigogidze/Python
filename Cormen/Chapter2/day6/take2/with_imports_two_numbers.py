'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''

from Chapter2.day4.binary_search import main as binary_search
from Chapter2.day3.merge_sort import main as merge_sort

def main(numbers:list, target_value:int) -> bool:
    print(f'Here is: {target_value} and numbers: {numbers}')

    numbers = merge_sort(numbers)

    for i in range(2, len(numbers) + 1):
        indice = numbers[:i]
        number_to_search = target_value - indice[-1]
        list_to_search = indice[:-1]
        if binary_search(list_to_search, number_to_search):
            return True
    return False

print('Answer is: ', main([6,1,2,4,-2,23],99))
print('Answer is: ', main([6,1,2,4,-2,23],2))
print('Answer is: ', main([6,1,2,4,-2,7],7))
print('Answer is: ', main([6,1,2,4,-2,23],4))
print('Answer is: ', main([6,1,2,4,-2,23],23))
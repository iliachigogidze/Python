from Chapter2.day3.merge_sort import main as merge_sort
from Chapter2.day4.binary_search import main as binary_search

def main(numbers:list, target_value:int) -> bool:
    print(f'Find sum of {target_value} in {numbers}')
    if len(numbers) <= 1:
        return False
    return find(numbers, target_value)


def find(numbers:list, target_value:int) -> bool:
    sorted_numbers = merge_sort(numbers)

    for i in range(2, len(sorted_numbers)+1):
        sublist = sorted_numbers[:i]
        value_to_find = target_value - sublist[-1]
        list_to_search = sublist[:-1]
        if binary_search(list_to_search, value_to_find):
            return True
    return False


print('Answer is: ', main([6,1,2,4,-2,23],99))
print('Answer is: ', main([6,1,2,4,-2,23],2))
print('Answer is: ', main([6,1,2,4,-2,7],7))
print('Answer is: ', main([6,1,2,4,-2,23],4))
print('Answer is: ', main([6,1,2,4,-2,23],23))
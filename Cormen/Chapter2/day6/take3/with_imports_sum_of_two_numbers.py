from Chapter2.day4.binary_search import main as binary_search
from Chapter2.day3.merge_sort import main as merge_sort

def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')

    sorted_numbers = merge_sort(numbers)
    for i in range(2, len(numbers)+1):
        indices = sorted_numbers[:i]
        number_to_search = target_value - indices[-1]
        list_for_search = indices[:-1]
        if binary_search(list_for_search, number_to_search):
            return True
    return False


print('Answer is: ', main([1,5,1,2,3,6,-2],0))

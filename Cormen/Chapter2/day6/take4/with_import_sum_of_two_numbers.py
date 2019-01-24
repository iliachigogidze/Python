from Chapter2.day3.merge_sort import main as merge_sort
from Chapter2.day4.binary_search import main as binary_search

def main(numbers:list, target_value: int) -> bool:
    print(f'Target: {target_value} numbers: {numbers}')
    if len(numbers) <= 1:
        return False
    return search(numbers, target_value)


def search(numbers:list, target_value: int) -> bool:
    sorted_numbers = merge_sort(numbers)

    for i in range(2, len(numbers)+1):
        indices = sorted_numbers[:i]

        number_to_search = target_value - indices[-1]
        list_for_search = indices[:-1]

        if binary_search(list_for_search, number_to_search):
            return True
    return False


print('Asnwer is: ', main([5,1,23,5,123,5,2],91))
print('Asnwer is: ', main([5,1,23,5,123,5,2],6))
print('Asnwer is: ', main([5,1,23,5,123,5,2],7))
print('Asnwer is: ', main([5,1,23,5,123,5,2],23))
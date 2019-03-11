from .day4.binary_search import main as binary_search
from .day3.merge_sort import main as merge_sort



'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''

def main(numbers, target_value):
    print(f'Find if {target_value} is sum of two numbers in {numbers}')
    sorted_numbers = merge_sort(numbers)
    
    for i in range(2, len(sorted_numbers)+1):
        indice = sorted_numbers[:i]
        # print(indice)
        number_to_find = target_value - indice[-1]
        # print('target: ', number_to_find)
        list_to_search = indice[:-1]
        # print('list: ', list_to_search)
        
        if binary_search(list_to_search, number_to_find):
            return True
    return False



print(main([5,1,23,5,3,12],12))
print(main([5,1,23,5,0,12],6))
# print(binary_search([1,2,3,4,7,8],9))
# print(binary_search([1,2,3,4,7,8],8))
# print(binary_search([1,2,3,4,7],8))
# print(binary_search([1,2,3,4,7],4))
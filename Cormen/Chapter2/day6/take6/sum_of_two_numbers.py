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


def binary_search(numbers:list, target_value:int) -> bool:
    while len(numbers) > 0:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
    return False




def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])
    right = merge_sort(numbers[middle_point:])

    result = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result
    

print(main([5,1,23,5,3,12],12))
print(main([5,1,23,5,0,12],6))
# print(binary_search([1,2,3,4,7,8],9))
# print(binary_search([1,2,3,4,7,8],8))
# print(binary_search([1,2,3,4,7],8))
# print(binary_search([1,2,3,4,7],4))
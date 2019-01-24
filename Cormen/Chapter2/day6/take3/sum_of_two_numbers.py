'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''

def main(numbers:list, target_value:int) -> bool:
    print(f'target: {target_value} in numbers: {numbers}')
 
    if len(numbers) < 2:
        return False
    
    sorted_numbers = merge_sort(numbers)
    for i in range(2, len(sorted_numbers)+1):
        print('hi')
        indices = sorted_numbers[:i]
        number_to_search = target_value - indices[-1]
        list_for_search = indices[:-1]
        if binary_search(list_for_search, number_to_search):
            return True
    return False


def binary_search(numbers:list, target_value:int) -> bool:
    while len(numbers) >= 1:
        middle_point = (len(numbers) // 2)
        print(numbers)
        

        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
    return False




def merge(left:list, right:list) -> list:
    result = []
    l = 0
    r = 0

    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        
    if l < len(left):
        result.extend(left[l:])
        return result
    if r < len(right):
        result.extend(right[r:])
        return result
    return result


def merge_sort(numbers:list) ->list:
    if len(numbers) == 1:
        return [numbers[0]]
    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])    
    right = merge_sort(numbers[middle_point:])
    return merge(left, right)


print('Answer is: ', main([1,5,1,2,3,6,-2],10))
# print(main([1,6,12,61],12))

# print('binary: ', binary_search([1,2,3,4,5,6,7,8],7))
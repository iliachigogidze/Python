'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''

def main(numbers: list, target_value: int) -> bool:
    print(f'Here is target: {target_value} and {numbers}')

    numbers = merge_sort(numbers)
    print(numbers)

    for i in range(2, len(numbers) + 1):
        indice = numbers[:i]
        number_to_search = target_value - indice[-1]
        list_for_search = indice[:-1]
        if binary_search(list_for_search, number_to_search):
            return True
    return False


def binary_search(numbers, target_value):
    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if len(numbers) == 1:
            if numbers[0] == target_value:
                return True
        if numbers[middle_point] == target_value:
            return True

        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
    return False
    


def merge(left, right):
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

def merge_sort(numbers):
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers[0]]

    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])
    right = merge_sort(numbers[middle_point:])
    return merge(left, right)
        

print('Answer is: ', main([1,6,12,5,123],129))
print('Answer is: ', main([1,6,12,5,123],7))
print('Answer is: ', main([1,6,12,5,123],12))
print('Answer is: ', main([1,1,1,1],12))
print('Answer is: ', main([],12))
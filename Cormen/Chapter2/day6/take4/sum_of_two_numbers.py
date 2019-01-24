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




def binary_search(numbers: list, target_value: int) -> bool:
    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        else:
            numbers = numbers[:middle_point]
    return False

def merge_sort(nubmers:list) -> list:
    if len(nubmers) == 1:
        return nubmers
    middle_point = len(nubmers) // 2
    left = merge_sort(nubmers[:middle_point])
    right = merge_sort(nubmers[middle_point:])

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


print('Asnwer is: ', main([5,1,23,5,123,5,2],91))
print('Asnwer is: ', main([5,1,23,5,123,5,2],6))
print('Asnwer is: ', main([5,1,23,5,123,5,2],7))
print('Asnwer is: ', main([5,1,23,5,123,5,2],23))
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


def merge_sort(numbers:list) -> list:
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


def binary_search(numbers:list, target_value:int) -> bool:
    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
    return False


print('Answer is: ', main([6,1,2,4,-2,23],99))
print('Answer is: ', main([6,1,2,4,-2,23],2))
print('Answer is: ', main([6,1,2,4,-2,7],7))
print('Answer is: ', main([6,1,2,4,-2,23],4))
print('Answer is: ', main([6,1,2,4,-2,23],23))
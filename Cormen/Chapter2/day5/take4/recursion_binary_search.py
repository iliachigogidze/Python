def main(numbers: list, target_value: int) -> bool:
    print(f'Find {target_value} in {numbers}')
    return binary_search(numbers, target_value)


def binary_search(numbers, target_value):
    middle_point = len(numbers) // 2
    if len(numbers) == 0:
        return False
    if len(numbers) == 1:
        if numbers[middle_point] == target_value:
            return True
        return False
    if numbers[middle_point] == target_value:
        return True
    elif target_value > numbers[middle_point]:
        return binary_search(numbers[middle_point+1:], target_value)
    else:
        return binary_search(numbers[:middle_point], target_value)


print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,4,5,8,9,14,14],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],14))
print('Answer is: ', main([1],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],15))
print('Answer is: ', main([1,4,5,8,9,14,14,15],17))
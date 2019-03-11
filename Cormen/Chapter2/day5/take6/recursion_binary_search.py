def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    return recursive_binary_search(numbers, target_value)


def recursive_binary_search(numbers:list, target_value:int) -> bool:
    if len(numbers) < 1:
        return False
    middle_point = len(numbers) // 2
    if numbers[middle_point] == target_value:
        return True
    elif target_value > numbers[middle_point]:
        recursive_binary_search(numbers[middle_point+   1:], target_value)
    elif target_value < numbers[middle_point]:
        recursive_binary_search(numbers[:middle_point], target_value)


print('Answer is: ', main([1,2,3,5,6,7],8))
print('Answer is: ', main([1,2,3,5,6],8))
print('Answer is: ', main([1,2,3,5,6],6))
print('Answer is: ', main([1,2,3,5,6,7],7))
print('Answer is: ', main([1],9))
print('Answer is: ', main([1],1))
print('Answer is: ', main([],1))
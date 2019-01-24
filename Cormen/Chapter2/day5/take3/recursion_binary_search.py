def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    if len(numbers) == 0:
        return False
    return binary_sort(numbers, target_value)


def binary_sort(numbers:list, target_value:int) -> bool:
    if len(numbers) == 1:
        return True if numbers[0] == target_value else False
    middle_point = (len(numbers) // 2) - 1
    if numbers[middle_point] == target_value:
        return True
    elif target_value > numbers[middle_point]:
        return binary_sort(numbers[middle_point+1:], target_value)
    elif target_value < numbers[middle_point]:
        return binary_sort(numbers[:middle_point], target_value)
    else:
        print('Error')

    
print('Answer is: ', main([1,5,6,8,8],8))
print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,2,3,4,5,6,7],6))
print('Answer is: ', main([1],6))
print('Answer is: ', main([1],1))
print('Answer is: ', main([],1))

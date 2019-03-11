def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    return binary_search(numbers, target_value)


def binary_search(numbers:list, target_value:int) -> bool:
    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
    return False

print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,4,5,8,9,14,14],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],14))
print('Answer is: ', main([1],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],15))
print('Answer is: ', main([1,4,5,8,9,14,14,15],17))


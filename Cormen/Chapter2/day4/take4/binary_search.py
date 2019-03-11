def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    if len(numbers) < 1:
        return False
    return binary_search(numbers, target_value)


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



print('Answer is: ', main([1,4,6,7,7,7,8,10,42],8))
print('Answer is: ', main([1,4,6,7,7,7,8,10,42],80))
print('Answer is: ', main([1,3],8))
print('Answer is: ', main([1],8))
print('Answer is: ', main([8],8))
print('Answer is: ', main([1,2,3,4,5,6,7],7))
print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,2,3,4,5,6,7],6))
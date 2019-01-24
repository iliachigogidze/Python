def main(numbers: list, target_value: int) -> bool:
    #print(f'You should find {target_value} in {numbers}')

    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        if numbers[middle_point] > target_value:
            numbers = numbers[:middle_point]
        elif numbers[middle_point] < target_value:
            numbers = numbers[middle_point + 1:]
    return False

if __name__ == '__main__':
    print('Answer is: ', main([1,4,6,7,7,7,8,10,42],8))
    print('Answer is: ', main([1,4,6,7,7,7,8,10,42],80))
    print('Answer is: ', main([1,3],8))
    print('Answer is: ', main([1],8))
    print('Answer is: ', main([8],8))
    print('Answer is: ', main([1,2,3,4,5,6,7],7))

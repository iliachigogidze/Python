def main(numbers, target_value):
    print(f'You should find {target_value} in {numbers}')

    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
        print(numbers)
    return False


print('Answer is: ', main([1,2,3,5,6,7],8))
print('Answer is: ', main([1,2,3,5,6,7],7))
print('Answer is: ', main([1],9))
print('Answer is: ', main([1],1))
print('Answer is: ', main([],1))
print('Answer is: ', main([-2],98))
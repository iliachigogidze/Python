def main(numbers, target_value):
    print(f'You should find {target_value} in {numbers}')
    return sort(numbers, target_value)


def sort(numbers, target_value):
    middle_point = len(numbers) // 2
    if numbers[middle_point] == target_value:
        return True
    if len(numbers) == 1:
        if numbers[0] == target_value:
            return True

    if numbers[middle_point] > target_value:
        return sort(numbers[:middle_point], target_value)
    else:
        return sort(numbers[middle_point:], target_value)
    return False

print('Answer is: ', main([1],7))
# print('Answer is: ', main([1,2,3,4,5,6],7))
# print('Answer is: ', main([],6))
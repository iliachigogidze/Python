def main(numbers, target_value):
    print(f'Yu should find {target_value} in {numbers}')
    return sort(numbers, target_value)

def sort(numbers, target_value):
    middle_point = len(numbers) // 2
    print('middle', middle_point)
    print('numbers:', numbers)
    if numbers[middle_point] == target_value:
        return True
    elif len(numbers) == 1:
        if numbers[0] == target_value:
            return True
    else:
        if numbers[middle_point] < target_value:
            return sort(numbers[middle_point+1:], target_value)
        else:
            return sort(numbers[:middle_point], target_value)
    return False


print('Answer is: ', main([1,4,5,8,9,14,14,15],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],14))
print('Answer is: ', main([1],1))
print('Answer is: ', main([1,4,5,8,9,14,14,15],15))

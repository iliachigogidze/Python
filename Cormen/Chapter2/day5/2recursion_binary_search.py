def main(numbers, target_value):
    print(f'You should find {target_value} in {numbers}')
    return binary_search(numbers, target_value)

def binary_search(numbers, target_value):
    middle_point = len(numbers) // 2
    if numbers[middle_point] == target_value:
        return True
    
    if len(numbers) == 1:
        if numbers[0] == target_value:
            return True
    elif target_value > numbers[middle_point]:
        return binary_search(numbers[middle_point+1:], target_value)
    elif target_value < numbers[middle_point]:
        return binary_search(numbers[:middle_point], target_value)
    return False


def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    
    return binary_search(numbers, target_value)


def binary_search(numbers, target_value):
    if len(numbers) == 1:
        return True if numbers[0] == target_value else False
        
    else:
        middle_point = (len(numbers) // 2) - 1
        if target_value == numbers[middle_point]:
            return True
        elif target_value > numbers[middle_point]:
            return binary_search(numbers[middle_point+1:], target_value)
        elif target_value <  numbers[middle_point]:
            return binary_search(numbers[:middle_point], target_value)
        
        


print('Answer is: ', main([1,2,3,4,5],5))
print('Answer is: ', main([1,2,3,4,5,6],5))
print('Answer is: ', main([1,2,3,4,5,6],7))
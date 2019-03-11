def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')
    return linear_search(numbers, target_value)


def linear_search(numbers:list, target_value:int) -> bool:
    for number in numbers:
        if number == target_value:
            return True
    return False


print('Answer is: ', main([1,2,3,74,5],5))
print('Answer is: ', main([1,2,3,4,5],6))
print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([1,2,3,4,5,6],7))
print('Answer is: ', main([],5))
print('Answer is: ', main([],1))
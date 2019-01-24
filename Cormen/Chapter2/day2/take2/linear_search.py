def main(numbers:list, target_value:int) -> bool:
    print(f'Find {target_value} in {numbers}')

    for num in numbers:
        if num is target_value:
            return True
    return False

print('Answer is: ', main([5,1,23,],0))

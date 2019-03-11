def main(numbers:list, target:int) -> bool:
    print(f'Find {target} in {numbers}')
    return linear_search(numbers, target)


def linear_search(numbers:list, target:int) -> bool:
    # for number in numbers:
    #     if number == target:
    #         return True
    # return False
    return target in numbers




print('Answer: ', main([5,12,3,6,1,35,12],5))
print('Answer: ', main([5,12,3,6,1,35,12],0))
print('Answer: ', main([5,12,3,6,1,35,12],15))
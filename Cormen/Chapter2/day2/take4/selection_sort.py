def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return selection_sort(numbers)


def selection_sort(numbers:list) -> list:
    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1
        while key < numbers[j] and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers


print('Answer is: ', main([4,9,1,0,-12,-4,32,-3,1,0,0]))
print('Answer is: ', main([4]))
print('Answer is: ', main([]))
print('Answer is: ', main([-2,-2,-2]))
print('Answer is: ', main([1,2,3]))
print('Answer is: ', main([1,2,3,2,1]))
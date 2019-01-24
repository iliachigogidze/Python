def main(numbers:list) -> list:
    print(f'Sort numbers {numbers}')
    return insertion_sort(numbers)


def insertion_sort(numbers:list) -> list:
    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1
        while key < numbers[j] and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1  
        numbers[j+1] = key
    return numbers


print('Answer is: ', main([6,12,-2,-6,2,6,-5,-2,0]))
print('Answer is: ', main([]))
print('Answer is: ', main([5,5,5]))
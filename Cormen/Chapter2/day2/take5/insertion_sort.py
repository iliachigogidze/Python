def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return insertion_sort(numbers)


def insertion_sort(numbers:list) -> list:
    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1
        while numbers[j] > key and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers


print('Answer is: ', main([5,-2,5,1,55,2,5,0,-7]))
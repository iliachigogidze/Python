def main(numbers:list) -> list:
    print(f'Sort numbers {numbers}')
    return selection_sort(numbers)


def selection_sort(numbers: list) -> list:
    for i in range(len(numbers)-1):
        min_position = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[min_position]:
                min_position = j
        temp_number = numbers[i]
        numbers[i] = numbers[min_position]
        numbers[min_position] = temp_number
    return numbers


print('Answer is: ', main([6,12,-2,-6,2,6,-5,-2,0]))
print('Answer is: ', main([]))
print('Answer is: ', main([5,5,5]))
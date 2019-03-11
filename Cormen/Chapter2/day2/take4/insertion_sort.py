def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return insertion_sort(numbers)


def insertion_sort(numbers:list) -> list:
    for i in range(len(numbers)-1):
        min_pos = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[min_pos]:
                min_pos = j
        temp_pos = numbers[i]
        numbers[i] = numbers[min_pos]
        numbers[min_pos] = temp_pos
    return numbers


print('Answer is: ', main([4,9,1,0,-12,-4,32,-3,1,0,0]))
print('Answer is: ', main([4]))
print('Answer is: ', main([]))
print('Answer is: ', main([-2,-2,-2]))
print('Answer is: ', main([1,2,3]))
print('Answer is: ', main([1,2,3,2,1]))
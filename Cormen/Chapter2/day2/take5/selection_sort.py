def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return selection_sort(numbers)


def selection_sort(numbers:list) -> list:
    for i in range(len(numbers)-1):
        smallest = i 
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j
        temp = numbers[i]
        numbers[i] = numbers[smallest]
        numbers[smallest] = temp
    return numbers


print('Answer is: ', main([5,-1,5,2,5,0,0,12]))
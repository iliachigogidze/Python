def main(numbers:list) -> list:
    print(f'Sort numbers {numbers}')
    return insertion(numbers)


def insertion(numbers):
    if len(numbers) == 1:
        return numbers[0]
    

def insertion_sort(numbers):
    for i in range(len(numbers)-1):
        key = numbers[i]
        j = i - 1
        while key < numbers[j] and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1
    numbers[j+1] = key
    return numbers


print('Answer is: ', main([5,12,-4,-4,23,-5,1,2,2]))
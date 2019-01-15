def main(numbers):
    print('Numbers is: ', numbers)

    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1

        while key > numbers[j] and j >= 0:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers




print('Answer is: ', main([5,3,4,71,2,-4,0,3]))
def main(numbers):
    print('Numbers is: ', numbers)

    l = len(numbers)
    for i in range(l):
        key = numbers[i]
        j = i - 1

        while numbers[j] > key and j >= 0:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


print('Answer is: ', main([5,2,4,6,1,3]))
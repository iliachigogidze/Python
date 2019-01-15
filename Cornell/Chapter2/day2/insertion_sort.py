def main(numbers):
    print('Numbers is: ', numbers)

    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1
        while numbers[j] > key and j >= 0:
            numbers[j + 1] = numbers[j]
            j -= 1
        
        numbers[j + 1] = key
    return numbers


print('Answer is: ', main([5,-2,-8,0,5,5,4,19]))
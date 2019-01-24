def main(numbers):
    print('Numbers is: ', numbers)

    for i in range(len(numbers)-1):
        pos_min = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[pos_min]:
                pos_min = j
        temp = numbers[i]
        numbers[i] = numbers[pos_min]
        numbers[pos_min] = temp
    return numbers


print('Answer is: ', main([5,1,2,6,1,23,-5,1,1]))
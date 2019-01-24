def main(numbers):
    print('Numbers is: ', numbers)

    for i in range(len(numbers)-1):
        minimum = numbers[i]
        index_minimum = i
        for j in range(i, len(numbers)):
            if numbers[j] < minimum:
                minimum = numbers[j]
                index_minimum = j
        temp = numbers[i] 
        numbers[i] = minimum
        numbers[index_minimum] = temp
    return numbers


print('Answer is: ', main([-9,-19,0,23,41,1,2,5,9,3,-3]))
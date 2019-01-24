def main(numbers):
    print('Numbers is: ', numbers)

    for i in range(len(numbers)-1):
        #find minimum
        #smallest = numbers[i]
        index_of_smallest = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[index_of_smallest]:
                #smallest = numbers[j]
                index_of_smallest = j
        #swap
        temp = numbers[i]
        numbers[i] = numbers[index_of_smallest]
        numbers[index_of_smallest] = temp
        del temp
    return numbers


print('Answer is: ', main([6,-5,9,9,0,9,9,-12,0,5.4,3,2.2]))
def main(numbers):
    print('Numbers is: ', numbers)
    for i in range(len(numbers)-1):
        index_of_smallest = i

        for j in range(i, len(numbers)):
            if numbers[j] < numbers[index_of_smallest]:
                index_of_smallest = j
        temp = numbers[i]
        numbers[i] = numbers[index_of_smallest]
        numbers[index_of_smallest] = temp    
    return numbers

print('Answer is: ', main([9,3,-12,0,3,-52,1,5]))
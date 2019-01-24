def main(numbers):
    print('Numbers is: ', numbers)
    
    for i in range(len(numbers)-1):
        for j in range(len(numbers),i+1):
            if numbers[j] < numbers[j-1]:
                temp = numbers[j]
                numbers[j] = numbers[j-1]
                numbers[j-1] = temp
    return numbers


print('Answer is: ', main([5,1,2,-5,-1,4]))
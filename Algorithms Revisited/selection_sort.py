'''
implement selection sort
'''

def selection_sort(numbers):
    print('Numbers: ', numbers)
    numbers = numbers
    for i in range(len(numbers)):
        temp = numbers[i]
        pos = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < temp:
                temp = numbers[j]
                pos = j
        temp_number = numbers[i]
        numbers[i] = numbers[pos]
        numbers[pos] = temp_number

    return numbers
        


print('ANSWER: ', selection_sort([3,4,8,2,9,1]))
print('ANSWER: ', selection_sort([10,-3,0,4,6,1,4,4,2,-5]))

def main(numbers):
    print('Numbers is: ', numbers)

    l1 = len(numbers) // 2
    l2 = len(numbers) - l1

    left = numbers[:l1]
    right = numbers[l1:]

    l = 0
    r = 0
    print('left', left, 'right', right)
    for i in range(len(numbers)):
        if left[l] < right[r]:
            numbers[i] = left[l]
            l += 1
        else:
            left[i] = right[r]
            r += 1

    return numbers


print('Answer is: ', main([2,4,5,7,1,2,3,6]))
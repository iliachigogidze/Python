def main(numbers:list) -> int:
    print(f'Find number of inversions in {numbers}')
    if len(numbers) < 2:
        return 0
    return inversions(numbers)[1]


def inversions(numbers:list) -> tuple:
    if len(numbers) <=1:
        return numbers, 0
    middle_point = len(numbers) // 2
    left, left_inv = inversions(numbers[:middle_point])
    right, right_inv = inversions(numbers[middle_point:])

    result = []
    l = 0
    r = 0
    inverses = 0 + left_inv + right_inv

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            inverses += (len(left) - l)
            r += 1

    result += left[l:]
    result += right[r:]

    return result, inverses

print('Answer is: ', main([5,1,2,3,5,12]))
print('Answer is: ', main([9,1,-4,0,0]))
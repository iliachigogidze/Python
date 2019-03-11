def main(numbers:list) -> int:
    print(f'Find number of inverses in {numbers}')
    if len(numbers) == 0:
        return 0
    return merge_sort(numbers)


def merge_sort(numbers:list) -> list:
    if len(numbers) <= 1:
        return numbers, 0
    middle_point = len(numbers) // 2
    left, left_inv = merge_sort(numbers[:middle_point])
    right, right_inv = merge_sort(numbers[middle_point:])

    result = []
    inverses = 0 + left_inv + right_inv    
    l = 0
    r = 0 

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
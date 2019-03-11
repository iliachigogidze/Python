def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return merge_sort(numbers)


def merge_sort(numbers:list) -> list:
    if len(numbers) <= 1:
        return numbers, 0
    middle_point = len(numbers) // 2
    left, left_inv = merge_sort(numbers[:middle_point])
    right, right_inv = merge_sort(numbers[middle_point:])

    result = []
    inversions = 0 + right_inv + left_inv
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            inversions += (len(left) - l)
            r += 1
    
    result += left[l:]
    result += right[r:]
    return result, inversions


print('Answer is: ', main([5,1,2,3,5,12]))
print('Answer is: ', main([9,1,-4,0,0]))

def main(numbers:list) -> int:
    print(f'Find inversions for {numbers}')
    if len(numbers) < 1:
        return 0
    return merge_sort(numbers)


def merge_sort(numbers:list):
    if len(numbers) == 1:
        return numbers, 0
    middle_point = len(numbers) // 2
    left, inv_left = merge_sort(numbers[:middle_point])
    right, inv_right = merge_sort(numbers[middle_point:])
    
    result = []
    inversions = 0 + inv_left + inv_right 
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            inversions += (len(left) - l)

    result += left[l:]
    result += right[r:]
    return result, inversions


print('Answer is: ', main([5,1,2,3,5,12]))
print('Answer is: ', main([9,1,-4,0,0]))
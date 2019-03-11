def main(numbers:list) -> list:
    print(f'Sort {numbers}')
    return merge_sort(numbers)


def merge_sort(numbers:list) -> list:
    if len(numbers) <= 1:
        return numbers
    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])
    right = merge_sort(numbers[middle_point:])

    result = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    
    result += left[l:]
    result += right[r:]
    return result


print('Answer is: ', main([1,2,3,4,5]))
print('Answer is: ', main([5,4,3,2,1]))
print('Answer is: ', main([1,1,1,1,1]))
print('Answer is: ', main([-6]))
print('Answer is: ', main([-6,-6,-6]))
print('Answer is: ', main([5,-19,-9,-21,5,8,81,0,5]))

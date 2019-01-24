def main(numbers):
    print('Numbers is: ', numbers)
    if len(numbers) == 0:
        return []
    return merge_sort(numbers)

def merge(left, right):
    
    result = []
    
    l = 0 
    r = 0

    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    if l < len(left):
        result.extend(left[l:])
        return result
    if r < len(right):
        result.extend(right[r:])
        return result

    return result

def merge_sort(numbers):
    if len(numbers) == 1:
        return [numbers[0]]
    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])
    right = merge_sort(numbers[middle_point:])
    return merge(left, right)

# print('Answer is: ', merge([1,4,6],[2,3,9]))
# print('Answer is: ', merge([],[]))
# print('Answer is: ', merge([1,4,6],[2,3,9,10,11,12,13]))
# print('Answer is: ', merge([1,4,6],[2]))
# print('Answer is: ', merge([1,4,6,61,123],[2,3,9]))

print('Answer is: ', main([-4,1,5,-7,412,1,6,2,3]))
print('Answer is: ', main([]))
print('Answer is: ', main([5,5,5]))
print('Answer is: ', main([-4]))



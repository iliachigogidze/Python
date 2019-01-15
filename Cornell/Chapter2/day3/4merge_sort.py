def main(numbers):
    print('Numbers is: ', numbers)

    if len(numbers) < 1:
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
    else:
        middle_point = len(numbers) // 2
        left = merge_sort(numbers[:middle_point])
        right = merge_sort(numbers[middle_point:])
        return merge(left, right)


# print('Answer is: ', merge([],[]))
# print('Answer is: ', merge([1,4,8],[2,7,9,10,11,11,11]))
# print('Answer is: ', merge([1,4,8],[2,7,9]))

print('Answer is: ', main([91,5,2,4,-5,0,3,1,-6]))
print('Answer is: ', main([]))
print('Answer is: ', main([5,5,5]))
print('Answer is: ', main([1,2,3,4,5,6]))
print('Answer is: ', main([-7,0,1,-5]))
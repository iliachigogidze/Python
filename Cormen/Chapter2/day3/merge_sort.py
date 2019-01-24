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
    else:
        middle_point = len(numbers) // 2
        left = merge_sort(numbers[:middle_point])
        right = merge_sort(numbers[middle_point:])
        return merge(left, right)

  


if __name__ == '__main__':
    print('Answer is: ', main([1,6,3,67,2,32,235,17,-53,-34,-324,5,2]))
    print('Answer is: ', main([]))
    print('Answer is: ', main([6,6,6,6]))
    print('Answer is: ', main([2,4,6,8]))
def main(left, right):
    print('You should merge {} and {}'.format(left, right))

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


print('Answer is: ', main([2,3,7],[4,8,9]))
print('Answer is: ', main([2],[4,8,9]))
print('Answer is: ', main([2,3,7],[4]))
print('Answer is: ', main([],[]))
print('Answer is: ', main([2,3,7],[4,8,9,10,43,132]))



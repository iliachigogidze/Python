def main(numbers):
    print('Numbers is: ', numbers)
    # return merge([1],[2])
    rec(numbers)

def rec(numbers):
    while len(numbers) > 1:
        l = len(numbers) // 2
        r = r + 1
        left = merge(numbers[:l])
        right = merge(numbers[r:])
        merge(left, right)


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
        # print(result)
        # print('l,r:',l,r)
    if l < len(left):
        result.extend(left[l:])
        return result
    elif r < len(right):
        result.extend(right[r:])
        return result
    else:
        return result


print('Answer is: ', main([1,4,7,2,4,5,7,3,9]))



# result = []
#     l = 0
#     r = 0
#     while (l or r) < min(len(left), len(right)):
#         print('l,r: ',l,r )
        
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#         print('l,r: ',l,r )
#     if (l or r) >= min(len(left), len(right)):
#         print('here?')
#         result.append(max(len(left),len(right)[max(l,r):]))
#     return result
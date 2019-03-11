def main(numbers:list) -> int:
    print(f'Find inversions in {numbers}')
    return find_inversions(numbers)[1]


def find_inversions(numbers:list) -> tuple:
    if len(numbers) == 1:
        return numbers, 0 
    middle_point = len(numbers) // 2
    left, left_inv = find_inversions(numbers[:middle_point])
    right, right_inv = find_inversions(numbers[middle_point:])

    result = []
    inversions = 0 + left_inv + right_inv   
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
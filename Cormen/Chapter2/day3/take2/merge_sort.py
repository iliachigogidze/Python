def main(numbers:list) -> list:
    print(f'Sort numbers: {numbers}')
    if len(numbers) == 0:
        return []
    return merge_sort(numbers)


def merge_sort(numbers:list) -> list:
    if len(numbers) == 1:
        return numbers

    middle_point = len(numbers) // 2
    left_list = merge_sort(numbers[:middle_point])
    right_list = merge_sort(numbers[middle_point:])
   
    result = []
    l = 0
    r = 0

    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            result.append(left_list[l])
            l += 1
        else:
            result.append(right_list[r])
            r += 1
    
    result += left_list[l:]
    result += right_list[r:]
    return result


print('Answer is: ', main([5,12,-4,123,14]))
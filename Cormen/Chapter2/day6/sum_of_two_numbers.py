'''
given set S of n numbers and target_value it determines if there exist two elements
in S whose sum is exactly target_value
'''

def main(numbers, target_value):
    print(f'{target_value} in {numbers}')

    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)

    result = False
    for i in range(2, len(sorted_numbers)+1):
        new_numbers = sorted_numbers[:i]
        last = new_numbers[-1]
        # print('laaaaaast: ', last)

        list_for_search = new_numbers[:-1]
        # print('list_for_search: ', list_for_search)

        new_target = target_value - last
        # print('item_for_search: ', new_target)

        if binary_search(list_for_search, new_target):
            result = True
    return result 

def binary_search(numbers, target_value):
    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        
        if len(numbers) == 1:
            if numbers[0] == target_value:
                return True

        if numbers[middle_point] == target_value:
            return True
        elif target_value > numbers[middle_point]:
            numbers = numbers[middle_point+1:]
        elif target_value < numbers[middle_point]:
            numbers = numbers[:middle_point]
    return False


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
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers[0]]
    middle_point = len(numbers) // 2
    left = merge_sort(numbers[:middle_point])
    right = merge_sort(numbers[middle_point:])
    return merge(left, right)



# print('Answer is: ', main(set([5,12,2,6,23,4,13]),7))
# print('Answer is: ', main(set([5,12,2,6,23,4,13]),100))
# print('Answer is: ', main(set([]),100))

# print('Answer is: ', binary_search([1,3,4,5,6],3))
# print('Answer is: ', binary_search([3],3))
# print('Answer is: ', binary_search([1,3,4,5,6],7))
# print('Answer is: ', binary_search([],3))
# print('Answer is: ', binary_search([-2],98))

# print('Answer is: ', merge_sort([5,12,-43,0,324,51]))
# print('Answer is: ', merge_sort([5,5,5]))
# print('Answer is: ', merge_sort([]))

print('Answer is: ', main([6,1,2,4,-2,23],99))
print('Answer is: ', main([6,1,2,4,-2,23],2))
print('Answer is: ', main([6,1,2,4,-2,7],7))
print('Answer is: ', main([6,1,2,4,-2,23],4))
print('Answer is: ', main([6,1,2,4,-2,23],23))


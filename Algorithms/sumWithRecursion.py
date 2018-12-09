'''
unda daitvalo list-shi elementebis jami rekursiit
'''

def sum_of_numbers(nums):
    print('NUMS: ', nums)

    if len(nums) == 1: return nums[0]
    elif not nums:
        print('There is no element in the list')
    else:
        return nums[0] + sum_of_numbers(nums[1:])


print(sum_of_numbers([1,3,2,5,3,0,-1]))
print(sum_of_numbers([1,3,2]))
print(sum_of_numbers([3]))
print(sum_of_numbers([0]))
print(sum_of_numbers([-18,-23]))
print(sum_of_numbers([-18]))
print(sum_of_numbers([]))

# rato agdebs boloshi None-s??????????/





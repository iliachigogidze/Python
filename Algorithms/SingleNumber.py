'''
gadaecema list romelshic yvela ricxvi meordeba garda ertisa da unda davabruno is erti
mag:
[2,2,1] >> 1
[4,4,3,2,2] >> 3
'''


def singleNumber(nums):
    print(nums)
    numbers = [0] * 10
    for num in nums:
        numbers[num % 10] += 1
    print('NUMBERS: ', numbers)
    
    for i in range(len(numbers)):
        print('i: ', numbers[i])
        if numbers[i] == 1:
            return 'ANSWER: ', i
    return False

print(singleNumber([2,3,3]))
print(singleNumber([3,3,2,2,1]))
print(singleNumber([0,1,1,3,3,0,5]))





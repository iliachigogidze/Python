'''
gadaecema list romelshic yvela ricxvi meordeba garda ertisa da unda davabruno is erti
mag:
[2,2,1] >> 1
[4,4,3,2,2] >> 3
'''


def singleNumber1(nums):
    print('NUMS: ', nums)
    for i in nums:
        counter = 0
        for j in nums:
            if i == j:
                #print('i = ',i, ' j = ',j)
                counter += 1
        if counter == 1:
            return i
    return False

# NOTE am amocanis amoxsna 1 xazshi :P
def singleNumber(nums):
    return 0 if not len(nums) else nums[0] ^ singleNumber(nums[1:]) 

print('UNIQUE: ', singleNumber([2,3,3]))
print('UNIQUE: ', singleNumber([3,3,2,2,1]))
print('UNIQUE: ', singleNumber([0,-1,-1,333,333,0,5]))







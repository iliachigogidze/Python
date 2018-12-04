'''
vabrunebt list-shi rac meordeba imas
Input: [1,3,4,2,2]
Output: 2
'''

def findDuplicate(nums):
    print('NUMS: ', nums)
    repeat = []
    
    for i in nums:
        counter = 0
        repeat.append(i)
        for j in nums:
            if i == j:
                counter += 1
                if counter == 2:
                    return i


print('ANSWER: ', findDuplicate([1,3,4,2,2]))
print('ANSWER: ', findDuplicate([1,3,4,4,2]))


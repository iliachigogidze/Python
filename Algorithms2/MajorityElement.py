'''
unda daabruno is elementi, romelic listshi naxevarze metia. mag1: [2,2,2,1,1,3,2] >> '2' (imitom rom 7 elementidan 4 (naxevarze meti) aris '2')
mag2: [3,4,1,1,1] >> '1' (5 dan 3 elementi aris '1')
'''
def majorityElement(nums):
    print('LIST: ', nums)
    max_num = 0
    max_count = 0
    l = len(nums)
    for i in nums:
        count = 0
        num = 0
        for j in nums:
            if i == j:
                count +=1
                num = i
                if max_count > l // 2:
                    return max_num
        if count > max_count:
            max_count = count
            max_num = num
    return max_num


print('ANSWER : ', majorityElement([2,2,1,1,1]))
print('ANSWER : ', majorityElement([2,2,1,1,1,3,3,3,3]))
print('ANSWER : ', majorityElement([2,2,1,1,1,1,0]))

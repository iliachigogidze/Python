'''
13. shemodis listi da am listshi ertnairi mimdebare ricxvebi unda gaskdes.
[1,1,1,2,3,3,4,5,5,4,2] >> yvela skdeba
'''

def main(nums):
    print('Numbers are : ', nums)
    stack = []

    for i in nums:
        deleted = False
        while stack and stack[-1] is i:
            stack.pop()
            deleted = True
        if not deleted:
            stack.append(i)
        print(stack)
    return stack
        
        
        


print('ANSWER: ', main([1,1,1,2,3,3,4,5,5,4,2]))
print('ANSWER: ', main([1,1,1,2,3,3,4,5,5,4,2,8,0]))
print('ANSWER: ', main([1,2,3,3,4,5,5,4,2,8,0,0]))


# assert main([]) == []
# assert main([1,1,1,1,1,1,1,1]) == []             
# assert main([1,1,1,2,3,3,4,5,5,4,2]) == []
# assert main([1,1,1,2,3,3,4,5,5,4,2,8]) == [8]
# assert main([9,1,1,1,2,3,3,4,5,5,4,2,8]) == [9,8]
# assert main([9,7,1,1,1,2,3,3,4,5,5,4,2,8]) == [9,7,8]             
             
             
             
             

    


    # stack = []
    # for x in nums:
    #     b = False
    #     while stack and stack[-1] == x:
    #         b = True
    #         stack.pop()
    #     if not b:
    #         stack.append(x)

    # return stack





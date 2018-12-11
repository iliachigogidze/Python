'''
13. shemodis listi da am listshi ertnairi mimdebare ricxvebi unda gaskdes.
[1,1,1,2,3,3,4,5,5,4,2] >> yvela skdeba
'''

def main(nums):
    # print('NUMS: ', nums)
    # stack = []

    # last = None
    # for i in nums:
    #     #print('i: ', i)
    #     if not stack:
    #         if last != i:
    #             stack.append(i)
    #             last = i
            
    #     else:
    #         #print('last: ', last, ' |  stack[len(stack) - 1: ', stack[len(stack) - 1] == i, '  |  i == last: ', i == last)
    #         if stack[len(stack) - 1 ] == i:
    #             stack.pop()
    #             last = i                    
    #         elif i == last:
    #             last = i
    #         else:
    #             stack.append(i)
    #             last = None
    #     #print(stack)
    #     #print('__________________________________')
    # return stack

    stack = []
    for x in nums:
        b = False
        while stack and stack[-1] == x:
            b = True
            stack.pop()
        if not b:
            stack.append(x)

    return stack


#print('ANSWER: ', main([1,1,1,2,3,3,4,5,5,4,2]))

assert main([]) == []
assert main([1,1,1,1,1,1,1,1]) == []             
assert main([1,1,1,2,3,3,4,5,5,4,2]) == []
assert main([1,1,1,2,3,3,4,5,5,4,2,8]) == [8]
assert main([9,1,1,1,2,3,3,4,5,5,4,2,8]) == [9,8]
assert main([9,7,1,1,1,2,3,3,4,5,5,4,2,8]) == [9,7,8]             
             
             
             
             

    





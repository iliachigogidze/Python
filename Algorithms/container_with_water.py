'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.


Note: You may not slant the container and n is at least 2.


Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''


def maxArea(numbers):
    print('Numbers: ', numbers)
    maxx = 0

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                temp_max = numbers[i] * (j-i)
            else:
                temp_max = numbers[j] * (j-i)
            if temp_max > maxx:
                maxx = temp_max
    return maxx



print('Answer = ', maxArea([1,8,6,2,5,4,8,3,7]))




# class Solution:
#     def maxArea(self, height, result = 0, L = 0):
#         if not height: return 0
#         R = len(height)-1          
#         while L != R:
#             result = max(result, min(height[L], height[R])*(R-L)) <---- es ra sintaqsia vabshe
#             if height[L] < height[R]:
#                 L += 1
#             else:
#                 R -= 1                
#         return result


# class Solution:
#     def maxArea(self, height, result = 0, L = 0):
#         if not height: return 0
#         R = len(height)-1          
#         while L != R:
#             result = max(result, min(height[L], height[R])*(R-L))
#             if height[L] < height[R]:
#                 L += 1
#             else:
#                 R -= 1                
#         return result


    
    


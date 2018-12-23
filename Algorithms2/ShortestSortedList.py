'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

def main(nums):
    print('NUMS: ', nums)
    l = len(nums)
    max_count = l
    
    for i in range(l):
        for j in range(i,l):
            temp_list = nums.copy()
            #print('i: ',i, temp_list[i],  'j: ', j, temp_list[j])
            temp_list[i:j] = sorted(temp_list[i:j])
            #print('TEMP: ', temp_list)
            #print(temp_list[i:j] == sorted(temp_list[i:j]))

            # NOTE es ar varga! es xazi imushavebs O(N*LOGN) shi roca shileba gaketdes O(N)-shi
            if temp_list == sorted(temp_list) and (j-i) < max_count: 
                max_count = j-i
            
            #print('MAX_COUNT: ', max_count)
    return max_count, temp_list[i:j]
                

ex1 = main([2,6,4,8,10,9,15])
print('ANSWER: ', ex1[0], 'LIST: ', ex1[1])

ex2 = main([1,2,1,3,4])
print('ANSWER: ', ex2[0], 'LIST: ', ex2[1])     
     
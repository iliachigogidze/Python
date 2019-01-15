'''
19. Read about merge sort algorithm and implement one in python on your own. 
Think about the time and space complexity of your algorithm? 
Justify your answer by proving it mathematically.
'''

def main(lst):
    print('INPUT: ', lst)

    return mergesort(lst)    

def merge(a,b):
    result = []
    # print(type(a))
    # if type(a) is int:
    #     print(type(b))
    #     if type(b) is int:
    #         result.append(min(a,b))
    #         result.append(max(a,b))
    #         print('aq')
    #         print('result2: ', result)
    #         return result
    # print('oadadas')
    if type(a) is int:
        a = [a]
    if type(b) is int:
        b = [b]
    #print('a ,b: ', type(a), type(b))
    la = len(a)
    lb = len(b)

    i = 0
    j = 0

    while i < la and j < lb:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
        #print('i: ',i, '  | j: ', j)
    while j < lb:
        result.append(b[j])
        j += 1
    while i < la:
        result.append(a[i])
        i += 1
    #print('result: ', result)
    return result

def mergesort(lst):
    if len(lst) < 2:
        return lst[0]
    mid = len(lst) // 2
    a = lst[:mid]
    b = lst[mid:]
    # print('a: ', a)
    # print('b: ', b)

    return merge(mergesort(a), mergesort(b))
    
    # print(a)
    # print(b)




# print(merge([1,4,5],[2,3,6,7]))
print(main([7,4,9,8,0,0,3,0,6,5]))
print(main([0]))
print(main([-5,5]))
print(main([-4,-2,-1,-1,-1,-1]))
print(main([100,100,5,3,0,-10]))
print(main([10,51,49,2,-9,-12,0,0,4,4,2,19]))



# mergesort([0])
# mergesort([])
# mergesort([])
# mergesort([])


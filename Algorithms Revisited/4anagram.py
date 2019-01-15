'''
23. Implement a function that given two strings returns true if and only if they are anagrams. 
Your program must have running time complexity of O(N) where N=max(len(A), len(B)) max length of given 
two strings.   
'''

def main(s1,s2):
    print('s1 and s2: ', s1, ' ', s2)
    dict1 = {}
    dict2 = {}

    if len(s1) is not len(s2):
        return False
    
    for c in s1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    for c in s2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1

    for item in dict1.keys():
        while dict1[item]:
            dict2[item] -= 1
            dict1[item] -= 1        
    
    for i in dict1.values() + dict2.values():
        if i is not 0:
            return False
    return True    



print(main('opa','pao'))
print(main('opaa','pao'))
print(main('opa','paoo'))
print(main('oop','opp'))



# def main(s1, s2):
#     print('STRINGS: ', s1, s2)
    
#     if (len(s1) or len(s2)) is 0:
#         return False

#     if len(s1) != len(s2):
#         return False

#     if sorted(s1) == sorted(s2):
#         return True
#     return False    
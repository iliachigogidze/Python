'''
23. Implement a function that given two strings returns true if and only if they are anagrams. 
Your program must have running time complexity of O(N) where N=max(len(A), len(B)) max length of given two strings.   
'''

def main(s1, s2):
    print('STRINGS: ', s1, s2)
    
    if (len(s1) or len(s2)) is 0:
        return False

    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    return False



print(main('opa','pao'))
print(main('opaa','pao'))
print(main('opa','paoo'))
print(main('oop','opp'))


    
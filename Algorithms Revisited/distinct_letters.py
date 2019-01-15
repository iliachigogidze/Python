'''
17. Given list of distinct letters, generate all possible words so that each letter is used only once per word.
Example: ['b', 'a', 'c'] -> abc acb bac bca cab cba
'''

def perms(s):        
    


print(perms('abc'))





# def perms(s):        
#     if(len(s)==1): 
#         return [s]
#     result=[]
#     for i,v in enumerate(s):
#         print('i: ',i, '   || v: ',v)
#         result += [v+p for p in perms(s[:i]+s[i+1:])]
#         print(result)
#     return result

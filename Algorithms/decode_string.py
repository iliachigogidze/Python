'''
a2b2[2aa2[b3[d]]] >> abbaaabdddbdddaaabdddbddd
'''

stack = []
numbers = ['1','2','3','4','5','6','7','8','9']

def rec(s):
    print('stack: ', stack)
    print('s: ', s)
    # if s:
    #     if s[0] in numbers:
    #         print('a')
    #         stack.append(int(s[0]))
    #         return rec(s[1:])
    #     elif s[0] not in numbers:
    #         print('b')
    #         if stack and str(stack[-1]) not in numbers:
    #             print('c')
    #             return s[0] + rec(s[1:])
    #         elif stack and str(stack[-1]) in numbers:
    #             print('d')
    #             stri = stack[-1] * s[0]
    #             stack.pop()
    #             return stri + rec(s[1:])
    #         elif not stack:
    #             print('e')
    #             return s[0] + rec(s[1:])
    #     else: return ''
    # else:
    #     return ''        
        

    if len(s) == 0:
        return ''
    elif str(s[0]) in numbers:
        stack.append(str(s[0]))
        return rec(s[1:])
    else:
        if stack:
            st = int(stack[-1]) * s[0]
            stack.pop()     
            return st + rec(s[1:])
        if not stack:
            return s[0] + rec(s[1:])


print(rec('4w3a2b'))
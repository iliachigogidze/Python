'''
stringi shemodis da unda daitvalo qvestringebis raodenoba romelic palindromia 
'''

# def problem(n):
#     result = 0
#     if len(n) == 0:
#         return 0
#     for i in len(n):


#     return result

# def is_palindrome(n):
#     n = ''.join(n.split(' ')).lower()
#     l = len(n)
#     for i in range(l):
#         if n[i] != n[l-1]:
#             return False
#         l -= 1
#     return True
# palindromes = 0

# def problem(n):
#     global palindromes
#     n = ''.join(n.split(' ')).lower()
#     l = len(n)
#     x = 0
#     y = 0
#     if is_palindrome(n,l, first_time = True):
#         #mashin naxevarze vamowmebt
#         for i in range(l // 2 - 1):
#             for j in range(l // 2 -1):
#                 if is_palindrome(n[i:j],len(n[i:j])):
#                     palindromes += 1
#     else:
#         #mtlianze vamowmebt
#         for i in range(l-1):
#             for j in range(l-1):
#                 if is_palindrome(n[i:j],len(n[i:j])):
#                     palindromes += 1

# def is_palindrome(n,l,first_time = False):
#     global palindromes
#     x = 0
#     y = 0
#     print('len: ', l)
#     if (l % 2 == 0):
#         x = l / 2 - 1
#         y = l / 2        
#     else:
#         x = l // 2
#         y = l // 2
#     for i in range(l // 2):
#         print('X: ', x, 'Y: ', y)
       
#         if n[int(x)] == n[int(y)]:
#             x -= 1
#             y += 1
#             print('X: ', x, 'Y: ', y)
#             if first_time == True:
#                 palindromes += 1
#             #print('Palindrome')
#         else:
#             #print('Stop')
#             return False
#     return True
    
#     print('L/2: ', l / 2, 'L//2: ', l // 2, 'L%2: ', l % 2)

def main(n):
    res = 0
    n = len(n)
    for i in range(n):
        for j in range(i,n):
            ok  = True
            for k in range(i,(j-i+1)//2):
                if n[i+k] != n[j-k]:
                    ok = False
                    break
                if ok:
                    res += 1
    return res


x = input("Enter string: ")
print(main(x))        
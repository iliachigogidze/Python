'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''
def problem(n):
   
    open_braces = ['{', '(', '[']
    close_braces = ['}', ')', ']']
    stack= []

    x = 0
    y = 0
    l = len(n)

    if l % 2 != 0:
        return False

    # NOTE es for bloki shegilia shecvalo erti xazit: if n[0] in close_braces: return False
    for i in close_braces:
        if n[0] == i:
            return False
    
    # NOTE esec winas pontshi
    for i in open_braces:
        if n[l-1] == i:
            return False
    

    # NOTE !!!!!!!!!!!!!!!!
    # WRONG SOLIUTION: (())() - amaze errors agdebs kodi vabshe. kargad dateste xolme.

    stack.append(n[0])
    for i in range(1,l):
        print('STACK: ', stack, '   LEN: ', len(stack))
        if stack: 
            if n[i] == '}': #stack[len(stack) - 1]
                if stack[len(stack) - 1] == '{': # NOTE igivea rac pirdapir -1
                    stack.pop()
                else:                 
                    stack.append(n[i])
            elif n[i] == ']':
                if stack[len(stack) - 1] == '[':
                    stack.pop()
                else:
                    stack.append(n[i])
            elif n[i] == ')':
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                else:
                    stack.append(n[i])
            elif n[i] == '{': #stack[len(stack) - 1]
                if stack[len(stack) - 1] == '}':
                    stack.pop()   
                else:              
                    stack.append(n[i])
            elif n[i] == '[':
                if stack[len(stack) - 1] == ']':
                    stack.pop()
                else:
                    stack.append(n[i])
            elif n[i] == '(':
                if stack[len(stack) - 1] == ')':
                    stack.pop()
                else:
                    stack.append(n[i])
            else:
                return False
        
    
    if len(stack) == 0:
        return True
    else:
        return False


x = (input("Enter Braces: "))
print(problem(x))


# NOTE es amoxsna is fucking wrong! 
# NOTE tavidanaa dasaweri axali tesloba metodit
def main(str):
    braces = {']':'[', '}':'{', ')':'('}

    print('BRACES: ', str)
    stack = []

    if not str:
        print('No Braces were provided')
    elif str[0] in braces:
        return False
    else:
        if str[-1] in braces.values():
            return False
    
    for i in str:
        if i in braces.values():
            stack.append(i)
        else:
            if not stack:
                return False
            if stack[-1] == braces[i]:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print('ANSWER: ', main('{}{}'))
print('ANSWER: ', main('())'))
print('ANSWER: ', main('{[]})'))
print('ANSWER: ', main(')([]'))
print('ANSWER: ', main('{[()]}'))
print('ANSWER: ', main('((((('))

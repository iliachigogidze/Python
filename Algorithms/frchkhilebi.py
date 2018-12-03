'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''
def problem(n):
   
    open_braces = ['{', '(', '[']
    close_braces = ['}', ')', ']']

    answer = False
    x = 0
    y = 0
    l = len(n)

    if l % 2 != 0:
        return answer
    
    x = int(l / 2 - 1)
    y = int(l / 2)

    for i in range(int(l/2)):
        if n[x] != n[y]:
            return answer
        x += -1
        y += 1   

    answer = True     
    return answer




x = (input("Enter Braces: "))
print(problem(x))


# NOTE es amoxsna is fucking wrong! 
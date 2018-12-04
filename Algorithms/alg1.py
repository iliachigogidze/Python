'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''
def problem(n):
    # minusebze ar cherdeba loop amitom vamravleb (-1)-ze
    if n < 0:  # NOTE am ifis magivrad shegidzlia dawero mxolod erti xazi: n = abs(n)
        n = -n

    max = 0
    while n!=0: # NOTE n!=0-is magivrad shegidzlia dawero pirdapir n. pythonshi 0 aris False da aranuli True. 
        
        last_digit = n % 10
        if last_digit > max:
            max = last_digit
        n //= 10
    return max

x = int(input("Enter Integer: "))
print(problem(x))
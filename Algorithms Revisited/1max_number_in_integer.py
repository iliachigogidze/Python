'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''

def problem(n):
    print('number is: ', n)
    maxx = 0
    
    if n is 0:
        return 0
    
    n = abs(n)

    while n:
        if n % 10 > maxx:
            maxx = n % 10
        n //= 10
    return maxx



x = int(input("Enter Integer: "))
print(problem(x))










# def problem(n):
#     # minusebze ar cherdeba loop amitom vamravleb (-1)-ze
#     if n < 0:  # NOTE am ifis magivrad shegidzlia dawero mxolod erti xazi: n = abs(n)
#         n = -n

#     max = 0
#     while n!=0: # NOTE n!=0-is magivrad shegidzlia dawero pirdapir n. pythonshi 0 aris False da aranuli True. 
        
#         last_digit = n % 10
#         if last_digit > max:
#             max = last_digit
#         n //= 10
#     return max
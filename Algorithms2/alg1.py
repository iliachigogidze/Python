'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''

def main(n):
    print('Input is: ', n)

    mx = 0
    if not n:
        return 0

    n = abs(n)

    while n:
        a = n % 10
        if a > mx:
            mx  = a
        n //= 10
    return mx



# def main(n):
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

while True:
    x = int(input("Enter 0 to exit. Enter Integer: "))
    if x is 0:
        break
    print(main(x))
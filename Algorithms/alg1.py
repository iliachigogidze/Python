'''
mocemul int-shi unda vipovot maqsimaluri cifri
'''
def problem(n):
    # minusebze ar cherdeba loop amitom vamravleb (-1)-ze
    if n < 0:
        n = -n

    max = 0
    while n!=0:
        
        last_digit = n % 10
        if last_digit > max:
            max = last_digit
        n //= 10
    return max

x = int(input("Enter Integer: "))
print(problem(x))
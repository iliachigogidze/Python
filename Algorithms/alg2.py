'''
abrunebs ricxvshi unikaluri cifrebis raodenobas
'''

def problem(n):
    uniques = []
    while n:
        if n % 10 not in uniques:
            uniques.append(n % 10)
            #print(uniques)
        
        n //= 10
    return len(uniques)

x = int(input("Enter Integer: "))
print(problem(x))
        
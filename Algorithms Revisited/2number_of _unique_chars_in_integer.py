'''
abrunebs ricxvshi unikaluri cifrebis raodenobas
'''


def problem(n):
    print('Number is: ', n)
    numbers = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    if n is 0:
        return 1
    n = abs(n)
    while n:
        numbers[n % 10] += 1
        n //= 10

    counter = 0
    for item in numbers:
        if numbers[item] is 1:
            counter += 1
    return counter


x = int(input("Enter Integer: "))
print(problem(x))




# NOTE am amocanis uketesad amoxsna shegidzlia 10 elementiani list-is shemogebit
# da shesabamis indeqsze True-s chawera tu es cifri shegxvda. bolos pasuxia False-ebis 
# raodenoba listshi.


# NOTE rodesac bitwise operatorebs gaarchev shemaxsene gavarchiot es amocana list-ebis gareshe.

        
################################
#dzveli amoxsna
################################


# def problem(n):
#     uniques = []
#     while n:
#         # NOTE rodesac kutvnilebas amowmeb jobia gamoiyeno SET da ara LIST. LIST-shi 
#         # kutvnilebis shemowmebas unda O(listis sigrdze) dro, da SET-shi sashualod O(1). 
#         if n % 10 not in uniques: 
#             uniques.append(n % 10)
#             #print(uniques)
        
#         n //= 10
#     return len(uniques)

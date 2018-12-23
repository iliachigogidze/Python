'''
dawere programa romelic ricxvebis masividan amoshlis gameorebul ricxvebs da bolos
dagitovebs marto unikalur ricxvebs igive tanmimdevrobit rac tavidanve iyo. 3 4 4 5 1 5 -> 3 4 5 1
'''

def uniques(nums):
    # print('NUMS: ', nums)
    # uniques = []
    # for i in nums:
    #     if i not in uniques:
    #         uniques.append(i)

    # return uniques


    print('NUMS: ', nums)
    uniques = []
    for i in nums:
        if not in_uniques(i, uniques):
            uniques.append(i)

    return uniques

# NOTE saxeli aralogikuradaa darqmeuli. is_unique logikurad True unda iyos tu Uniquea da ara piriqit.
def in_uniques(i, uniques):
    for x in uniques:
        if x == i:
            return True
    return False

print('UNIQUES: ', uniques([-99,0,0,2,2,4,4]))
print('UNIQUES: ', uniques([-99,0,0,22,3,22,4,4,99]))
print('UNIQUES: ', uniques([3]))
print('UNIQUES: ', uniques([3,-3,-2,3,1,3,4]))



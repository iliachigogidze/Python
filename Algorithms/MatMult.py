'''
9. dawere funqcia romelshic shedis ori matrica (listebis listi an sheni matricis klasi
sheqmeni) da gamodis mati namravli.
'''

def mat_mult(mat1, mat2):
    mat1_m = len(mat1) # row
    mat1_n = len(mat1[0]) #column
    
    mat2_m = len(mat2) # row
    mat2_n = len(mat2[0]) # columns
    
    print('mat1_n', mat1_n, '  mat2_m: ', mat2_m)
    
    if mat1_n != mat2_m:
        print('Wrong dimensions! Matrices can\'t be multiplied!')

    mult = []
    for a in range(mat1_m):
        mult.append([0]*mat2_n)
    
    print(mult)

    for i in range(mat1_m):
        print('i: ', i)
        for j in range(mat2_n):
            print('j: ', j)
            #mult[i][j]
            total = 0
            print('mat1_n-1: ',mat1_n)
            for k in range(mat1_n):
                print('k: ', k)
                print('mat1[i][k]: ', mat1[i][k], 'mat2[k][i]: ',mat2[k][i])
                total += mat1[i][k] * mat2[k][i]
            print('total: ', total)
            mult[i][j] = total
            print('MULT: ', mult)
    return mult 


print('ANSWER: ', mat_mult([[2,2],[3,3]], [[5,5],[5,5]]))
    
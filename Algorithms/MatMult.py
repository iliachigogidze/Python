'''
9. dawere funqcia romelshic shedis ori matrica (listebis listi an sheni matricis klasi
sheqmeni) da gamodis mati namravli.
'''

def mat_mult(mat1, mat2):
    mat1_m = len(mat1)
    mat1_n = len(mat1[0])
    
    mat2_m = len(mat2)
    mat2_n = len(mat2[0])
    
    print('mat1_n', mat1_n, '  mat2_m: ', mat2_m)
    
    if mat1_n != mat2_m:
        print('Wrong dimensions! Matrices can\'t be multiplied!')

    mult = []
    for a in range(mat1_m):
        mult.append([0]*mat2_n)
    
    print(mult)

    for i in range(mat1_m-1):
        print('i: ', i)
        for j in range(mat2_n-1):
            print('j: ', j)
            #mult[i][j]
            total = 0
            for k in range(mat1_n-1):
                print('k: ', k)
                total += mat1[i][k] * mat2[k][i]
            mult[i][j] = total
    return mult 


print(mat_mult([[1,1],[1,1]], [[2,2],[2,2]]))
    
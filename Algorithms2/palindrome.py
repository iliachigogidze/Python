'''
stringi shemodis da unda daitvalo qvestringebis raodenoba romelic palindromia 
'''

def main(n):
    res = 0
    n = len(n)
    for i in range(n):
        for j in range(i,n):
            ok  = True
            for k in range(i,(j-i+1)//2):
                if n[i+k] != n[j-k]:
                    ok = False
                    break
                if ok:
                    res += 1
    return res


x = input("Enter string: ")
print(main(x))    

# NOTE amas ro miiyvan bolomde dauwere test-ebic (shegidzlia gamoiyeno assert an unit test).
# edge-case-ebze shemowmeba ar dagaviwydes.
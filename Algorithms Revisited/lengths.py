'''
26. ori monakveti shemodis (2, 7) anu x gherdze 2dan 7is chatvlit.
'''

result = []

def main(cords):
    for cord in cords:    
        # if not result:
        #     result.append(cord)
        for i,pair in enumerate(result):
            print('pair= ', pair)
            print(any(elem in cord for elem in pair))
            print('result = ', result)
            condition = any(elem in range(cord[0], cord[1]) for elem in pair)
            if condition:
                #mashin ikveteba # aq rogor davamtavro didi for loop?
                overlap(pair, cord, i) 
        result.append(cord)
    return result


def overlap(pair, cord, i):
    if cord[0] < pair[0]:
        result[i][0] = cord[0]
    if cord[1] > pair[1]:
        result[i][1] = cord[1]
            
        
print(main([[1,3],[2,5],[4,10]]))
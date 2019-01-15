'''
Write a recursive function that finds and returns the minimum element in an array, 
'''

def main(lst):
    print("LIST: ", lst)
    if not lst:
        print('List is empty bitch')
    else:
        return recursion(lst)

def recursion(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0],recursion(lst[1:]))

print('ANSWER: ', main([4,-3,2,99,0,-10,7,5,3,0,0,1]))
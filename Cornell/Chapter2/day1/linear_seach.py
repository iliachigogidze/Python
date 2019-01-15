def main(numbers, v):
    print('You should find --{}-- in {}'.format(v, numbers))

    for i in range(len(numbers)):
        if numbers[i] is v:
            return i
    return None

print('Answer is: ', main([5,1,3,8,6,-2,4], 8))
print('Answer is: ', main([5,1,3,8,6,-2,4], 9))

def main(numbers, value):
    print('You should find {} in {}'.format(value, numbers))

    for i in numbers:
        if i is value:
            return True
    return False

print('Answer is: ', main([5,4,2,2,2,-9,0,-10,0],2))
print('Answer is: ', main([5,4,2,2,2,-9,0,-10,0],8))

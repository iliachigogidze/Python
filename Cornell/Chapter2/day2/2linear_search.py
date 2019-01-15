def main(numbers, value):
    print(f'You should find {value} in {numbers}')

    for i, num in enumerate(numbers):
        if num is value:
            return f'{value} is at {i+1} position'
    return f'There is no {value}'


print('Answer is: ', main([-3,-2.2,9,0,0,9],9))
print('Answer is: ', main([-3,-2.2,9,0,0,9],8))

def main(numbers, target_value):
    print(f'You should find {target_value} in {numbers}')

    while len(numbers) >= 1:
        middle_point = len(numbers) // 2
        if numbers[middle_point] == target_value:
            return True 
        
        if numbers[middle_point] < target_value:
            numbers = numbers[middle_point+1:]
        else:
            numbers = numbers[:middle_point]
    return False

print('Answer is: ', main([5,2,6,7,1,2],2))
print('Answer is: ', main([],2))
print('Answer is: ', main([5,2,6,7,1,2],9))
print('Answer is: ', main([9],9))
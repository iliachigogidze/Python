'''
shemomaval integer-shi unda daalago cifrebi klebis mixedvit da ise gamoitano
'''

def main(n):
    print('number: ', n)
    numbers = [0] * 10
    answer = 0

    while n:
        numbers[n % 10] += 1
        n //= 10


    for i in range(len(numbers)-1,-1,-1): # NOTE len(numbers) ar ginda imitoro ici ro 10-s udris yoveltvis
        while numbers[i]:
            answer = answer * 10 + i
            numbers[i] += -1 # NOTE -= 1 jobia 

    return answer

x = int(input('Enter Integer: '))
print('LIST: ', main(x))
    
    # numbers = [0] * 10
    # answer = 0
    
    # while n:
    #     numbers[temp % 10] += 1
    #     n //= 10
    
    # for i in range(len(numbers)- 1, -1,-1):
    #     if i != 0:
    #         answer +


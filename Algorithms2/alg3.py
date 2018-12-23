'''
shemomaval integer-shi unda daalago cifrebi klebis mixedvit da ise gamoitano
'''
class Solution:
    def __init__(self, n):
        self.n = n
        self.answer = 0
        pass

    def main(self):
        while self.n != 0:
            last = self.n % 10
            self.f(last)
            self.n //= 10
        return self.answer

    def f(self, last):
        print('LAST: ',last)
        print(last <= self.answer % 10 or self.answer == 0)
        if last <= self.answer % 10 or self.answer == 0:
            self.answer = self.answer * 10 + last
            print('SELF ANSWER: ', self.answer)
        else:
            loss = 0
            counter = 1
            temp_answer = self.answer
            print('TEMP: ', temp_answer)
            while last > temp_answer % 10:
                loss = (temp_answer % 10) * counter + loss 
                print('LOSS: ', loss)
                temp_answer //= 10
                print('TEMP_AN: ', temp_answer)
                counter *= 10
                if temp_answer == 0:
                    break
                #print('LOSS: ', loss, 'temp_answer: ', temp_answer, 'counter: ', counter, 'answer: ', self.answer)
            self.answer = temp_answer * 10 * counter + last * counter + loss





x = int(input('Enter Integer: '))
solution = Solution(x)
print(solution.main())
        
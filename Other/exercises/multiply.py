'''
Let's say you want to multiply the output by a variable amount. 
You could define the decorator and use it as follows:
'''

def mult(n):
    def wrapper(f):
        def inner(*args, **kwargs):
            result = f(*args, **kwargs) * n
            return result 
        return inner
    return wrapper


# @mult(3)
def num(num:int) -> int:
    return num

num = mult(4)(num)

print(num(3))
print(mult(5)(2))
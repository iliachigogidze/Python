def my_decorator(f):
    def inner(list_of_values):
        return [f(value) for value in list_of_values]
    return inner

@my_decorator
def uppercase(s):
    '''turn word_like_this to WORD LIKE THIS'''

    return ''.join([word.upper() for word in s.split('_')])

print(uppercase(['ilia_chigogidze', 'nika_chigogidze']))


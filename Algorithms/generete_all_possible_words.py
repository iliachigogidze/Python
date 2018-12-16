'''
17. Given lis of disinct letters, generate all possible words so that each letter is used only once per word.
Example: ['b', 'a', 'c'] -> abc acb bac bca cab cba
'''

def main(s):
    print('String: ', s)
    chunks = []
    chunks.append(s[-1])
    words = generate_strings_with_swaping(chunks)

    for i in range(1,len(s)):
        b = s[-i-1]
        chunks = words
        chunks = concatenate(b,chunks)
        words = generate_strings_with_swaping(chunks)
        chunks = words

    return chunks
    


def generate_strings_with_swaping(s):
    strings = []
    for chunk in s:
        result = chunk
        for _ in range(len(chunk)):
            result = result[-1] + result[:-1]
            strings.append(result)
    return strings

def concatenate(last_char, words):
    result = []
    for i in words:
        result.append(last_char + i)
    return result   

print('ANSWER: ', main('abc'), '  |  len = ',len(main('abc')))
print('____________________________________')
print('ANSWER: ', main('abcd'))
print('____________________________________')
print('ANSWER: ', main('a'))
print('____________________________________')
print('ANSWER: ', main('abcde'))
print('____________________________________')
print('ANSWER: ', main('aocm'))
print('____________________________________')




# print(generate_strings_with_swaping(['ab','op','m']))
# print(concatenate('c',['ab','bbb','db']))
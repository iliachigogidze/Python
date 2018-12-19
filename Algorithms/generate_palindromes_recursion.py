'''
18. Given a list of distinct letters and a positive number N, generate all possible palindromes 
having the length not greater than N. Single word can be used multiple times per palindrome. Example: ['a', 'b'], N=3  a aa aaa b bb bbb aba bab
'''

def main(ls, n):
    print('List: ', ls)

    word = 'a' * n
    return recursion(word, ls)

def recursion(word,ls):
    if len(word) == 0: return ['']
    elif len(word) == 1: return [c for c in ls]
    else:
        word = word[1:-1]
        word = recursion(word,ls)

        palindromes = []
        for w in word:
            palindromes.append(w)
            for c in ls:
                if c is w:
                    palindromes.append(c+w)
                palindromes.append(c+w+c)
        return palindromes


print(main(['a','b'], 4))
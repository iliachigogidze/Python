from sklearn.svm import SVC

SVC

def underline(f):
    def wrapper(*args, **kwargs):
        return '<u>' + f(*args, **kwargs) + '<u>'
    return wrapper


def italic(f):
    def wrapper(*args, **kwargs):
        return '<i>' + f(*args, **kwargs) + '<i>'
    return wrapper


def bold(f):
    def wrapper(*args, **kwargs):
        return '<b>' + f(*args, **kwargs) + '<b>'
    return wrapper

    
@underline
@italic
@bold
def text_print(text:str) -> str:
    return text


print(text_print('hello world'))

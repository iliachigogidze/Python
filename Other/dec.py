def fucking(exp):
    def my_decorator(f):
        def wrap(*args, **kwargs):
            results = f(*args, **kwargs)
            new_result = [i**exp for i in results]
            return new_result
        return wrap
    return my_decorator

@fucking(3)
def ranges(s,e):
    result = [i for i in range(s,e)]
    return result

print(ranges(2,6))

import time

def timeis(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrap

def printList(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        print(*args[1])
        for i in result:
            print([str(x) for x in i])
    return wrap
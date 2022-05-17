import time
import datetime

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
        txt = '|'
        underline = '='
        for i in args[1]:
            txt += ' {:^20} |'.format(i)
            underline += 23*'='
        print(txt)
        print(underline)
        for i in result:
            txt = '|'
            for v in i:
                if isinstance(v, datetime.datetime):
                    txt += ' {:^20} |'.format(v.strftime('%d/%m/%Y'))
                else:
                    txt += ' {:^20} |'.format(str(v))
            print(txt)
    return wrap
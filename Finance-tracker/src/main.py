from .utils import sql_commands

import time

def timeis(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrap

def conprint(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in result:
            print([str(x) for x in i])
    return wrap

@conprint
def get_users():
    conn = sql_commands.connectdb()
    result = sql_commands.select(conn,
                        'users', 
                        ['user_id', 'name', 'created_on'])
    conn.close()
    return result

@conprint
def get_categories():
    conn = sql_commands.connectdb()
    result = sql_commands.select(conn,
                        'categories', 
                        ['category_id', 'name', 'created_on'])
    conn.close()
    return result

@conprint
def get_transactions():
    conn = sql_commands.connectdb()
    result = sql_commands.select(conn,
                        'Finances', 
                        ['transaction_id', 'money', 'user_id', 'category_id', 'created_on'])
    conn.close()
    return result
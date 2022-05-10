from .utils import sql_commands, decorators

@decorators.printList
def get_data(table, columns):
    """
    gets data from postgres server

    Args:
        table (str): table name
        columns (list[str]): list of colum names

    Returns:
        list[list[dif types]]: wanted data
    """
    conn = sql_commands.connectdb()
    result = sql_commands.select(conn,
                        table, 
                        columns)
    conn.close()
    return result

def insert_data(table, columns):
    conn = sql_commands.connectdb()
    result = sql_commands.insertinto(conn,
                        table, 
                        columns)
    conn.close()
    return result
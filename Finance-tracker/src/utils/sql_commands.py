import psycopg2

def connectdb(database="financedb", 
                user="myusername", 
                password="mypassword",
                host="localhost",
                port="5433"):
    """
    connectdb - connects to db

    Args:
        database (str): Name of database. Defaults to "Financedb".
        user (str): Username. Defaults to "myusername".
        password (str): Password. Defaults to "mypassword".
        host (str): Server host. Defaults to "localhost".
        port (str): Server port. Defaults to "5433".

    Returns:
        conn: psycopg2 connection
    """
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    return conn

def insertinto(conn, table, values):
    """
    insersts into table

    Args:
        conn (conn): psycopg2 connection
        table (str): name of table to insert into
        values (dict): {column1: value1, column2: value2, ...}
    """
    cmdcolumns = ""
    cmdvalues = ""
    for col, val in values.items():
        cmdcolumns += f"{col}, "
        cmdvalues += f"'{val}', "
    cmdcolumns = cmdcolumns[:-2]
    cmdvalues = cmdvalues[:-2]
    cmd = f"INSERT INTO {table} ({cmdcolumns}) VALUES ({cmdvalues})"
    
    cur = conn.cursor()
    cur.execute(cmd)
    conn.commit()

def select(conn, table, columns):
    """
    SQL SELECT command

    Args:
        conn (conn): psycopg2 connection
        table (str): name of table
        columns (list[str]): list of column names

    Returns:
        list[set]: List of set of records
    """
    cmdcolumns = ", ".join(columns)
    cmd = f"SELECT {cmdcolumns} FROM {table}"
    
    cur = conn.cursor()
    cur.execute(cmd)
    result = cur.fetchall()

    return result


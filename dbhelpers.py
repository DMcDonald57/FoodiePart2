import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(
            user = dbcreds.user,
            password = dbcreds.password,
            host = dbcreds.host,
            port = dbcreds.port,
            database = dbcreds.database,
            autocommit = True
            )

        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as e:
        print("Operational Error:", e)
    except Exception as e:
        print("Unexpected Error:",e)

def disconnect_db(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as e:
        print("Operational Error:", e)
    except mariadb.InternalError as e:
        print("Internal Error:",e)
    except Exception as e:
        print("Unexpected Error:",e)

def execute_statement(cursor,statement,args={}):
    try:
        cursor.execute(statement, args)
        result = cursor.fetchall()
        return result
    except mariadb.ProgrammingError as e:
        if "doesn't have a result set" in e.msg:
            return None
        print("Syntax error in your SQL statement:", e)
        return str(e)
    except mariadb.IntegrityError as e:
        print("the statement failed to execute due to intergity error,", e)
        return str(e)
    except mariadb.DataError as e:
        print("data error:",e)
        return str(e)
    except Exception as e:
        print("Unexpected Error:",e)
        return str(e)

def run_statement(statement, args=[]):
    cursor = connect_db()
    if (cursor == None):
        print("Failed to connect to DB, statement will not run")
        return  None
    result = execute_statement(cursor, statement, args)
    disconnect_db(cursor)
    return result
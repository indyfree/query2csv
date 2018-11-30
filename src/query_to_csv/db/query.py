from query_to_csv import db
from query_to_csv import output

def execute_query(query):
    try:
        conn = db.by_pymysql()
        cursor = conn.cursor()

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    except Exception as e:
        output.print_query_failed(e)


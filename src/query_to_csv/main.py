from query_to_csv import db
from query_to_csv import write as w
from query_to_csv import output

QUERY = """
        SELECT *
        FROM procom.trades
        WHERE exec_time
        BETWEEN '2016-05-31 00:00:00' AND '2018-01-31 00:00:00'
        """

FILENAME = "procom_data.csv"


def main():
    output.print_header()
    output.print_start()

    query_result = db.execute_query(QUERY)
    w.write_data_to_csv(query_result, FILENAME)

    output.print_query_succeeded(FILENAME)


if __name__ == "__main__":
    main()

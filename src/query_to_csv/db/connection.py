import pymysql
from dotenv import find_dotenv, load_dotenv
import os
import sys

from query_to_csv import output


# load up the .env entries as environment variables
load_dotenv(find_dotenv())

db_user = os.getenv("DB_USER")
db_pw = os.getenv("DB_PW")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_schema = os.getenv("DB_SCHEMA")

if not all([db_user, db_pw, db_host, db_port, db_schema]):
    raise ValueError("Could not load all required credentials from .env")


def by_pymysql():
    try:
        conn = pymysql.connect(
            host=db_host, user=db_user, passwd=db_pw, db=db_schema, port=int(db_port)
        )

        return conn

    except Exception as e:
        output.print_connection_failed(e)
        sys.exit(1)

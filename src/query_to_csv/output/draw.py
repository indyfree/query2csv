import click as c
import datetime

from query_to_csv import write as w

def print_start():
    c.secho('start building csv-file')
    c.secho('└── executed: {}'.format(datetime.datetime.now()))


def print_connection_failed(error):
    c.secho('\nCan not connect to db!', fg='red', bold=True)
    c.secho('error occured:\n└── {}'.format(error))


def print_query_failed(error):
    c.secho('\nQuery failed!', fg='red', bold=True)
    c.secho('error occured:\n└── {}'.format(error))


def print_query_succeeded(filename):
    c.secho('\nSuccessfully build csv-file!', fg='green', bold=True)
    c.secho('csv-file written to:\n└── {}'.format(w.OUTPUT_DIR + filename))


def print_header():
    img = """
                         ___             
 ___ ___ _____ ______ __|_  |________  __
/ _ `/ // / -_) __/ // / __// __(_-< |/ /
\_, /\_,_/\__/_/  \_, /____/\__/___/___/ 
 /_/             /___/                                                                     
"""
    c.secho(img, bold=True, fg='blue')

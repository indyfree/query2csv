import csv

from query_to_csv import write as w


def write_data_to_csv(query_data, FILENAME):

    with open(w.OUTPUT_DIR + FILENAME, "w") as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in query_data:
            writer.writerow(row)

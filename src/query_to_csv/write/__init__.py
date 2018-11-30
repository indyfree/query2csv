from .csv_writer import write_data_to_csv

from pathlib import Path

PROJECT_DIR = str(Path(__file__).resolve().parents[3])
OUTPUT_DIR = PROJECT_DIR + '/out/'
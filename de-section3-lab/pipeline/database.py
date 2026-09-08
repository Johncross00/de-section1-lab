import duckdb

DB_PATH = "data/airtravel.duckdb"


def get_connection():
    return duckdb.connect(DB_PATH)
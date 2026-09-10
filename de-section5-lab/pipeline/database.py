import duckdb

DB_PATH = "data/lab5.duckdb"

def get_connection():
    return duckdb.connect(DB_PATH)
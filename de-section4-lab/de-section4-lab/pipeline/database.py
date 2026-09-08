import duckdb

DB_PATH = "data/lab4.duckdb"

def get_connection():
    return duckdb.connect(DB_PATH)
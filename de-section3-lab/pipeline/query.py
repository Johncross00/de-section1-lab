import duckdb


def show_results():
    conn = duckdb.connect("data/airtravel.duckdb")

    print("\n=== ETL Table ===")
    print(conn.sql("""
        SELECT *
        FROM air_travel_etl
    """).df())

    print("\n=== ELT Table ===")
    print(conn.sql("""
        SELECT *
        FROM air_travel_elt
    """).df())

    conn.close()
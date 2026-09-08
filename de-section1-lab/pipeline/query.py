import duckdb

from pipeline.config import SILVER_FILE, GOLD_FILE


def query_examples():
    """
    Execute SQL queries directly on Parquet files.
    """

    print("\nRunning SQL queries with DuckDB...")

    con = duckdb.connect(database=":memory:")
    try:
        # Query Silver dataset
        q1 = con.execute(f"""
            SELECT
                sex,
                smoker,
                AVG(tip_pct) AS avg_tip_pct,
                SUM(total_bill) AS revenue
            FROM read_parquet('{SILVER_FILE.as_posix()}')
            GROUP BY sex, smoker
            ORDER BY avg_tip_pct DESC
        """).df()

        print("\n=== SQL on Silver ===")
        print(q1)

        # Query Gold dataset
        q2 = con.execute(f"""
            SELECT
                day,
                AVG(avg_tip_pct) AS avg_tip_pct
            FROM read_parquet('{GOLD_FILE.as_posix()}')
            GROUP BY day
            ORDER BY avg_tip_pct DESC
        """).df()

        print("\n=== SQL on Gold ===")
        print(q2)
    finally:
        con.close()

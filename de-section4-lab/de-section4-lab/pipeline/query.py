from pipeline.database import get_connection


def batch_query():

    conn = get_connection()

    result = conn.execute("""
        SELECT
            customer,
            SUM(total) AS total_spent
        FROM read_parquet('data/transactions_summary.parquet')
        GROUP BY customer
        ORDER BY total_spent DESC
    """).df()

    print("\nBatch Result\n")

    print(result)

    conn.close()
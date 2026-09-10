from pipeline.database import get_connection


def warehouse_query():

    conn = get_connection()

    query = """
    SELECT
        c.name AS customer,
        p.name AS product,
        SUM(f.amount) AS total

    FROM read_parquet('data/fact_sales.parquet') f

    JOIN read_parquet('data/dim_customer.parquet') c
        ON f.customer_id = c.customer_id

    JOIN read_parquet('data/dim_product.parquet') p
        ON f.product_id = p.product_id

    GROUP BY
        c.name,
        p.name

    ORDER BY total DESC
    """

    result = conn.execute(query).df()

    print("\n=== Warehouse Query ===\n")
    print(result)

    conn.close()
from pipeline.database import get_connection


def run_lakehouse():

    print("\n" + "=" * 50)
    print("Lakehouse Query")
    print("=" * 50)

    conn = get_connection()

    query = """

    SELECT

        s.customer_id,

        e.user,

        s.amount,

        e.action

    FROM read_parquet('data/fact_sales.parquet') s

    JOIN read_json_auto('data/raw_events.json') e

        ON lower(e.user)=lower(

            (

                SELECT name

                FROM read_parquet('data/dim_customer.parquet')

                WHERE customer_id=s.customer_id

            )

        )

    """

    result = conn.execute(query).df()

    print(result)

    conn.close()
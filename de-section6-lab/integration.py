import duckdb


def run_integration():

    print("\n" + "=" * 50)
    print("Multi-Cloud Integration")
    print("=" * 50)

    conn = duckdb.connect()

    result = conn.execute("""

        SELECT
            'AWS' AS cloud,
            COUNT(*) AS records
        FROM read_csv_auto('aws_s3_bucket/transactions.csv')

        UNION ALL

        SELECT
            'Azure' AS cloud,
            COUNT(*) AS records
        FROM read_parquet('azure_blob_container/revenue.parquet')

        UNION ALL

        SELECT
            'GCP' AS cloud,
            COUNT(*) AS records
        FROM read_json_auto('gcp_storage_bucket/events.json')

    """).df()

    print(result)

    conn.close()
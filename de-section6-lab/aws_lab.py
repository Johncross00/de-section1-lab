from pathlib import Path

import duckdb
import pandas as pd

AWS_BUCKET = Path("aws_s3_bucket")
AWS_BUCKET.mkdir(exist_ok=True)


def run_aws():

    print("=" * 50)
    print("AWS S3 + Athena")
    print("=" * 50)

    # Simulation d'un upload vers S3
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Eve"],
        "spend": [120, 300, 500]
    })

    df.to_csv(
        AWS_BUCKET / "transactions.csv",
        index=False
    )

    print("[AWS] Uploaded to simulated S3 bucket")

    conn = duckdb.connect()

    result = conn.execute("""

        SELECT
            name,
            SUM(spend) AS total_spend

        FROM read_csv_auto('aws_s3_bucket/transactions.csv')

        GROUP BY name

    """).df()

    print("\n[AWS Athena Simulation]\n")
    print(result)

    conn.close()
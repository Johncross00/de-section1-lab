from pathlib import Path

import duckdb
import pandas as pd

GCS_BUCKET = Path("gcp_storage_bucket")
GCS_BUCKET.mkdir(exist_ok=True)


def run_gcp():

    print("\n" + "=" * 50)
    print("Google Cloud Storage + BigQuery")
    print("=" * 50)

    events = pd.DataFrame([
        {"user": "Alice", "event": "login"},
        {"user": "Bob", "event": "purchase", "amount": 250},
        {"user": "Alice", "event": "purchase", "amount": 500},
    ])

    events.to_json(
        GCS_BUCKET / "events.json",
        orient="records",
        lines=True
    )

    print("[GCP] Wrote events to simulated GCS bucket")

    conn = duckdb.connect()

    result = conn.execute("""

        SELECT
            user,
            COUNT(*) AS actions,
            SUM(amount) AS total_amount

        FROM read_json_auto('gcp_storage_bucket/events.json')

        GROUP BY user

    """).df()

    print("\n[GCP BigQuery Simulation]\n")
    print(result)

    conn.close()
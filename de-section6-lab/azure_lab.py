from pathlib import Path

import duckdb
import pandas as pd

AZURE_CONTAINER = Path("azure_blob_container")
AZURE_CONTAINER.mkdir(exist_ok=True)


def run_azure():

    print("\n" + "=" * 50)
    print("Azure Blob + Synapse")
    print("=" * 50)

    data = pd.DataFrame({
        "region": ["US", "EU", "APAC"],
        "revenue": [1000, 700, 400]
    })

    data.to_parquet(
        AZURE_CONTAINER / "revenue.parquet",
        index=False
    )

    print("[Azure] Stored data in simulated blob storage")

    conn = duckdb.connect()

    result = conn.execute("""

        SELECT
            region,
            revenue,
            revenue * 0.10 AS tax_estimate

        FROM read_parquet('azure_blob_container/revenue.parquet')

    """).df()

    print("\n[Azure Synapse Simulation]\n")
    print(result)

    conn.close()
import pandas as pd

from pipeline.database import get_connection


def run_batch():

    print("=" * 50)
    print("Starting Batch Pipeline")
    print("=" * 50)

    raw = pd.DataFrame({
        "customer": ["Alice", "Bob", "Alice", "Eve"],
        "amount": [100, 200, 50, 300],
        "date": [
            "2024-01-01",
            "2024-01-01",
            "2024-01-02",
            "2024-01-02"
        ]
    })

    raw.to_csv("data/transactions_raw.csv", index=False)

    df = pd.read_csv("data/transactions_raw.csv")

    df["date"] = pd.to_datetime(df["date"])

    df.to_parquet(
        "data/transactions_clean.parquet",
        index=False
    )

    summary = (
        df.groupby(
            ["customer", "date"],
            as_index=False
        )
        .agg(total=("amount", "sum"))
    )

    summary.to_parquet(
        "data/transactions_summary.parquet",
        index=False
    )

    print("Batch pipeline completed.")
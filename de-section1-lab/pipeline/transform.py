from pathlib import Path

import pandas as pd

from pipeline.config import SILVER_FILE


REQUIRED_COLUMNS = {
    "total_bill", "tip", "sex", "smoker", "day", "time", "size"
}


def transform_to_silver(bronze_path: Path) -> Path:
    """
    Read Bronze data, clean it and write it to the Silver layer.
    """

    print("\nTransforming Bronze -> Silver...")

    # Read Bronze data
    df = pd.read_csv(bronze_path)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        raise ValueError(
            "Bronze dataset is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    # Values are required for downstream aggregation and validation.
    if df[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Bronze dataset contains missing values in required columns.")

    if (df["total_bill"] <= 0).any():
        raise ValueError("Bronze dataset contains non-positive total_bill values.")

    # Derived column
    df["tip_pct"] = (df["tip"] / df["total_bill"]).round(4)

    # Synthetic datetime
    df["visit_datetime"] = pd.date_range(
        "2024-01-01",
        periods=len(df),
        freq="h"
    )


    # Save to Silver
    df.to_parquet(SILVER_FILE, index=False)

    print(f"[SILVER] {len(df)} rows written.")

    return SILVER_FILE

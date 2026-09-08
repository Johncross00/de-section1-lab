from pathlib import Path

import pandas as pd

from pipeline.config import GOLD_FILE


def aggregate_to_gold(silver_path: Path) -> Path:
    """
    Read Silver data and create an aggregated Gold dataset.
    """

    print("\nAggregating Silver -> Gold...")

    # Read Silver dataset
    df = pd.read_parquet(silver_path)

    # Aggregate
    summary = (
        df.groupby(
            ["sex", "smoker", "day"],
            as_index=False
        )
        .agg(
            avg_tip_pct=("tip_pct", "mean"),
            total_revenue=("total_bill", "sum"),
            rows=("tip_pct", "count"),
        )
    )

    # Save Gold dataset
    summary.to_parquet(GOLD_FILE, index=False)

    print(f"[GOLD] {len(summary)} rows written.")

    return GOLD_FILE
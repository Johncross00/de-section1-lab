from pathlib import Path

import pandas as pd

from pipeline.config import BRONZE_FILE, RAW_URL


def extract_to_bronze() -> Path:
    """
    Extracts the raw dataset from the source URL
    and stores it in the Bronze layer.
    """

    print("=" * 50)
    print("Starting Bronze ingestion...")
    print("=" * 50)

    try:

        df = pd.read_csv(RAW_URL)

        df.to_csv(BRONZE_FILE, index=False)

        print(f"Dataset downloaded successfully.")
        print(f"Rows      : {len(df)}")
        print(f"Columns   : {len(df.columns)}")
        print(f"Saved to  : {BRONZE_FILE}")

        return BRONZE_FILE

    except Exception as error:

        raise RuntimeError(
            f"Bronze extraction failed: {error}"
        )

# pipeline/extract.py

import pandas as pd

URL = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
OUTPUT = "data/airtravel.csv"


def extract():
    df = pd.read_csv(URL)

    df.columns = (
    df.columns
      .str.strip()
      .str.replace('"', '', regex=False)
      .str.lower()
)

    df.to_csv(OUTPUT, index=False)

    print("=" * 50)
    print("Dataset extracted successfully")
    print("=" * 50)
    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")
    print(f"Saved   : {OUTPUT}")

    return df
import pandas as pd

from pipeline.database import get_connection


def run_etl(df: pd.DataFrame):
    print("\nStarting ETL...")

    # Rename columns
    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    year_col = df.columns[1]

    print(year_col)
    print(df[year_col])

    df[year_col] = df[year_col].astype(int)

    print(df[year_col])

    df_filtered = df[df[year_col] > 300]

    print(df_filtered)

    # Load into DuckDB
    conn = get_connection()

    conn.execute("DROP TABLE IF EXISTS air_travel_etl")

    conn.register("temp_df", df_filtered)

    conn.execute("""
        CREATE TABLE air_travel_etl AS
        SELECT *
        FROM temp_df
    """)

    conn.close()

    print(f"Loaded {len(df_filtered)} rows into air_travel_etl")

    return df_filtered
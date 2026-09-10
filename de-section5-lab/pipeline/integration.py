import pandas as pd

from pipeline.database import get_connection


def run_etl():

    print("\n" + "=" * 50)
    print("Running ETL")
    print("=" * 50)

    df = pd.read_json(
        "data/raw_events.json",
        lines=True
    )

    # Transformation AVANT chargement
    purchases = df[df["action"] == "purchase"].copy()

    purchases["amount"] = purchases["amount"].fillna(0)

    conn = get_connection()

    conn.execute("""
        CREATE OR REPLACE TABLE purchases_etl AS
        SELECT * FROM purchases
    """)

    print(conn.execute(
        "SELECT * FROM purchases_etl"
    ).df())

    conn.close()


def run_elt():

    print("\n" + "=" * 50)
    print("Running ELT")
    print("=" * 50)

    conn = get_connection()

    conn.execute("""
        CREATE OR REPLACE TABLE raw_events AS
        SELECT *
        FROM read_json_auto('data/raw_events.json')
    """)

    conn.execute("""
        CREATE OR REPLACE TABLE purchases_elt AS

        SELECT *

        FROM raw_events

        WHERE action='purchase'
    """)

    print(conn.execute(
        "SELECT * FROM purchases_elt"
    ).df())

    conn.close()
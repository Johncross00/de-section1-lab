import pandas as pd

from pipeline.database import get_connection


def create_lake():

    print("\n" + "=" * 50)
    print("Creating Data Lake")
    print("=" * 50)

    events = pd.DataFrame([
        {
            "event_id": 1,
            "user": "Alice",
            "action": "login"
        },
        {
            "event_id": 2,
            "user": "Bob",
            "action": "purchase",
            "amount": 25
        },
        {
            "event_id": 3,
            "user": "Alice",
            "action": "purchase",
            "amount": 999
        }
    ])

    events.to_json(
        "data/raw_events.json",
        orient="records",
        lines=True
    )

    print("Raw JSON created.")

    conn = get_connection()

    result = conn.execute("""

        SELECT
            user,
            action,
            amount

        FROM read_json_auto('data/raw_events.json')

        WHERE action='purchase'

    """).df()

    print("\n=== Data Lake Query ===\n")

    print(result)

    conn.close()
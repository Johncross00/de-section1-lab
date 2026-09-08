import pandas as pd
import pandera.pandas as pa
from pandera import Check

from pipeline.config import SILVER_FILE


def validate_silver(silver_path=SILVER_FILE):
    """
    Validate the Silver dataset using Pandera.
    """

    print("\nValidating Silver dataset...")

    df = pd.read_parquet(silver_path)

    schema = pa.DataFrameSchema(
        {
            "total_bill": pa.Column(float, Check.ge(0)),
            "tip": pa.Column(float, Check.ge(0)),
            "sex": pa.Column(str),
            "smoker": pa.Column(str),
            "day": pa.Column(str),
            "time": pa.Column(str),
            "size": pa.Column(int, Check.ge(1)),
            "tip_pct": pa.Column(float, Check.between(0, 1)),
            "visit_datetime": pa.Column(
                "datetime64[ns]"
            ),
        }
    )

    schema.validate(df)

    print("[VALID] Silver dataset is valid.")

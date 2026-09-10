import pandas as pd


def run_quality_checks():
    print("=" * 50)
    print("Running Data Quality Checks")
    print("=" * 50)

    df = pd.read_csv("data/airtravel.csv")

    print("\nDataset Preview")
    print(df.head())

    print("\nRunning Checks...\n")

    # 1. Vérifier les colonnes
    expected_columns = ["month", "1958", "1959", "1960"]

    assert list(df.columns) == expected_columns, \
        "❌ Unexpected column names"

    # 2. Vérifier les valeurs nulles
    assert df["1958"].isnull().sum() == 0
    assert df["1959"].isnull().sum() == 0
    assert df["1960"].isnull().sum() == 0

    # 3. Vérifier les valeurs positives
    assert (df["1958"] > 0).all()

    print("✅ All quality checks passed!")
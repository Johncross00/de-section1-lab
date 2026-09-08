from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

RAW_URL = (
    "https://raw.githubusercontent.com/"
    "mwaskom/seaborn-data/master/tips.csv"
)

BRONZE_FILE = BRONZE_DIR / "tips_raw.csv"
SILVER_FILE = SILVER_DIR / "tips_clean.parquet"
GOLD_FILE = GOLD_DIR / "tips_summary.parquet"

for folder in (
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
):
    folder.mkdir(parents=True, exist_ok=True)
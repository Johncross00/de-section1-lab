from datetime import datetime


def generate_metadata():
    metadata = {
        "dataset": "AirTravel",
        "owner": "John Cross",
        "source": "CSV",
        "rows": 12,
        "columns": 4,
        "created_at": datetime.now().isoformat(),
        "classification": "Internal"
    }

    print("=" * 50)
    print("Dataset Metadata")
    print("=" * 50)

    for key, value in metadata.items():
        print(f"{key}: {value}")
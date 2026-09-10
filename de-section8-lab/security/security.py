import pandas as pd


def secure_dataset():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "email": [
            "alice@email.com",
            "bob@email.com",
            "charlie@email.com"
        ]
    })

    print("=" * 50)
    print("Original Dataset")
    print("=" * 50)
    print(df)

    # Masquage des emails
    df["email"] = df["email"].apply(
        lambda x: "***@" + x.split("@")[1]
    )

    print("\nSecured Dataset")
    print("=" * 50)
    print(df)
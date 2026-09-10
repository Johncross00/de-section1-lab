import pandas as pd


def create_warehouse():

    print("=" * 50)
    print("Creating Data Warehouse")
    print("=" * 50)

    dim_customer = pd.DataFrame({
        "customer_id": [1, 2, 3],
        "name": ["Alice", "Bob", "Eve"],
        "region": ["US", "EU", "US"]
    })

    dim_product = pd.DataFrame({
        "product_id": [10, 11, 12],
        "name": ["Laptop", "Mouse", "Keyboard"],
        "category": [
            "Electronics",
            "Accessories",
            "Accessories"
        ]
    })

    fact_sales = pd.DataFrame({
        "sale_id": [1001, 1002, 1003, 1004],
        "customer_id": [1, 2, 1, 3],
        "product_id": [10, 11, 12, 10],
        "amount": [999, 25, 50, 999],
        "date": [
            "2024-01-01",
            "2024-01-01",
            "2024-01-02",
            "2024-01-02"
        ]
    })

    dim_customer.to_parquet(
        "data/dim_customer.parquet",
        index=False
    )

    dim_product.to_parquet(
        "data/dim_product.parquet",
        index=False
    )

    fact_sales.to_parquet(
        "data/fact_sales.parquet",
        index=False
    )

    print("Warehouse created.")
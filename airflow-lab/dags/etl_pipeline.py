from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

import duckdb
import pandas as pd


def extract_data():

    print("Extracting dataset...")

    df = pd.read_csv("/opt/airflow/dags/data/airtravel.csv")

    df.to_csv(
        "/opt/airflow/dags/data/extracted.csv",
        index=False
    )

    print(df.head())


def transform_data():

    print("Transforming dataset...")

    df = pd.read_csv(
        "/opt/airflow/dags/data/extracted.csv"
    )

    df.columns = [
        c.replace('"', "")
        .lower()
        for c in df.columns
    ]

    df["1958"] = df["1958"].astype(int)

    df = df[df["1958"] > 300]

    df.to_csv(
        "/opt/airflow/dags/data/transformed.csv",
        index=False
    )

    print(df.head())

def load_data():

    print("Loading into DuckDB...")

    conn = duckdb.connect(
        "/opt/airflow/dags/data/airtravel.duckdb"
    )

    df = pd.read_csv(
        "/opt/airflow/dags/data/transformed.csv"
    )

    conn.execute("""

        CREATE OR REPLACE TABLE air_travel AS

        SELECT *

        FROM df

    """)

    print(

        conn.execute(

            "SELECT * FROM air_travel"

        ).df()

    )

    conn.close()


with DAG(
    dag_id="etl_airflow_demo",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["lab", "etl", "duckdb"],
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_data,
    )

    extract >> transform >> load
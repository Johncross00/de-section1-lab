from pipeline.integration import run_etl, run_elt
from pipeline.lake import create_lake
from pipeline.lakehouse import run_lakehouse
from pipeline.query import warehouse_query
from pipeline.warehouse import create_warehouse


def main():

    create_warehouse()

    warehouse_query()

    create_lake()

    run_lakehouse()

    run_etl()

    run_elt()


if __name__ == "__main__":
    main()
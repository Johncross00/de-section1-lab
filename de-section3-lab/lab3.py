from pipeline.extract import extract
from pipeline.etl import run_etl
from pipeline.elt import run_elt
from pipeline.query import show_results


def main():
    df = extract()

    run_etl(df)

    run_elt(df)

    show_results()


if __name__ == "__main__":
    main()
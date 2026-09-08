from pipeline.batch import run_batch
from pipeline.query import batch_query
from pipeline.streaming import run_stream


def main():

    run_batch()

    batch_query()

    run_stream()


if __name__ == "__main__":
    main()
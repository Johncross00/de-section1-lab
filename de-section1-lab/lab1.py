from pipeline.extract import extract_to_bronze
from pipeline.transform import transform_to_silver
from pipeline.aggregate import aggregate_to_gold
from pipeline.query import query_examples
from pipeline.validate import validate_silver

def main():

    bronze = extract_to_bronze()

    silver = transform_to_silver(bronze)

    validate_silver(silver)

    gold = aggregate_to_gold(silver)

    query_examples()


if __name__ == "__main__":
    main()
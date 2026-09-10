from quality.quality_check import run_quality_checks
from governance.metadata import generate_metadata
from security.security import secure_dataset


def main():
    run_quality_checks()
    print()

    generate_metadata()
    print()

    secure_dataset()


if __name__ == "__main__":
    main()
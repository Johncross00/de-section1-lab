from aws_lab import run_aws
from azure_lab import run_azure
from gcp_lab import run_gcp
from integration import run_integration


def main():

    run_aws()

    run_azure()

    run_gcp()

    run_integration()


if __name__ == "__main__":
    main()
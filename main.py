import argparse
import sys

from models.employee import Employee
from parsers.csv_parser import parse_csv
from reports.payout_report import generate_payout_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        nargs="+",
        help="List of paths to CSV files with employee data"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["payout"],
        help="Report type (for example, payment)")

    parser.add_argument(
        "--format",
        choices=["table", "json"],
        default="table",
        help="Output format of the report"
    )

    args = parser.parse_args()

    employees = []
    for file in args.files:
        employees.extend(parse_csv(file))

    if args.report == "payout":
        report = generate_payout_report(
            employees=employees,
            format=args.format
        )
        print(report)
    else:
        print("Invalid report")
        sys.exit(1)

if __name__ == "__main__":
    main()
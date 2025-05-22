from typing import List

from models.employee import Employee


def parse_csv(csv_file_path : str) -> List[Employee]:
    with open(csv_file_path, "r", encoding="utf-8") as f:
        lines=f.readlines()

    headers = [h.strip().lower() for h in lines[0].strip().split(",")]

    required_fields = {"name", "department", "hours_worked"}
    if not required_fields.issubset(set(headers)):
        raise ValueError(f"Required columns are missing: {required_fields - set(headers)}")

    rate_column = next((col for col in ("hourly_rate", "rate", "salary") if col in headers), None)
    if rate_column is None:
        raise ValueError("Payment column not found (hourly_rate / rate / salary)")

    results = []
    for line in lines[1:]:
        values = [v.strip() for v in line.strip().split(",")]
        row = dict(zip(headers, values))

        hourly_raw = row.get("hourly_rate") or row.get("rate") or row.get("salary")


        employee_data = Employee(
            id=int(row["id"]) if "id" in row else None,
            email=row.get("email"),
            name=row.get("name"),
            department=row.get("department"),
            hours_worked=float(row.get("hours_worked")),
            hourly_rate=float(hourly_raw),
        )

        results.append(employee_data)

    return results

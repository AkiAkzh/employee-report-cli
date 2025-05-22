import json
from collections import defaultdict
from typing import List

from models.employee import Employee


def generate_payout_report(employees : List[Employee],  format: str = "table") -> str:
    departments = defaultdict(list)
    for emp in employees:
        departments[emp.department].append(emp)

    lines = []

    if format == "json":
        result = {}
        for department, emps in departments.items():
            emp_list = []
            total_payout = 0
            total_hours = 0
            for emp in emps:
                payout = emp.hours_worked * emp.hourly_rate
                total_hours += emp.hours_worked
                total_payout += payout
                emp_list.append({
                    "name": emp.name,
                    "hours_worked": int(emp.hours_worked),
                    "hourly_rate": emp.hourly_rate,
                    "payout": int(payout)
                })
            result[department] = {
                "employees": emp_list,
                "total_hours_worked": int(total_hours),
                "total_payout": int(total_payout)
            }
        return json.dumps(result, indent=4, ensure_ascii=False)



    for department, emps in departments.items():

        lines.append(f"{department}")
        lines.append(" " * 16 + " name              hours  rate   payout")
        total_payout = 0
        total_hours = 0
        for emp in emps:
            payout = emp.hours_worked * emp.hourly_rate
            total_hours  += emp.hours_worked
            total_payout += payout
            lines.append(
                f"{'-' * 16} {emp.name:<18}{int(emp.hours_worked):<7}{int(emp.hourly_rate):<7}${int(payout)}"
            )
        lines.append(" " * 16 + f" {'':<18}{int(total_hours):<7}{'':<7}${int(total_payout)}")
        lines.append("")

    return "\n".join(lines)
import pytest
from typing import List
from models.employee import Employee
from reports.payout_report import generate_payout_report

def create_employees() -> List[Employee]:
    return [
        Employee(name="Yuna Kim", department="Marketing", hours_worked=160, hourly_rate=50),
        Employee(name="Haruka Tanaka", department="Design", hours_worked=150, hourly_rate=35),
        Employee(name="Miyu Sato", department="Design", hours_worked=140, hourly_rate=40),
        Employee(name="Soojin Park", department="HR", hours_worked=155, hourly_rate=42),
    ]

def test_generate_payout_report_structure():
    employees = create_employees()
    report = generate_payout_report(employees)

    assert "Marketing" in report
    assert "Design" in report
    assert "HR" in report

def test_generate_payout_report_values():
    employees = [
        Employee(name="Yuna Kim", department="Marketing", hours_worked=160, hourly_rate=50),  # 8000
        Employee(name="Haruka Tanaka", department="Marketing", hours_worked=150, hourly_rate=40),  # 6000
    ]
    report = generate_payout_report(employees)

    assert "Yuna Kim" in report
    assert "$8000" in report
    assert "$6000" in report
    assert "$14000" in report  # total

def test_generate_payout_report_formatting():
    employees = [
        Employee(name="Miyu Sato", department="Sales", hours_worked=100, hourly_rate=25),  # 2500
    ]
    report = generate_payout_report(employees)

    assert "Sales" in report
    assert "Miyu Sato" in report
    assert "$2500" in report
    assert "$2500" in report.splitlines()[-2]  # Total payout

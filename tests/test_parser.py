import pytest
from textwrap import dedent
from models.employee import Employee
from parsers.csv_parser import parse_csv
import tempfile

def create_temp_csv(content: str) -> str:
    temp = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".csv")
    temp.write(content)
    temp.close()
    return temp.name

def test_parse_csv_with_hourly_rate():
    csv_data = dedent("""\
        id,email,name,department,hours_worked,hourly_rate
        1,yuna@example.com,Yuna Kim,Marketing,160,50
    """)
    path = create_temp_csv(csv_data)
    employees = parse_csv(path)

    assert len(employees) == 1
    emp = employees[0]
    assert emp.name == "Yuna Kim"
    assert emp.department == "Marketing"
    assert emp.hours_worked == 160
    assert emp.hourly_rate == 50

def test_parse_csv_with_rate():
    csv_data = dedent("""\
        name,department,hours_worked,rate
        Haruka Tanaka,Design,150,35
    """)
    path = create_temp_csv(csv_data)
    employees = parse_csv(path)

    assert len(employees) == 1
    emp = employees[0]
    assert emp.name == "Haruka Tanaka"
    assert emp.department == "Design"
    assert emp.hours_worked == 150
    assert emp.hourly_rate == 35

def test_parse_csv_with_salary():
    csv_data = dedent("""\
        name,department,hours_worked,salary
        Miyu Sato,Sales,160,37
    """)
    path = create_temp_csv(csv_data)
    employees = parse_csv(path)

    assert len(employees) == 1
    emp = employees[0]
    assert emp.name == "Miyu Sato"
    assert emp.department == "Sales"
    assert emp.hours_worked == 160
    assert emp.hourly_rate == 37

def test_parse_csv_missing_rate_column():
    csv_data = dedent("""\
        name,department,hours_worked
        Soojin Park,HR,150
    """)
    path = create_temp_csv(csv_data)

    with pytest.raises(ValueError):
        parse_csv(path)

from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    name : str
    department : str
    hours_worked : float
    hourly_rate : float
    id: Optional[int] = None
    email: Optional[str] = None
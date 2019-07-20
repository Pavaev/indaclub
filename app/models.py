from dataclasses import dataclass, field
from typing import Dict

from app.constants import Activity, StyleType


@dataclass(frozen=True)
class Style:
    name: str
    style_type: StyleType
    dance_description: str


@dataclass
class Person:
    name: str
    styles: Dict[str, Style] = field(default_factory=dict)
    activity: Activity = field(default=None)

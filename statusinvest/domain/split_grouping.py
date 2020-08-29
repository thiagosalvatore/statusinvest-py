from dataclasses import dataclass
from datetime import date
from typing import Tuple

from statusinvest.enums import EventType


@dataclass
class SplitGrouping:
    """
    This class is responsible for storing information about spliting and grouping events
    """

    event_type: EventType = None
    announcement_date: date = None
    start_date: date = None
    proportion: Tuple[float, float] = None

from dataclasses import dataclass
from datetime import date


@dataclass
class Bonus:
    """
    This class is responsible for storing information about bonus events
    """

    announcement_date: date = None
    date_ex_bonus: date = None
    data_com_bonus: date = None
    incorporation_date: date = None
    base_value: float = None
    proportion: float = None
    received_ticker: str = None

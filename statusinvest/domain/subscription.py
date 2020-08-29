from dataclasses import dataclass
from datetime import date


@dataclass
class Subscription:
    """
    This class is responsible for storing information about subscription events
    """

    announcement_date: date = None
    reference_date: date = None
    base_value: float = None
    percentage: float = None
    received_ticker: str = None

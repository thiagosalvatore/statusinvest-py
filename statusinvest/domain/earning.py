from dataclasses import dataclass
from datetime import date

from statusinvest.enums import EarningType


@dataclass
class Earning:
    """
    This class is responsible for storing information about earnings events
    """

    earning_type: EarningType = None
    reference_date: date = None
    payment_date: date = None
    value: float = None
    description: str = None

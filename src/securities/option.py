from dataclasses import dataclass
from helper_objects import Price
from stock import Stock
from enum import Enum
from datetime import date

class Direction(Enum):
    BUY = 0
    SELL = 1

class OptionType(Enum):
    CALL = 0
    PUT = 1

@dataclass
class Option:
    """Class for holding a single option contract."""
    stock: Stock

    direction: Direction
    option_type: OptionType

    date: date
    price: Price

    volume: int

    # Calculated variables:
        # IV
        # Black Scholes fair price
        # Total Cost?
        # PnL until expiry?
from dataclasses import dataclass
from helper_objects import Price

@dataclass
class Stock:
    """Class for holding a single stock."""
    name: str
    ticker: str

    price: Price

@dataclass
class StockPosition:
    """Class for holding a position consisting of one type of stock"""

    stock: Stock
    amount: int
    average_buy_price: float

    def total_cost(self) -> float:
        return self.amount * self.average_buy_price

    def total_value(self) -> float:
        return self.amount * self.stock.price.ask

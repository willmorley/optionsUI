from dataclasses import dataclass

@dataclass
class Price:
    """Class holding a price"""

    bid: float
    ask: float

    def spread(self) -> float:
        return self.ask - self.bid

    def spread_percent(self) -> float:
        return self.spread() / self.ask